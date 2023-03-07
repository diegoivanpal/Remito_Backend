from fastapi import FastAPI, APIRouter
from routers import remitos,date

app = FastAPI()
app.include_router(remitos.router)
app.include_router(date.router)

@app.get("/")
async def root( ):    
    return {"message": "API de Remitos"}