import sqlite3 as sq

def find_data_base():
    with sq.connect("DB.db") as con:
        cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS drivers(
    drivers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    power INTEGER,
    voltage_min INTEGER,
    voltage_max INTEGER,
    current INTEGER,
    protection INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS components(
    components_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS orders(
    orders_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    order_date INTEGER,
    deadline INTEGER
    )""")
    #возможно дедлайн сделать строковым типом, а не числовым

    cur.execute("""CREATE TABLE IF NOT EXISTS components_drivers(
    components_drivers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    drivers_id INTEGER,
    components_id INTEGER,
    count INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS drivers_orders(
    drivers_orders_id INTEGER PRIMARY KEY AUTOINCREMENT,
    orders_id INTEGER,
    drivers_id INTEGER,
    count INTEGER
    )""")