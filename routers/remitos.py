from fastapi import APIRouter, HTTPException, status
from db.models.remito import Remito, Device

from db.schemas.remito import remito_schema,remitos_schema
from db.client import db_client

import json



router = APIRouter( prefix="/remitos",
                   tags=["remito"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

@router.get("/")
async def fetch_remitos():
    return remitos_schema(db_client.remitos.find())

@router.post("/")
async def add_remito(remito: Remito):
    
    new_remito = to_dict(remito)
    id = db_client.remitos.insert_one(new_remito).inserted_id
    return str(id)

