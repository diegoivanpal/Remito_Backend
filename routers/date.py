from fastapi import APIRouter, HTTPException, status
from db.models.remito import Remito, Device,Date
from db.schemas.remito import remito_schema,remitos_schema
from db.client import db_client
from utils.util import to_dict, search_remito
from bson import ObjectId
from datetime import datetime
from middleware.verify_token import VerifyTokenRoute




router = APIRouter( prefix="/date",
                   tags=["date"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}, route_class=VerifyTokenRoute)

@router.post("/")
async def search_remito_by_dates(date : Date ) :
    try:
        remito = remitos_schema(db_client.remitos.find( { date: { "$gte" : date.date_strt ,"$lte" : date.date_end} }))
        return Remito(**remito)
    except:
        return {"error": "No se ha encontrado el remito"}  


   