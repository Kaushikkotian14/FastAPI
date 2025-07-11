from fastapi import FastAPI
from routers import auth_router, user_router, expense_router, bank_router
 
app = FastAPI(
    title="Expense Tracker API",
    description="JWT-secured FastAPI backend for managing users, expenses, and bank accounts",
    version="1.0.0"
)
 

app.include_router(auth_router.router, tags=["Auth"])
app.include_router(user_router.router, tags=["User"])
app.include_router(bank_router.router, tags=["Bank"])
app.include_router(expense_router.router, tags=["Expense"])