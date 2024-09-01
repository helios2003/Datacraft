"""
Defining the schemas for the various tables in the database
"""

from sqlalchemy import Column, Float, Integer, DateTime, String
from db.init import Base

class MergedSheet(Base):
    """Represents a merged sheet in the database."""
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

    def __repr__(self):
        return f"<MergedSheet(id={self.id}, order_id={self.order_id})>"

class SummarySheet(Base):
    """Represents a summary sheet in the database."""
    __tablename__ = "summarysheet"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    total = Column(Float)

    def __repr__(self):
        return f"<SummarySheet(id={self.id}, description={self.description})>"

class GroupedSheet(Base):
    """Represents a grouped sheet in the database."""
    __tablename__ = "groupedsheet"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    transaction_type = Column(String)
    invoice_amt = Column(Float)
    total = Column(Float)

    def __repr__(self):
        return f"<GroupedSheet(id={self.id}, order_id={self.order_id})>"

class BaseSheet(Base):
    """Base class for various sheet types."""
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    transaction_type = Column(String)
    invoice_amt = Column(Float)
    total = Column(Float)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, order_id={self.order_id})>"

class RemovalOrderIDsSheet(BaseSheet):
    """Represents a sheet for removal order IDs."""
    __tablename__ = "removalorderidssheet"

class ReturnSheet(BaseSheet):
    """Represents a return sheet."""
    __tablename__ = "returnsheet"

class NegativePayoutsSheet(BaseSheet):
    """Represents a sheet for negative payouts."""
    __tablename__ = "negativepayoutssheet"

class OrderPaymentReceivedSheet(BaseSheet):
    """Represents a sheet for orders with received payments."""
    __tablename__ = "orderpaymentreceivedsheet"

class OrderNotApplicableSheet(BaseSheet):
    """Represents a sheet for orders not applicable."""
    __tablename__ = "ordernotapplicablesheet"

class PaymentPendingSheet(BaseSheet):
    """Represents a sheet for pending payments."""
    __tablename__ = "paymentpendingsheet"

class ToleranceBaseSheet(Base):
    """Base class for tolerance-related sheets."""
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String)
    transaction_type = Column(String)
    invoice_amt = Column(Float)
    total = Column(Float)
    tolerance_status = Column(String)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, order_id={self.order_id}, tolerance_status={self.tolerance_status})>"

class WithinToleranceSheet(ToleranceBaseSheet):
    """Represents a sheet for items within tolerance."""
    __tablename__ = "withintolerancesheet"

class ToleranceBreachedSheet(ToleranceBaseSheet):
    """Represents a sheet for items that breached tolerance."""
    __tablename__ = "tolerancebreachedsheet"
