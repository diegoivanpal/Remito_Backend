def remito_schema(remito) -> dict:
    return {"id": str(remito["_id"]),
            "number": remito["number"],
            "date": remito["date"],
            "from_workshop": remito["from_workshop"],
            "to_workshop":remito["to_workshop"],
            "user": remito["user"],
            "devices": remito["devices"]
            }

def remitos_schema(remitos) -> list:
    return [remito_schema(remito) for remito in remitos]

