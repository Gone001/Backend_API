from typing import Annotated

from fastapi import FastAPI, Header
from pydantic important BaseModel 

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}

@app.get("/profile")
async def profile(
    authorization: Annotated[str | None, Header()] = None
):
    return {"authorization": authorization}

#Header using Basemodel class 

'''class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []
    
@app.get("/item/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers
'''
# configuration with extra formbid data 
class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers
