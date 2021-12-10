from fastapi import FastAPI, APIRouter
import requests
import json
import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()





origins = ["*"]






key = os.getenv("key")

app = FastAPI(
    title="Chefs Academy notification api", openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter()

class biodata(BaseModel):
    name: str
    phonenumber: int
    email: str
    address: str
    course: str





@api_router.get("/", status_code=200)
async def root():
    """
    Root Get
    """
    return {
        "msg": "chefsacademy notification api..."
    }

@api_router.get("/getchatid", status_code=200)
async def root_getid():
    
    test= requests.get(f"https://api.telegram.org/{key}/getUpdates")
    rf = json.loads(test.content)
    return (rf)

@api_router.post("/notify", status_code=200)
async def send_notification(details:biodata):
    _info =f"Name: {details.name} \nPhone number: {details.phonenumber} \nEmail: {details.email} \nAddress: {details.address} \nCourse: {details.course}"
    
    test= requests.get(f"https://api.telegram.org/{key}/sendMessage?chat_id=589503354&text={_info}")
    rf = json.loads(test.content)
    return (rf)




app.include_router(api_router)