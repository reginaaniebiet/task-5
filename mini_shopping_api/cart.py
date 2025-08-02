import json
import os
import math

CART_FILE = "cart.json"

def load_cart():
    if not os.path.exists(CART_FILE):
        return {}
    with open(CART_FILE, "r") as f:
        return json.load(f)

def save_cart(cart):
    with open(CART_FILE, "w") as f:
        json.dump(cart, f, indent=4)

def add_to_cart(product_id, qty, products):
    cart = load_cart()
    str_id = str(product_id)

    # Find product
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return {"error": "Product not found"}

    if str_id in cart:
        cart[str_id]["qty"] += qty
    else:
        cart[str_id] = {
            "name": product["name"],
            "price": product["price"],
            "qty": qty
        }

    save_cart(cart)
    return {"message": f"Added {qty} x {product['name']} to cart."}

def checkout_cart():
    cart = load_cart()
    if not cart:
        return {"message": "Cart is empty"}

    total = 0
    for item in cart.values():
        total += item["price"] * item["qty"]

# round up to 2 decimal places
    total = math.ceil(total * 100) / 100  
    return {
        "items": cart,
        "total_amount": total
    }
