"""
This module contains the API definitions for file uploads and processing.
"""

import os
import shutil
from typing import List
from uuid import uuid4
import pandas as pd
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from helper.functions import delete_files_in_directory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/') 
def root():
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
        os.mkdir('merchant', exist_ok=True)
        os.mkdir('payment', exist_ok=True)
        
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
def process_files():
    """
    Preprocess the data according to the task's instructions
    Args:
        None
    Status:
        200: On successful preprocessing
        500: Internal Server Error
    """
    try:
        merchant_file_path = os.listdir('merchants')[0]
        payment_file_path = os.listdir('payments')[0]
        
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
        
        df_merged = pd.concat([df_merged_merchant, df_merged_payment], ignore_index=True)
        
        return {"msg": "Your dataframes have been successfully processed"}
        
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "An error occured"
        ) from e
        
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
