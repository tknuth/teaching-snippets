# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import sqlite3
import random
import pandas as pd

conn = sqlite3.connect("./restaurant.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS meals")
cur.execute("DROP TABLE IF EXISTS orders")

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS meals
    (id INTEGER PRIMARY KEY, name TEXT, type TEXT, diet INTEGER, price INTEGER)
"""
)

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS orders
    (id INTEGER PRIMARY KEY, order_date TEXT, customer_id INTEGER, meal_id INTEGER)
"""
)

meals = [
    ("Penne Arrabiata", "main", 1, 1200),
    ("Pizza Margherita", "main", 1, 1500),
    ("Avocado Salad", "starter", 0, 900),
    ("Tomato Soup", "starter", 0, 700),
    ("Grilled Salmon", "main", 2, 2200),
    ("Chocolate Cake", "dessert", 0, 800),
    ("Vegetable Stir Fry", "main", 0, 1100),
    ("Lamb Curry", "main", 3, 2500),
    ("Mushroom Risotto", "main", 0, 1600),
    ("Quinoa Salad", "starter", 0, 950),
    ("Vegan Tacos", "main", 0, 1200),
    ("Vegan Burger", "main", 0, 1300),
    ("Beef Burger", "main", 3, 1300),
    ("Spaghetti Bolognese", "main", 3, 1400),
    ("French Onion Soup", "starter", 1, 800),
    ("BBQ Ribs", "main", 3, 2700),
    ("Fried Chicken", "main", 3, 1900),
    ("Seafood Paella", "main", 2, 2600),
    ("Pad Thai", "main", 3, 1350),
    ("Apple Pie", "dessert", 1, 700),
    ("Tiramisu", "dessert", 1, 900),
    ("Cheesecake", "dessert", 1, 850),
    ("Chocolate Milkshake", "dessert", 1, 650),
    ("Vegan Chocolate Milkshake", "dessert", 0, 650),
]

cur.executemany(
    "INSERT INTO meals (name, type, diet, price) VALUES (?, ?, ?, ?)",
    meals,
)

conn.commit()


def get_random_meal(meal_type, conn):
    df = pd.read_sql("SELECT * FROM meals", conn)
    return random.choice(df.query(f"type == '{meal_type}'").id.tolist())


def insert_meal(order_date, customer_id, meal_type, cur, conn):
    meal_id = get_random_meal(meal_type, conn)
    cur.execute(
        """INSERT INTO orders (customer_id, meal_id, order_date) VALUES (?, ?, ?)""",
        (customer_id, meal_id, order_date),
    )


n = 100
min_n = 50
sigma = 0.1 * n
order_dates = (
    pd.date_range("2024-02-01", "2024-02-29", freq="D").strftime("%Y-%m-%d").tolist()
)
customer_id = 0

for order_date in order_dates:
    m = max([min_n, int(random.normalvariate(mu=n, sigma=sigma))])

    for i in range(m):
        if random.random() > 0.5:
            insert_meal(order_date, customer_id, "starter", cur, conn)
        if random.random() > 0.9:
            insert_meal(order_date, customer_id, "main", cur, conn)
        if random.random() > 0.5:
            insert_meal(order_date, customer_id, "dessert", cur, conn)

        customer_id += 1

conn.commit()

cur.close()
conn.close()

# %%
conn = sqlite3.connect("./restaurant.db")
cur = conn.cursor()

cur.execute(
    """
    SELECT * FROM meals WHERE type = 'main' AND price > 1500
    """
)

for row in cur:
    print(row)

cur.close()
conn.close()

# %%
conn = sqlite3.connect("./restaurant.db")

df = pd.read_sql(
    """
    SELECT * FROM meals WHERE type = 'dessert'
    """,
    conn,
)

conn.close()

df

# %%
conn = sqlite3.connect("./restaurant.db")

# Bestellungen mit vegetarischen Gerichten
df = pd.read_sql(
    """
    SELECT order_date, customer_id, diet as meal_diet FROM orders
    LEFT JOIN meals ON orders.meal_id = meals.id
    GROUP BY customer_id
    HAVING MAX(meal_diet) < 2;
    """,
    conn,
)

conn.close()

df

# %%
conn = sqlite3.connect("./restaurant.db")

# Bestellungen mit weniger als 3 Gerichten
df = pd.read_sql(
    """
    SELECT order_date, customer_id, SUM(price) as total_price, COUNT(*) as number_of_dishes
    FROM orders
    LEFT JOIN meals ON orders.meal_id = meals.id
    GROUP BY customer_id
    HAVING COUNT(*) < 3
    ORDER BY total_price DESC;
    """,
    conn,
)

conn.close()

df
