"""
This module contains the API definitions for file uploads and processing.
"""

import os
import glob
import shutil
from typing import List
from uuid import uuid4
import pandas as pd
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from helper.functions import delete_files_in_directory, copy_cols_data, categorize_tolerance, generate_grouped_table
from db.init import engine, Session
from db.models import MergedSheet, GroupedSheet, OrderPaymentReceivedSheet, ReturnSheet, PaymentPendingSheet, NegativePayoutsSheet, ToleranceBreachedSheet
from sqlalchemy import func, text
from urllib.parse import unquote
from sqlalchemy.future import select
from db.init import table_exists

session = Session()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/') 
def root() -> dict:
    """
    Root endpoint
    
    Args:
        None
        
    Returns:
        JSON: A welcome message.
    """
    return {"msg": "Welcome to the backend, this is a test endpoint"}

@app.post('/upload')
def upload_files(files: List[UploadFile] = File(...)) -> dict:
    """
    Upload endpoint which accepts user's files
    
    Args:
        files: List of 2 files
        
    Returns:
        JSON: A JSON object informing the status of the request
        
    Status:
        200: Successful upload
        400: If 2 files are not uploaded
        500: Internal Server Error
    """
    try:
        if len(files) != 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Please upload exactly two files"
            )
        if (files[0].filename.split('.')[-1] != 'xlsx' or 
            files[1].filename.split('.')[-1] != 'csv'):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file type"
            ) 
        os.makedirs('merchant', exist_ok=True)
        os.makedirs('payment', exist_ok=True)
        
        # all the other files in the directories are deleted to save these 2 files
        delete_files_in_directory('merchant')
        delete_files_in_directory('payment')
        
        merchant_file = str(uuid4())
        payment_file = str(uuid4())
        
        with open(os.path.join('merchant', merchant_file), "wb") as buffer:
            shutil.copyfileobj(files[0].file, buffer)
        
        with open(os.path.join('payment', payment_file), "wb") as buffer:
            shutil.copyfileobj(files[1].file, buffer)
        return {"msg": "Files uploaded successfully"}
            
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "An error occured"
        ) from e
        
@app.get('/process')
def process_files() -> dict:
    """
    Preprocess the data according to the task's instructions
    
    Args:
        None
        
    Status:
        200: On successful preprocessing
        500: Internal Server Error
    """
    try:
        merchant_file_path = glob.glob(os.path.join('merchant', '*'))[0]
        payment_file_path = glob.glob(os.path.join('payment', '*'))[0]
        
        df_merchant = pd.DataFrame(pd.read_excel(merchant_file_path))
        df_payment = pd.read_csv(payment_file_path)
        
        # preprocessing for merchant file        
        df_merchant = df_merchant[df_merchant["Transaction Type"] != "Cancel"]
        df_merchant['Transaction Type'] = df_merchant['Transaction Type'].str.replace('Refund', 
                                                                                      'Return')
        df_merchant['Transaction Type'] = df_merchant['Transaction Type'].str.replace('FreeReplacement', 
                                                                                      'Return')
        
        # preprocessng for payment file
        df_payment = df_payment[df_payment["type"] != "Transfer"]
        
        df_payment.rename(columns={"type": "Payment Type"}, inplace=True)
        df_payment.rename(columns={"order id": "Order Id"}, inplace=True)

        df_payment["Payment Type"] = df_payment["Payment Type"].str.replace("Adjustment", "Order")
        df_payment["Payment Type"] = df_payment["Payment Type"].str.replace("FBA Inventory Fee", "Order")
        df_payment["Payment Type"] = df_payment["Payment Type"].str.replace("Fulfilment Fee Refund", "Order")
        df_payment["Payment Type"] = df_payment["Payment Type"].str.replace("Service Fee", "Order")
        df_payment["Payment Type"] = df_payment["Payment Type"].str.replace("Refund", "Return")
        df_payment["Transaction Type"] = "Payment"
        
        # Merging the 2 dataframes
        df_merged_cols = ['Order Id', 'Transaction Type', 'Payment Type', 'Invoice Amount', 'total', 
                          'description', 'Order Date', 'date/time']
        
        df_merged_merchant = pd.DataFrame(columns=df_merged_cols)
        df_merged_payment = pd.DataFrame(columns=df_merged_cols)
        
        for col in df_merged_cols:
            copy_cols_data(df_merchant, df_merged_merchant, col)
            copy_cols_data(df_payment, df_merged_payment, col)
        
        df_merged = pd.concat([df_merged_merchant, df_merged_payment], ignore_index=True)
        df_mapped = df_merged.rename(columns={
                    'Order Id': 'order_id',
                    'Transaction Type': 'transaction_type',
                    'Payment Type': 'payment_type',
                    'Invoice Amount': 'invoice_amt',
                    'total': 'total',
                    'description': 'description',
                    'Order Date': 'order_date',
                    'date/time': 'date_time'
                }) 
        df_mapped['id'] = range(1, len(df_mapped) + 1)
        df_mapped['total'] = df_mapped['total'].str.replace(',', '').astype(float)
        
        df_mapped.to_sql('mergedsheet', engine, if_exists='replace')

        return {"msg": "Your dataframes have been successfully processed"}
        
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "An error occured"
        ) from e

