import sqlite3 as sq


def find_data_base():
    with sq.connect("DB.db") as con:
        cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS driver(
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    power INTEGER,
    voltage_min INTEGER,
    voltage_max INTEGER,
    current INTEGER,
    protection INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS component(
    component_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS 'contract'(
    contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    contract_date TEXT,
    deadline TEXT
    )""")

    # возможно дедлайн сделать строковым типом, а не числовым

    cur.execute("""CREATE TABLE IF NOT EXISTS component_driver(
    component_driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_id INTEGER,
    component_id INTEGER,
    count INTEGER
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS driver_contract(
    driver_contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_id INTEGER,
    driver_id INTEGER,
    count INTEGER
    )""")
