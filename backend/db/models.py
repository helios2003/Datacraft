from sqlalchemy import Column, Float, Integer, DateTime, String
from db.init import Base

class MergedSheet(Base):
    __tablename__ = "MergedSheet"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    transaction_type = Column(String)
    payment_type = Column(String)
    invoice_amt = Column(Float)
    total = Column(Float)
    description = Column(String)
    order_date = Column(DateTime)
    date_time = Column(String)
    
class GroupedTable(Base):
    __tablename__ = "SummarySheet"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    total = Column(Float) 
    
