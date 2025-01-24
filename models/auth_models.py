from pydantic import BaseModel

class RegisterForm(BaseModel):
    fname: str
    lname: str
    email: str
    password: str

class LoginForm(BaseModel):
    email: str
    password: str