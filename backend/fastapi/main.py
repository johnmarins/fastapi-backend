from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
        return {"Hello":"¡World!"}

@app.get("/curso")
async def read_root():
        return {"url_curso":"https://localhost:8000/python"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
