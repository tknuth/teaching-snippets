-- Bestellungen mit vegetarischen Gerichten
SELECT order_date, customer_id, diet as meal_diet FROM orders
LEFT JOIN meals ON orders.meal_id = meals.id
GROUP BY customer_id
HAVING MAX(meal_diet) < 2;

-- Bestellungen mit weniger als 3 Gerichten
SELECT order_date, customer_id, SUM(price) as total_price, COUNT(*) as number_of_dishes
FROM orders
LEFT JOIN meals ON orders.meal_id = meals.id
GROUP BY customer_id
HAVING COUNT(*) < 3
ORDER BY total_price DESC;