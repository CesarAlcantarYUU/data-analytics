USE northwind;
-- What is the product name(s) of the most expensive products?
SELECT ProductName
FROM products
WHERE UnitPrice = (
	SELECT MAX(UnitPrice)
    FROM products
);

-- What is the product name(s) and categories of the least expensive products?
SELECT p.ProductName, c.CategoryName
FROM products p
INNER JOIN categories c
ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = (
	SELECT MIN(UnitPrice)
    FROM products
);

-- What is the order id, shipping name and shipping address of all orders shipped via
-- "Federal Shipping"?
SELECT OrderID, ShipName, ShipAddress
FROM orders
WHERE ShipVia = (
	SELECT ShipperID
    FROM shippers
    WHERE CompanyName = 'Federal Shipping'
);

-- What are the order ids of the orders that included "Sasquatch Ale"?
SELECT OrderID
FROM `order details`
WHERE ProductID = (
	SELECT ProductID
    FROM products
    WHERE ProductName = 'Sasquatch Ale'
);

-- What is the name of the employee that sold order 10266?
SELECT FirstName, LastName
FROM employees
WHERE EmployeeID = (
	SELECT EmployeeID
    FROM orders
    WHERE OrderID = 10266
);

-- What is the name of the customer that bought order 10266?
SELECT ContactName
FROM customers
WHERE CustomerID = (
	SELECT CustomerID
    FROM orders
    WHERE OrderID = 10266
);

