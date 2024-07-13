from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad User
class User(BaseModel):
    name: str
    lastname: str
    url: str
    age: int


users_list = [User(name="John", lastname="Marin", url="https://www.google.com", age=25),
            User(name="Ana", lastname="Perez", url="https://www.facebook.com", age=30),
            User(name="Juan", lastname="Sanchez", url="https://www.twitter.com", age=40)]


@app.get("/usersjson")
async def usersJson():
    return users_list

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)