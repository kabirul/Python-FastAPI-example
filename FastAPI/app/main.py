from typing import Union
from fastapi import FastAPI
#from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from app.api.notes import create_note,update_note,read_note,read_all_notes,delete_note,delete
from app.api.ping import ping

from app.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI()

origins = [    
    "http://127.0.0.1:8000/",
    "http://localhost:8081",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()  

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

#app.include_router(ping.router)
#app.include_router(notes.router, prefix="/notes", tags=["notes"])

#class Item(BaseModel):
    #name: str
    #price: float
    #is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"This is first Python FastAPI Demo"}


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
    #return {"item_id": item_id, "q": q}

#@app.put("/items/{item_id}")
#def update_item(item_id: int, item: Item):
    #return {"item_name": item.name,"item_price":item.price, "item_id": item_id}
