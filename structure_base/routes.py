from fastapi import APIRouter, Depends, HTTPException, status, Request
router = APIRouter()

@router.post("/login")
def login_user():
    return {"message": "Login successful"}
