import sqlite3

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name, Price) values (?,?)"
        cursor.execute(sql, values)
        db.commit()


if __name__ == "__main__":
    product = ("Latte", 1.35)
    insert_data(product)
    product = ("Green Tea", 1.2)
    insert_data(product)
    product = ("Black Tea", 1.5)
    insert_data(product)