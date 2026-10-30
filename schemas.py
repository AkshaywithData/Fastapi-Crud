from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional

class EmployeeSchema(BaseModel):

    employeeID: int
    EmployeeName: str
    City : Optional[str] = None
    EffectiveDate: Optional[date] = None
    EndDate: Optional[date] = None
    IsActive: Optional[bool] = None

    model_config = {
        "from_attributes": True
    }

class EmployeeCreate(BaseModel):
    EmployeeName: str
    City: Optional[str] = None
    EffectiveDate: Optional[date] = None
    IsActive: Optional[bool] = None
    
class DepartmentSchema(BaseModel):
    DeptID: int
    DepartmentName: str

    model_config = {
        "from_attributes": True
    }



class DateSchema(BaseModel):
    DateID: int
    FullDate: date
    Month: Optional[int] = None
    Year: Optional[int] = None
    model_config = {
        "from_attributes": True
    }

class ExpenseSchema(BaseModel):
    ExpenseID: int
    DateID: int
    employeeID: int
    DeptID: int
    ExpenseType: str
    Vendor: str
    PaymentMode: str
    Amount: Decimal

    model_config = {
        "from_attributes": True
    }