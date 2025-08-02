from fastapi import FastAPI, HTTPException, Query
import json
import os

from cart import add_to_cart, checkout_cart

app = FastAPI()

PRODUCT_FILE = "products.json"

# Load product list
def load_products():
    if not os.path.exists(PRODUCT_FILE):
        return []
    with open(PRODUCT_FILE, "r") as f:
        return json.load(f)

@app.get("/products/")
def get_products():
    return load_products()

@app.post("/cart/add")
def add_product_to_cart(product_id: int = Query(...), qty: int = Query(1)):
    if qty < 1:
        raise HTTPException(status_code=400, detail="Quantity must be at least 1")
    products = load_products()
    result = add_to_cart(product_id, qty, products)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@app.get("/cart/checkout")
def checkout():
    return checkout_cart()
