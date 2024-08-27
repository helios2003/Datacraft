import os
import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from uuid import uuid4
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
    return {"msg": "Welcome to the backend, this is a test endpoint"}

@app.post('/upload')
def upload_files(files: List[UploadFile] = File(...)):
    """
    Upload endpoint which accepts user's files
    Args:
        files: List of 2 files
    Returns:
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
        if files[0].filename.split('.')[-1] is not 'xlsx' or files[1].filename.split('.')[-1] is not 'csv':
           raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid file type"
                ) 
        os.mkdir('merchant', exist_ok=True)
        os.mkdir('payment', exist_ok=True)
        
        # all the other files in the direcotries are deleted to save these 2 files
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
        )
        
@app.get('/process')
def process_files():
    pass

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)