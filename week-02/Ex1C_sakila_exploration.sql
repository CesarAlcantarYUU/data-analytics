/*
a)The information that is included is actor_id,
first_name, last_name, and last_update
b) The information that is included is film_id,
title, description, release_year, language_id,
original_language_id, rental_duration, rental_rate,
length, replacement_cost, rating, special_features,
and last_update
c) inventory, film_text, film_category, and film_actor
d) The table includes fields of "rental_id", "rental_date", 
"inventory_id", "customer_id", "return_date", "staff_id",
and "last_update. I would say since it has a filter option
it is easy to read because there's about 1001 records which
is a lot of information and without the filter option it 
would be hard to read. 
e) The inventory table includes fields of inventory_id, film_id,
store_id, and last_update. I would say this is hard to read
because I don't get how the fields correlate with eachother.
f) The only tables you need are the rental, film, and inventory tables.
The film table has the film titles, the rental table has the rental date,
and inventory table has the film_id to connect to the film table.
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;
