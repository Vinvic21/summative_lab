from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("inventory")
def get_invetory():
    pass
@app.route("inventory/<int:id>", methods = ["GET"])
def get_inventory_by_id(id):
    pass

@app.route("inventory", methods = ["POST"])
def add_invetory():
    pass

@app.route("inventory/<int:id>", methods = ["PATCH"])
def update_inventory(id):
    pass

@app.route("inventory/<int:id>", methods = ["DELETE"])
def delete_inventory(id):
    pass

if __name__ == ("__main__"):
    app.run(debug=True)
