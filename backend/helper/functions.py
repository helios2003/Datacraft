"""
Module contains a list of helper functions required in main.py
"""
import os

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
