from sqlalchemy import Column, Float, Integer, DateTime, String
from db.init import Base

class MergedSheet(Base):
    __tablename__ = "mergedsheet"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    transaction_type = Column(String)
    payment_type = Column(String)
    invoice_amt = Column(Float)
    total = Column(Float)
    description = Column(String)
    order_date = Column(DateTime)
    date_time = Column(String)
    
class SummarySheet(Base):
    __tablename__ = "summarysheet"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    total = Column(Float) 
    
class GroupedSheet(Base):
    __tablename__ = "groupedsheet"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    transaction_type = Column(String)
    invoice_amt = Column(Float)
    total = Column(Float) 
    
class BaseSheet(Base):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    transaction_type = Column(String)
    invoice_amt = Column(Float)
    total = Column(Float)  
    
class RemovalOrderIDsSheet(BaseSheet):
    __tablename__ = "removalorderidssheet"
    
class ReturnSheet(BaseSheet):
    __tablename__ = "returnsheet"
    
class NegativePayoutsSheet(BaseSheet):
    __tablename__ = "negativepayoutssheet"
    
class OrderPaymentReceivedSheet(BaseSheet):
    __tablename__ = "orderpaymentreceivedsheet"
    
class OrderNotApplicableSheet(BaseSheet):
    __tablename__ = "ordernotapplicablesheet"

class PaymentPendingSheet(BaseSheet):
    __tablename__ = "paymentpendingsheet"
    
class ToleranceBaseSheet(Base):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    transaction_type = Column(String)
    invoice_amt = Column(Float)
    total = Column(Float)  
    tolerance_status = Column(String)
    
class WithinToleranceSheet(ToleranceBaseSheet):
    __tablename__ = "withintolerancesheet"
    
class ToleranceBreachedSheet(ToleranceBaseSheet):
    __tablename__ = "tolerancebreachedsheet"
