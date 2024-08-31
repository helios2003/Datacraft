"""
Module contains a list of helper functions required in main.py
"""
import os
import shutil
import pandas as pd

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

def categorize_tolerance(row):
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
    else:
        return 'Tolerance Breached'