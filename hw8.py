

import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)

    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_products(conn, product):
    try:
        sql = '''INSERT INTO products
        (product_tittle, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def update_product_quantity_id(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)

def update_product_price_id(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)        



def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Error:
        print(Error)

connection = create_connection("hw.db")

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_tittle VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.00,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print("Connected!")
    # select_all_products(connection)
    # create_table(connection, create_products_table)
    # create_products(connection, ("??????????", 140.00, 20))
    # create_products(connection, ("????????????????", 50.00, 30))
    # create_products(connection, ("??????????????", 110.00, 10))
    # create_products(connection, ("??????", 14.00, 12))
    # create_products(connection, ("????????", 25.00, 130))
    # create_products(connection, ("????????????", 45.00, 300))
    # create_products(connection, ("????????", 770.00, 35))
    # create_products(connection, ("??????????", 70.00, 15))
    # create_products(connection, ("????????", 10.00, 200))
    # create_products(connection, ("????????", 80.00, 150))
    # create_products(connection, ("??????????", 80.00, 100))
    # create_products(connection, ("????????", 110.00, 20))
    # create_products(connection, ("??????", 940.00, 10))
    # create_products(connection, ("??????????????", 340.00, 70))
    # create_products(connection, ("??????????", 100.00, 50))
   

    print("Done")        