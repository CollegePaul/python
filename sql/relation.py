import sqlite3


def query(sql, data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        #Turn on the foreign keys so that it will check first before instering the productTypeID
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql, data)
        db.commit()

def insert_product_types_data(records):
    sql = "insert into ProductType(Description) values (?)"
    for record in records:
        query(sql, record)

def insert_product_data(records):
    sql = "insert into Product (Name, Price, ProductTypeID) values  (?,?,?)"
    for record in records:
        query(sql, record)


if __name__ == "__main__":
    #product_types = [("Coffee",),("Tea",),("Cold Drink",)]
    #insert_product_types_data(product_types)

    #products = [("Americano", 2.0, 1), ("Moicha",3.5,1),("Green Tea",1.25,2)]

    #the product below can't be insterted as the ProductTypeID of 5 does not exist.
    products = [("Cookie",1.15,5)]
    insert_product_data(products)