"""
-- 1. SELECT with JOIN, WHERE, GROUP BY, HAVING, and ORDER BY
SELECT 
    c.CustomerID,
    c.Name AS CustomerName,
    COUNT(o.OrderID) AS TotalOrders,
    SUM(oi.Quantity * p.Price) AS TotalSpent
FROM 
    Customers c
JOIN 
    Orders o ON c.CustomerID = o.CustomerID
JOIN 
    OrderItems oi ON o.OrderID = oi.OrderID
JOIN 
    Products p ON oi.ProductID = p.ProductID
WHERE 
    o.OrderDate >= '2024-01-01'  -- Filter for recent orders
GROUP BY 
    c.CustomerID, c.Name
HAVING 
    TotalSpent > 500             -- Only include customers who spent more than $500
ORDER BY 
    TotalSpent DESC;             -- Order customers by total spending in descending order

-- 2. INSERT a new customer
INSERT INTO Customers (CustomerID, Name, Email)
VALUES (101, 'Jane Doe', 'jane.doe@example.com');

-- 3. UPDATE an order's status
UPDATE Orders
SET Status = 'Shipped', ShippingDate = NOW()
WHERE OrderID = 123;

-- 4. DELETE an order that was canceled
DELETE FROM Orders
WHERE OrderID = 456 AND Status = 'Canceled';
"""

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

# 1. SELECT with JOIN, WHERE, GROUP BY, HAVING, and ORDER BY
# Merge DataFrames (equivalent to SQL JOINs)
merged = (
    orders.merge(order_items, on="OrderID")
    .merge(products, on="ProductID")
    .merge(customers, on="CustomerID")
)

# Filter rows (equivalent to WHERE)
merged["OrderDate"] = pd.to_datetime(merged["OrderDate"])
filtered = merged[merged["OrderDate"] >= "2024-01-01"]

# Group by Customer and calculate aggregations
aggregated = (
    filtered.groupby(["CustomerID", "Name"])
    .agg(
        TotalOrders=("OrderID", "nunique"),  # Count unique orders
        TotalSpent=(
            "Quantity",
            lambda x: (x * filtered.loc[x.index, "Price"]).sum(),
        ),  # Calculate total spent
    )
    .reset_index()
)

# Filter aggregated data (equivalent to HAVING)
aggregated = aggregated[aggregated["TotalSpent"] > 500]

# Sort results (equivalent to ORDER BY)
result = aggregated.sort_values(by="TotalSpent", ascending=False)
print(result)

# 2. INSERT a New Customer
new_customer = {"CustomerID": 101, "Name": "Jane Doe", "Email": "jane.doe@example.com"}
customers = pd.concat([customers, pd.DataFrame([new_customer])], ignore_index=True)
print(customers)

# 3. UPDATE an Order's Status

orders.loc[orders["OrderID"] == 102, ["Status", "OrderDate"]] = [
    "Shipped",
    pd.Timestamp.now(),
]
print(orders)

# 4. DELETE an Order

orders = orders[~((orders["OrderID"] == 103) & (orders["Status"] == "Pending"))]
print(orders)
