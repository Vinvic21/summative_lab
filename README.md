# Admin Portal Inventory

This project is a simple inventory management system built with Python and Flask. It provides a REST API for managing inventory items and a small command-line interface for interacting with the API.

## Features

- View all inventory items
- View a single inventory item by barcode
- Add a new item to the inventory by scanning a product barcode
- Update an item’s price or stock level
- Delete an item from the inventory
- Fetch product metadata from the Open Food Facts API

## Project Files

- app.py: Flask API endpoints for inventory operations
- cli.py: Command-line interface for testing the API
- inventory.py: In-memory inventory data store
- test.py: Basic API tests using pytest and requests

## Requirements

Install the required Python packages:

```bash
pip install flask requests pytest
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## Using the CLI

Run the command-line client in a separate terminal:

```bash
python cli.py
```

You can use the CLI to view, add, update, and delete inventory items.

## API Endpoints

- GET /inventory - View all inventory items
- GET /inventory/<id> - View one inventory item
- POST /inventory - Add an item using a barcode
- PATCH /inventory/<id> - Update an item
- DELETE /inventory/<id> - Delete an item

## Running Tests

```bash
pytest -q
```

## Notes

The inventory data is currently stored in memory, so changes will be lost when the server restarts.
