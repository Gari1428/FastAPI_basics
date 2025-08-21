from fastapi import FastAPI
from enum import Enum
app = FastAPI()

food_items = {
    "indian" :["Samosa","Aloo poori"],
    "american" :["Hot dog", "Apple Pie"],
    "italian" :['Pasta','Pizza']
}



class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"


@app.get("/get_cuisine/{cuisine}")
async def get_cuisine(cuisine: AvailableCuisines):
    items = food_items.get(cuisine)
    if not items:
        return f"{cuisine} cuisine is not available"

    return food_items.get(cuisine)

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_coupon(code: int):
    return {'discount_amount' : coupon_code.get(code)}