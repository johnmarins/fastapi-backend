from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad User
class User(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int


users_list = [User(id=1, name="John", lastname="Marin", url="https://www.google.com", age=25),
            User(id=2, name="Ana", lastname="Perez", url="https://www.facebook.com", age=30),
            User(id=3, name="Juan", lastname="Sanchez", url="https://www.twitter.com", age=40)]


@app.get("/usersjson")
async def usersJson():
    return users_list

#Path
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "User not found"}

#Query
@app.get("/userquery/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "User not found"}




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)