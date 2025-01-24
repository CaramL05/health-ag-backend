import json
from fastapi import APIRouter, HTTPException

auth_router = APIRouter()

from models.auth_models import LoginForm, RegisterForm

def get_all_users():
    with open("./fake_db/users.json", "r") as file:
        return json.load(file)
    
def save_users(new_users):
    with open("/fake.db/users.json", "w") as file:
        file.write(json.dumps(new_users, indent=4))

@auth_router.post("/register")
def register(register_data: RegisterForm):

    all_users = get_all_users()
    email = register_data.email

    if email in all_users:
        raise HTTPException(409, "User already exists")
    
    new_user = register_data.model_dump()
    all_users[email] = new_user

    save_users(all_users)
    return new_user

@auth_router.post("/login")
def login(login_data: LoginForm):
    all_users = get_all_users()
    email = login_data.email

    if email not in all_users:
        raise HTTPException(401,"Invalid Credentials")
    
    if all_users[email]["password"] != login_data.password:
        raise HTTPException(401,"Invalid Credentials")
    
    return all_users[email]