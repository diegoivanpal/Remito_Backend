import os
from fastapi import Request
from fastapi.responses import JSONResponse
from jose import jwt, JWTError, exceptions
from dotenv import load_dotenv
from fastapi.routing import APIRoute

load_dotenv(".env")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_DURATION= os.environ.get("ACCESS_TOKEN_DURATION")
SECRET = os.environ.get("SECRET")

def validate_token(token, output=False):
    try:
        if output:
            jwt.decode(token, SECRET, algorithms=ALGORITHM)
        jwt.decode(token, SECRET, algorithms=ALGORITHM)
        
    except exceptions.JWSSignatureError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)
    except exceptions.JWTError:
        return JSONResponse(content={"message": "Signature verification failed"}, status_code=401)
    

class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()

        async def verify_token_middleware(request:Request):
            token = request.headers["Authorization"].split(" ")[1]
            print(token)

            validation_response = validate_token(token, output=True)

            if validation_response == None:
                return await original_route(request)
            else:
                return validation_response
        return verify_token_middleware    
        


