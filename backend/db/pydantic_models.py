from pydantic import BaseModel
from datetime import datetime

class MergedSheetModel(BaseModel):
    order_id: str
    transaction_type: str
    payment_type: str
    invoice_amount: float
    total: float
    description: str
    order_date: datetime
    date_time: datetime

    class Config:
        anystr_strip_whitespace = True
        date_format = 'iso'