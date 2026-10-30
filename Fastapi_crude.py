from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import FactExpense, Dimemployee
from schemas import ExpenseSchema, EmployeeSchema, EmployeeCreate

app = FastAPI(
    title = "Expense Data warehouse API",
    description = "API for the expense data warehouse",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {"message" : "Expense Data Warehouse is running"}

@app.get("/expenses", response_model=list[ExpenseSchema])
def get_expenses(db: Session = Depends(get_db)):

    expenses = db.query(FactExpense).all()

    return expenses

@app.post("/employees", response_model= EmployeeSchema)
def create_employee(employee: EmployeeCreate, db:Session = Depends(get_db)):
    new_employee = Dimemployee(
        EmployeeName = employee.EmployeeName,
        City = employee.City,
        EffectiveDate = employee.EffectiveDate,
        IsActive = employee.IsActive)

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

@app.get("/employees", response_model = list[EmployeeSchema])
def get_employees(db: Session = Depends(get_db)):

    employees = db.query(Dimemployee).all()

    return employees

@app.put("/employees/{empID}",response_model = EmployeeSchema)
def update_employee(empID: int,employee: EmployeeCreate, db: Session = Depends(get_db)):

    existingemployee = db.query(Dimemployee).filter(
        Dimemployee.employeeID == empID
    ).first()

    if not existingemployee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    existingemployee.EmployeeName = employee.EmployeeName
    existingemployee.City = employee.City
    existingemployee.EffectiveDate = employee.EffectiveDate
    existingemployee.IsActive = employee.IsActive


    db.commit()
    db.refresh(existingemployee)

    return existingemployee

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(Dimemployee).filter(Dimemployee.employeeID ==emp_id).first()

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    try:

        db.delete(employee)
        db.commit()
        return {"message": "Employee deleted successfully"}
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Could not delete employee"
        )


@app.get("/expensepagi", response_model= list[ExpenseSchema])
def get_expenses2(
    skip: int = 2,
    limit: int = 10,db: Session = Depends(get_db)):
    expensepagi = db.query(FactExpense).offset(skip).limit(limit).all()

    return expensepagi