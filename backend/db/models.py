from sqlalchemy import Boolean, Column, Float, ForeignKey, DateTime, String
from backend.db.init import Base

class MergedSheet(Base):
    __tablename__ = "merged_sheet"
    
    order_id = Column(String)
    transaction_type = Column(String)
    payment_type = Column(String)
    invoice_amt = Column(Float)
    total = Column(String)
    description = Column(String)
    order_date = Column(DateTime)
    date_time = Column(String)
    
