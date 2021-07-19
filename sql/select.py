import sqlite3

def select_all_products():
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        products = cursor.fetchall()
        return products

def select_all_products_ascending():
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product order by Name asc")
        products = cursor.fetchall()
        return products

def select_product(id):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select Name,Price from Product where ProductID=?", (id,))
        product = cursor.fetchone()
        return product


if __name__ == "__main__":
    products = select_all_products_ascending()
    print(products)

    product = select_product(3)
    print(product)
