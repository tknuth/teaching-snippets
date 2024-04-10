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

conn = sqlite3.connect("./restaurant.db")
cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS meals
"""
)

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS meals
    (id INTEGER PRIMARY KEY, name TEXT, type TEXT, diet INTEGER, price INTEGER)
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
    """
    INSERT INTO meals (name, type, diet, price) VALUES (?, ?, ?, ?)
""",
    meals,
)

conn.commit()

cur.close()
conn.close()

# %%
conn = sqlite3.connect("./restaurant.db")
cur = conn.cursor()

cur.execute("SELECT * FROM meals WHERE type = 'main' AND price > 1500")

for row in cur:
    print(row)

cur.close()
conn.close()

# %%
import pandas as pd

conn = sqlite3.connect("./restaurant.db")
df = pd.read_sql("SELECT * FROM meals WHERE type = 'dessert'", conn)
conn.close()
df

# %%
import random

conn = sqlite3.connect("./restaurant.db")
cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS orders
"""
)

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS orders
    (id INTEGER PRIMARY KEY, date TEXT, customer_id INTEGER, meal_id INTEGER)
"""
)


def insert_random_meal(date, customer_id, meal_ids, cur):
    meal_id = random.choice(meal_ids)
    cur.execute(
        """INSERT INTO orders (customer_id, meal_id, date) VALUES (?, ?, ?)""",
        (customer_id, meal_id, date),
    )


df_meals = pd.read_sql("SELECT * FROM meals", conn)
starter_ids = df_meals.query("type == 'starter'").id.tolist()
main_ids = df_meals.query("type == 'main'").id.tolist()
dessert_ids = df_meals.query("type == 'dessert'").id.tolist()

n = 100
dates = (
    pd.date_range("2024-02-01", "2024-02-29", freq="D").strftime("%Y-%m-%d").tolist()
)
customer_id = 0

for date in dates:
    m = max([50, int(random.normalvariate(mu=n, sigma=n * 0.1))])
    for i in range(m):
        has_starter = random.random() > 0.5
        has_dessert = random.random() > 0.5

        if has_starter:
            insert_random_meal(date, customer_id, starter_ids, cur)

        insert_random_meal(date, customer_id, main_ids, cur)

        if has_dessert:
            insert_random_meal(date, customer_id, dessert_ids, cur)

        customer_id += 1

conn.commit()

cur.close()
conn.close()

# %%
