/*
a) The name of the table that holds the items Northwind Sells is "products".
b) "categories" table holds the types/categories of the items Northwind Sells. 
*/

USE northwind;
(Select *
From employees);

/*
a)Margaret last name is "Peacock" so it makes it look like shes a bird.
*/

USE northwind;
(Select *
From products);
/* 
a)The query returns 77 records. You can retrieve only 10 rows by changing the limit to only 10 rows. 
*/

USE northwind;
(Select *
From categories);
/* 
a) The category id of seafood is 8. 
*/

USE northwind;
(Select OrderID, OrderDate, ShipName, ShipCountry
From orders);
