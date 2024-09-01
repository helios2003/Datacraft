"""
Module contains a list of helper functions required in main.py
"""
import os
import pandas as pd
from sqlalchemy import exc
from db.init import engine, Session
from db.models import MergedSheet

session = Session()

def delete_files_in_directory(directory_path: str) -> None:
    """
    Deletes all the files in the directory
    
    Args:
        directory_path: Path to the directory
        
    Returns:
        None
    """
    try:
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except OSError:
        print("Error occurred while deleting files.")

def copy_cols_data(df_source: pd.DataFrame, df_target: pd.DataFrame, col: str) -> bool:
    """
    Copies the column's data from source dataframe to target dataframe
    
    Args:
        df_source: pd.DataFrame
        df_target: pd.DataFrame
        col: str
        
    Returns:
        bool: That column exists and it could be successfully copied
    """
    if col in df_source.columns:
        df_target[col] = df_source[col]
        return True
    return False

def categorize_tolerance(row: pd.core.series.Series) -> str:
    """
    Gives the tolerance of the data based on a variety of factors
    
    Args:
        row: A pandas dataframe's row
        
    Returns:
        Tolerance (str): If tolerance is breached or not 
    """
    pna = row['total']
    percentage = row['percentage']
    
    if 0 < pna <= 300:
        return 'Within Tolerance' if percentage > 50 else 'Tolerance Breached'
    elif 301 < pna <= 500:
        return 'Within Tolerance' if percentage > 45 else 'Tolerance Breached'
    elif 501 < pna <= 900:
        return 'Within Tolerance' if percentage > 43 else 'Tolerance Breached'
    elif 901 < pna <= 1500:
        return 'Within Tolerance' if percentage > 38 else 'Tolerance Breached'
    elif pna > 1500:
        return 'Within Tolerance' if percentage > 30 else 'Tolerance Breached'
    return 'Tolerance Breached'
    
def generate_grouped_table() -> None:
    """
    Groups the table based on order ID and transaction type
    
    Args:
        None
        
    Returns:
        None: If successfully completed the grouping process
    """
    try:
        statement = session.query(MergedSheet).all()
        df = pd.DataFrame([row.__dict__ for row in statement])
        
        if '_sa_instance_state' in df.columns:
            df = df.drop(columns=['_sa_instance_state'])
            
        df_filtered = df.dropna(subset=['order_id'])
        
        # Grouping the data by description
        df_summary = df.groupby(['description']).agg({
            'total': 'sum'
        })
        
        # Grouping the data by order_id and then by transaction type
        df_grouped = df_filtered.groupby(['order_id', 'transaction_type']).agg({
            'invoice_amt': 'sum',
            'total': 'sum'
        }).reset_index()
        
        df_summary['id'] = range(1, len(df_summary) + 1)
        df_grouped['id'] = range(1, len(df_grouped) + 1)
        
        df_summary.to_sql('summarysheet', engine, if_exists='replace')
        df_grouped.to_sql('groupedsheet', engine, if_exists='replace')
    
    except exc.SQLAlchemyError as e:
        raise e
        