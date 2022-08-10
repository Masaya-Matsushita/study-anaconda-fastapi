from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = 1.0

class Data(BaseModel):
    shopInfo: ShopInfo
    items: List[Item]

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/countries/{country_name}")
def country(country_name: str, country_id: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_id": country_id
    }

@app.post("/item/")
def message(item: Item):
    return {"message": f"{item.name}は、税込価格{int(item.price*item.tax)}円です。"}

@app.post("/shop/")
def shop(data: Data):
    return {"data": data}
