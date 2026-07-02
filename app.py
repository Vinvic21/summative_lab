from flask import Flask, request, jsonify
from inventory import inventory
import requests

app = Flask(__name__)



def fetch_product(barcode):
    base_url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        if data.get("status")== 1:
            product = data["product"]
            return{
                "product_name": product.get("product_name"),
                "brands": product.get("brands"),
                "ingredients_text": product.get("ingredients_text"),
                "price": 0.0, 
                "stock": 0      
            }
    return None
            

@app.route("/inventory")
def get_invetory():
    return jsonify(inventory)
@app.route("/inventory/<id>", methods = ["GET"])
def get_inventory_by_id(id):
    item = inventory.get(id)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Could not find Item"}), 404

@app.route("/inventory", methods = ["POST"])
def add_invetory():
    data = request.get_json()
    barcode = data.get("barcode")
    product = fetch_product(barcode)
    if product:
        inventory[barcode] = product
        return jsonify({"message": "Product addded successfully"}),201
    else:
        return jsonify({"message": "product not found"}), 401

    

@app.route("/inventory/<id>", methods = ["PATCH"])
def update_inventory(id):
    if id not in inventory:
        return ("Item not found", 404)
    data = request.get_json()
    inventory[id].update(data)
    return jsonify(inventory[id])

@app.route("/inventory/<id>", methods = ["DELETE"])
def delete_inventory(id):
    if id not in inventory:
        return ("Item not found", 404)
    del inventory[id]
    return ("Item deleted", 204)

if __name__ == ("__main__"):
    app.run(debug=True)
