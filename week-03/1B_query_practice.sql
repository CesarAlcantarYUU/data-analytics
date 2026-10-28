USE northwind;
SELECT *
FROM products
WHERE UnitPrice <= 7.50;

SELECT *
FROM products
WHERE UnitsInStock = 0
	AND UnitsOnOrder > 0;

SELECT ProductName, CategoryID
FROM northwind.products;

SELECT *
FROM northwind.categories;

SELECT p.ProductName
FROM northwind.products AS p
JOIN northwind.categories AS c
	ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood';

-- You know what supplier each product comes from because of the SupplierID on the products column.
SELECT ProductName, SupplierID
FROM northwind.products;

SELECT *
FROM northwind.suppliers;

SELECT SupplierID, CompanyName
FROM northwind.suppliers
WHERE CompanyName = 'Tokyo Traders';

SELECT ProductName
FROM northwind.products
WHERE SupplierID = (
	SELECT SupplierID
    FROM northwind.suppliers
    WHERE CompanyName = 'Tokyo Traders'
);

SELECT COUNT(*) AS TotalEmployees
FROM northwind.employees;

SELECT FirstName, LastName, Title
FROM northwind.employees
WHERE Title LIKE '%manager%';