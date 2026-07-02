import pytest
import requests
import json

BASE_URL = "http://127.0.0.1:5000"
BARCODE = "5000159484695"

def test_add_product():
    response = requests.post(f"{BASE_URL}/inventory", json={"barcode": BARCODE})
    assert response.status_code == 201
    assert response.json()["message"] == "Product addded successfully"

def test_get_product():
    response = requests.get(f"{BASE_URL}/inventory/{BARCODE}")
    assert response.status_code == 200
    assert response.json()["product_name"] is not None

def test_patch_product():
    response = requests.patch(f"{BASE_URL}/inventory/{BARCODE}", json={"price": 4.99})
    assert response.status_code == 200
    assert response.json()["price"] == 4.99

def test_delete_product():
    response = requests.delete(f"{BASE_URL}/inventory/{BARCODE}")
    assert response.status_code == 204
