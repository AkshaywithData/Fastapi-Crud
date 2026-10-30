# Expense Data Warehouse API

## Project Overview
The Expense Data Warehouse API is a REST API built using FastAPI and SQLAlchemy to interact with an expense data warehouse stored in MySQL.

The API provides endpoints to retrieve expense records, manage employee records, and retrieve expenses using pagination. It demonstrates how Python applications can expose database operations through RESTful APIs.

## Technologies Used

- Python — application development
- FastAPI — REST API development
- SQLAlchemy — database interaction and ORM
- Pydantic — request validation and response serialization
- MySQL — relational database
- Uvicorn — ASGI server for running FastAPI

Expense-Data-Warehouse-API/
│
├── Fastapi_crude.py              
├── models.py            
├── schemas.py           
├── database.py         
├── config.py            
├── requirements.txt     
├── .env                 
├── .gitignore
├── LICENSE
└── README.md


## Database Models

The API uses the following tables from the Expense Data Warehouse:

- FactExpense — stores expense transactions.
- Dimemployee — stores employee details.
- DimDepartment — stores department information.
- DimDate — stores date dimension information.

## API Endpoints

The following table describes the available endpoints in the Expense Data Warehouse API.

| HTTP Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Check API status |
| `GET` | `/expenses` | Retrieve all expenses |
| `POST` | `/employees` | Create a new employee |
| `GET` | `/employees` | Retrieve all employees |
| `PUT` | `/employee/{empID}` | Update an existing employee |
| `DELETE` | `/employees/{emp_id}` | Delete an employee |
| `GET` | `/expensepagi` | Retrieve expenses with pagination |

## Installation and Setup

1. Clone the repository

git clone <your-repository-url>
cd Expense-Data-Warehouse-API

Replace <your-repository-url> with your GitHub repository URL.

2. Install dependencies

python -m pip install -r requirements.txt

3. Configure environment variables

Create a .env file in the project directory with your MySQL connection settings:

DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=Expense

4. Run the API

python -m uvicorn Fastapi_crude:app --reload

The command assumes your file contains app = FastAPI(...).

The API will be available at:

http://127.0.0.1:8000

## Key Learning Outcomes

- Creating REST APIs using FastAPI
- Implementing CRUD operations
- Connecting FastAPI to MySQL using SQLAlchemy
- Validating requests and serializing responses using Pydantic
- Managing database sessions using dependency injection
- Implementing pagination
- Testing endpoints through Swagger UI

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

**Akshay Gawand**

GitHub: @AkshaywithData  