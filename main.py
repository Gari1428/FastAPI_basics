from fastapi import FastAPI
app = FastAPI()


food_items = {
    'Indian': ["Samosa", "Aloo Puri"],
    'American': ["Hot dog", "Apple Pie"],
    'Italian' : ['Pasta','Pizza']
}

@app.get("/get_items/{cuisine}")
def get_items(cuisine):
    #Adding validation
    items = food_items.get(cuisine)
    if not items:
        return f"{cuisine} cuisine is not available"

    return food_items.get(cuisine)

@app.get("/")
def hello():
    return ("Hello","World")

@app.get("/hello/{name}")
def hello(name): 
    return f"Hello {name}"