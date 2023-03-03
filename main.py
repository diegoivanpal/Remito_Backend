
from fastapi import FastAPI
from routers import remitos


app = FastAPI()

app.include_router(remitos.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}