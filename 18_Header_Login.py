from fastapi import FastAPI,Body,Header,Response,HTTPException
from typing import Annotated
from pydantic import BaseModel
from uuid import uuid4

app=FastAPI()

data={"email":"dassg360@gmail.com","password":"Gopi@123"}
access_token={}

class standard(BaseModel):
    email:str
    password:str

@app.get("/login")
async def login_user(user:Annotated[standard,Body()],response:Response):
    if not user.email or not user.password:
        raise HTTPException(status_code=401,detail={"message":"Missing credentials"})
    if user.email==data["email"] and user.password==data["password"]:
        raise HTTPException(status_code=200,detail={"message":"login sucessfully"})
    else:
        raise HTTPException(status_code=401,detail={"Message":"Login failed"})

    token=str(uuid4())
    response.set_cookie(key="session_token",value=token)
    access_token[token]=data.email
    return{"message":"Cookie stored","Welcome":user.email}
@app.get("/profile")
async def profileinfo(
    authorization:Annotated[str|None,Header()]=None):
    if not authorization :
        raise HTTPException(status_code=401,detail={"message":"unauthorized"})
    if authorization not in access_token :
        raise HTTPException(status_code=401,detail={"message":"unauthorized"})
    if authorization==access_token.get(authorization):
        return{
            "message":"Profile",
            "email":access_token.get(authorization)
        }
        