@app.get('/generate/tables')        
def generate_tables() -> dict:
    """
    Creates all the relevant tables after processing the datasets
    
    Args:
        None

    Returns:
        dict: a success message

    Status:
        200: If all the preprocessing steps were successful
        500: If server side error exists
    """
    try:
        # try grouping the table(s) as mentioned in the task
        generate_grouped_table()
        
        statement = session.query(GroupedSheet).all()
        df = pd.DataFrame([row.__dict__ for row in statement])
        
        if '_sa_instance_state' in df.columns:
            df = df.drop(columns=['_sa_instance_state'])
        
        # 1. Mark Removal Order IDs
        df_rem_ids = df.copy()
        df_rem_ids.loc[df_rem_ids['order_id'].str.len() == 10, 'order_id'] = 'Removal Order IDs'
        df_rem_ids['id'] = range(1, len(df_rem_ids) + 1)
        
        # 2. Mark Returns
        df_ret = df.copy()
        df_ret.loc[(df_ret['transaction_type'] == 'Return') & 
                   (df_ret['invoice_amt'].notna()), 'transaction_type'] = 'Return'
        df_ret['id'] = range(1, len(df_ret) + 1)
        
        # 3. Mark Negative Payouts
        df_neg = df.copy()
        df_neg.loc[(df_neg['transaction_type'] == 'Payment') & 
                   (df_neg['total'] < 0), 'transaction_type'] = 'Negative Payout'
        df_neg['id'] = range(1, len(df_neg) + 1)

        # 4. Mark Order & Payment Received
        df_rec = df.copy()
        df_rec.loc[
            (df_rec['order_id'].notna()) & 
            (df_rec['total'].notna()) & 
            (df_rec['invoice_amt'].notna()), 
            'transaction_type'
        ] = 'Order & Payment Received'
        df_rec['id'] = range(1, len(df_rec) + 1)

        # 5. Mark Order Not Applicable but Payment Received
        df_not_app = df.copy()
        df_not_app.loc[
            (df_not_app['order_id'].notna()) & 
            (df_not_app['total'].notna()) & 
            (df_not_app['invoice_amt'].isna()), 
            'transaction_type'
        ] = 'Order Not Applicable but Payment Received'
        df_not_app['id'] = range(1, len(df_not_app) + 1)

        # 6. Mark Payment Pending
        df_pending = df.copy()
        df_pending.loc[
            (df_pending['order_id'].notna()) & 
            (df_pending['invoice_amt'].notna()) & 
            (df_pending['total'].isna()), 
            'transaction_type'
        ] = 'Payment Pending'
        df_pending['id'] = range(1, len(df_pending) + 1)
        
        # 7. Tolerance Breached or not Breached
        df_tolerance = df.copy()
        df_tolerance = df_tolerance[(df_tolerance['invoice_amt'] != 0) & 
                                    df_tolerance['total'].notna()]
        
        df_tolerance['percentage'] = (df_tolerance['total'] / df_tolerance['invoice_amt']) * 100
        df_tolerance['tolerance_status'] = df_tolerance.apply(categorize_tolerance, axis=1)
        
        df_within_tolerance = df_tolerance[df_tolerance['tolerance_status'] == 'Within Tolerance']
        df_tolerance_breached = df_tolerance[df_tolerance['tolerance_status'] == 'Tolerance Breached']

        df_within_tolerance['id'] = range(1, len(df_within_tolerance) + 1)
        df_tolerance_breached['id'] = range(1, len(df_tolerance_breached) + 1)

        # Store the dataframes in the DB
        df_rem_ids.to_sql('removalorderidssheet', con=engine, if_exists='replace')
        df_ret.to_sql('returnsheet', con=engine, if_exists='replace')
        df_neg.to_sql('negativepayoutssheet', con=engine, if_exists='replace')
        df_rec.to_sql('orderpaymentreceivedsheet', con=engine, if_exists='replace')
        df_not_app.to_sql('ordernotapplicablesheet', con=engine, if_exists='replace')
        df_pending.to_sql('paymentpendingsheet', con=engine, if_exists='replace')
        df_within_tolerance.to_sql('withintolerancesheet', con=engine, if_exists='replace')
        df_tolerance_breached.to_sql('tolerancebreachedsheet', con=engine, if_exists='replace')
            
        return {"msg": "All the tables have been created"}
    
    except Exception as e:
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while generating tables"
        ) from e       
    
