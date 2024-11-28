import json

import pandas as pd

customers = pd.DataFrame(
    {
        "CustomerID": [1, 2],
        "Name": ["Alice Smith", "Bob Johnson"],
        "Email": ["alice@example.com", "bob@example.com"],
    }
)

orders = pd.DataFrame(
    {
        "OrderID": [101, 102, 103],
        "CustomerID": [1, 2, 1],
        "OrderDate": ["2024-01-15", "2024-02-01", "2024-01-20"],
        "Status": ["Pending", "Shipped", "Pending"],
    }
)

order_items = pd.DataFrame(
    {
        "OrderID": [101, 101, 102, 103, 103],
        "ProductID": [201, 202, 203, 201, 204],
        "Quantity": [2, 1, 1, 3, 1],
    }
)

products = pd.DataFrame(
    {
        "ProductID": [201, 202, 203, 204],
        "ProductName": ["Widget A", "Widget B", "Widget C", "Widget D"],
        "Price": [50.0, 30.0, 100.0, 20.0],
    }
)

data = {
    "customers": customers.to_dict(),
    "orders": orders.to_dict(),
    "order_items": order_items.to_dict(),
    "products": products.to_dict(),
}


with open("data.json", "w") as f:
    json.dump(data, f)
