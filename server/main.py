from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# pip install "uvicorn[standard]"

from pydantic import BaseModel
from typing import Union

import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_ID = "2e976171-72d2-453b-af21-a56106691a0a"
PRIVATE_KEY = "226d2dd1-dee9-4896-907b-4a0b7e5aa665"

class User(BaseModel):
    username: str
    secret: str
    email: Union[str, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None

@app.post('/login/')
async def root(user: User):
    response = requests.get('https://api.chatengine.io/users/me/', 
        headers={ 
            "Project-ID": PROJECT_ID,
            "User-Name": user.username,
            "User-Secret": user.secret
        }
    )
    return response.json()

@app.post('/signup/')
async def root(user: User):
    response = requests.post('https://api.chatengine.io/users/', 
        data={
            "username": user.username,
            "secret": user.secret,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
        headers={ "Private-Key": PRIVATE_KEY }
    )
    return response.json()

# python3 -m venv venv
# source venv/bin/activate
# pip install --upgrade pip
# pip install -r requirements.txt
# uvicorn main:app --reload --port 3001