@app.get('/generate/summary')
def get_summary() -> dict:
    """
    Extract the necessary information from the uploaded datasets
    
    Args:
        None

    Returns:
        dict: the relevant data

    Status:
        200: Returns the data successfully
        500: If server side error exists
    """
    try:
        distinct_count = session.execute(select(func.count(
            GroupedSheet.order_id.distinct()))).scalar()
        
        order_payment_received = session.query(OrderPaymentReceivedSheet).filter(
                        OrderPaymentReceivedSheet.transaction_type == 'Order & Payment Received').count()
        
        payment_pending = session.query(PaymentPendingSheet).filter(
                        PaymentPendingSheet.transaction_type == 'Payment Pending').count() 
        
        tolerance_breached = session.query(ToleranceBreachedSheet).filter(
                        ToleranceBreachedSheet.tolerance_status == 'Tolerance Breached').count()
        
        return_sheet = session.query(ReturnSheet).filter(
                        ReturnSheet.transaction_type == 'Return').count()   
        
        negative_payout = session.query(NegativePayoutsSheet).filter(
                        NegativePayoutsSheet.transaction_type == 'Negative Payout').count() 
        
        return {"distinct_count": distinct_count,
                "order_payment_received": order_payment_received,
                "payment_pending": payment_pending,
                "tolerance_breached": tolerance_breached,
                "return_sheet": return_sheet,
                "negative_payout": negative_payout 
                }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while obtaining the tables"
        ) from e 
        
@app.get('/table')
def get_table(table_name: str) -> dict:
    """
    Retrieve data from a specified table in the database.
    
    Args:
        table_name (str): URL encoded table name

    Returns:
        dict: the relevant table in the dictonary format

    Status:
        200: Returns the table succcesfully
        404: If the table is not found 
        500: If server side error exists
    """
    decoded_name = unquote(table_name)
    name_mapping = {
        "Previous Month Order": "groupedsheet",
        "Order": "orderpaymentreceivedsheet",
        "Payment Pending": "paymentpendingsheet",
        "Tolerance Rate Breached": "tolerancebreachedsheet",
        "Return": "returnsheet",
        "Negative Payout": "negativepayoutssheet"
    }
    
    act_table_name = name_mapping.get(decoded_name)   
    try:
        if not table_exists(act_table_name):
            raise HTTPException(
                status_code=404,
                detail=f"Table '{act_table_name}' does not exist in the database."
            )
            
        query = text(f"SELECT * FROM {act_table_name}")
        result = session.execute(query)
        rows = result.fetchall()
        data = [dict(row._mapping) for row in rows]
        
        return {"data": data}
    
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while obtaining the tables"
        ) from e   
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
