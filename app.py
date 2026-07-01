from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

inventory ={}

@app.route("inventory")
def get_invetory():
    return jsonify(inventory)
@app.route("inventory/<int:id>", methods = ["GET"])
def get_inventory_by_id(id):
    item = inventory.get(id)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Could not find Item"}), 404

@app.route("inventory", methods = ["POST"])
def add_invetory():
    data = request.get_json()
    

@app.route("inventory/<int:id>", methods = ["PATCH"])
def update_inventory(id):
    pass

@app.route("inventory/<int:id>", methods = ["DELETE"])
def delete_inventory(id):
    pass

if __name__ == ("__main__"):
    app.run(debug=True)
