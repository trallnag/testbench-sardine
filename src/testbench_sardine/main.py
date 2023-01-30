from typing import Union

from fastapi import FastAPI, HTTPException

from . import utils

app = FastAPI()


@app.get("/")
async def get_root():
    return {"message": "Hello World"}


@app.get("/pizza-size")
async def get_pizza_size(diameter: Union[int, float]):
    return {"area": utils.pizza_size(diameter)}


@app.get("/users/{username}/email")
async def get_users_username_email(username: str):
    if username == "foo":
        return {"username": username, "email": "foo@example.com"}
    elif username == "bar":
        return {"username": username, "email": "bar@example.com"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
