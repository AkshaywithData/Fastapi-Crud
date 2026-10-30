from sqlalchemy import Column, String, Integer, Date, Numeric,Boolean
from database import Base

class FactExpense(Base):
    __tablename__ = "FactExpense"

    ExpenseID = Column(Integer, primary_key=True)
    DateID = Column(Integer)
    employeeID = Column(Integer)
    DeptID = Column(Integer)
    ExpenseType = Column(String)
    Vendor = Column(String)
    PaymentMode = Column(String)
    Amount = Column(Numeric)    

class Dimemployee(Base):

    __tablename__ = "Dimemployee"

    employeeID = Column(Integer, primary_key=True, autoincrement=True)
    EmployeeName = Column(String(100), nullable=False)
    City = Column(String(100))
    EffectiveDate = Column(Date)
    EndDate = Column(Date) 
    IsActive = Column(Boolean)

    
class DimDepartment(Base):
    __tablename__ = "DimDepartment"

    DeptID = Column(Integer, primary_key=True, autoincrement=True)
    DepartmentName = Column(String(100), nullable=False)

class DimDate(Base):
    __tablename__ = "DimDate"

    DateID = Column(Integer, primary_key=True, autoincrement=True)
    FullDate = Column(Date, nullable=False)
    Month = Column(Integer)
    Year = Column(Integer)

