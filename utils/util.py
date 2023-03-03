import json
from db.schemas.remito import remito_schema,remitos_schema
from db.models.remito import Remito, Device
from db.client import db_client


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

def search_remito(field: str, key):
    try:
        remito = remito_schema(db_client.remitos.find_one({field: key}))
        return Remito(**remito)
    except:
        return {"error": "No se ha encontrado el remito"}  