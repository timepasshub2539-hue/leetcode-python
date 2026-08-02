from fastapi import FastAPI, Depends, HTTPException
from passlib.hash import bcrypt
import jwt, datetime

app = FastAPI()
SECRET = "change-me"

@app.post("/signup")
def signup(u: UserIn):
    return db.insert("users", {"email": u.email,
        "pw": bcrypt.hash(u.password)})

@app.post("/login")
def login(u: UserIn):
    row = db.get_user(u.email)
    if not row or not bcrypt.verify(u.password, row.pw):
        raise HTTPException(401, "bad credentials")
    return {"token": make_token(row.id)}

@app.post("/expenses")
def create_expense(exp: ExpenseIn, user=Depends(current_user)):
    return db.insert("expenses", {**exp.dict(), "user_id": user.id})

@app.get("/expenses")
def list_expenses(range: str = None, user=Depends(current_user)):
    return db.query_filtered(user.id, range)

@app.put("/expenses/{eid}")
def update_expense(eid: int, exp: ExpenseIn, user=Depends(current_user)):
    return db.update("expenses", eid, exp.dict(), owner=user.id)

@app.delete("/expenses/{eid}")
def delete_expense(eid: int, user=Depends(current_user)):
    return db.delete("expenses", eid, owner=user.id)
