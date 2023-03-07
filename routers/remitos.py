from fastapi import APIRouter, HTTPException, status
from db.models.remito import Remito, Device
from db.schemas.remito import remito_schema,remitos_schema
from db.client import db_client
from utils.util import to_dict, search_remito
from bson import ObjectId
from datetime import datetime,date
from middleware.verify_token import VerifyTokenRoute


router = APIRouter( prefix="/remitos",
                   tags=["remito"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}, route_class=VerifyTokenRoute)

@router.get("/")
async def fetch_remitos():
    return remitos_schema(db_client.remitos.find())

@router.get("/{id}")
async def fetch_remito(id: str):
    return search_remito("_id", ObjectId(id))

@router.post("/")
async def add_remito(remito: Remito):

    remito.date = str(date.today())
    remito.number = db_client.remitos.count_documents({}) + 1
    print(remito)    
    new_remito = to_dict(remito)
    print(new_remito)  
    id = db_client.remitos.insert_one(new_remito).inserted_id
    return str(id)

