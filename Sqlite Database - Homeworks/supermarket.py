import sqlite3
import time

class Product:

    def __init__(self,name,category,stock,price):

        self.name = name
        self.category = category
        self.stock = stock
        self.price = price

    def __str__(self):

        return "Product Name : {}\nCategory : {}\nStock : {}\nPrice : {}\n".format(self.name,self.category,self.stock,self.price)


class Supermarket:

    def __init__(self):

        self.connect()

    #connect to the database
    def connect(self):

        #define the database
        self.connection = sqlite3.connect("Supermarket.db")

        #define the cursor
        self.cursor = self.connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS products (Name TEXT,Category TEXT,Stock INT,Price FLOAT)"

        #execute the query
        self.cursor.execute(query)

        #commit changes
        self.connection.commit()

    #disconnect from the database
    def disconnect(self):

        self.connection.close()

    def show_products(self):

        query = "SELECT * FROM products"

        #execute the query
        self.cursor.execute(query)

        #define the list of all products
        products = self.cursor.fetchall()

        if len(products) == 0:

            print("There is no product in the supermarket...")

        else:

            for i in products:

                #create product object
                product = Product(i[0],i[1],i[2],i[3])
                print(product)

    def find_product(self,name):

        query = "SELECT * FROM products WHERE Name = ?"

        #define the query by using name
        self.cursor.execute(query,(name,))

        #define the list of the particular product
        products = self.cursor.fetchall()

        if len(products) == 0:

            print("There is no such product...")

        else:

            #create product object
            product = Product(products[0][0],products[0][1],products[0][2],products[0][3])
            print(product)

    def add_product(self,product):

        query = "INSERT INTO products VALUES(?,?,?,?)"

        #execute the query by using fields of product object
        self.cursor.execute(query,(product.name,product.category,product.stock,product.price))

        #commit changes
        self.connection.commit()

    def delete_product(self,name):

        query = "DELETE FROM products WHERE Name = ?"

        #execute the query by using name
        self.cursor.execute(query,(name,))

        #commit changes
        self.connection.commit()

    def make_discount(self,name,amount):

        query = "SELECT * FROM products WHERE Name = ?"

        #execute the query by using name
        self.cursor.execute(query,(name,))

        #define the list of the particular product
        products = self.cursor.fetchall()

        if len(products) == 0:

            print("There is no such product...")

        else:

            price = products[0][3]

            #substract the amount from the price
            price -= amount

            query2 = "UPDATE products SET Price = ? WHERE Name = ?"

            #execute the query2 by using price and name
            self.cursor.execute(query2,(price,name))

            #commit changes
            self.connection.commit()

    def make_raise(self,name,amount):

        query = "SELECT * FROM products WHERE Name = ?"

        #execute the query by using name
        self.cursor.execute(query,(name,))

        #define the list of the particular product
        products = self.cursor.fetchall()

        if len(products) == 0:

            print("There is no such product...")

        else:

            price = products[0][3]

            #add tha amount to the price
            price += amount

            query2 = "UPDATE products SET Price = ? WHERE Name = ?"

            #execute the query2 by using price and name
            self.cursor.execute(query2,(price,name))

            #commit changes
            self.connection.commit()

    def add_stock(self,name,amount):

        query = "SELECT * FROM products WHERE Name = ?"

        #execute the query by using name
        self.cursor.execute(query,(name,))

        #define the list of the particular product
        products = self.cursor.fetchall()

        if len(products) == 0:

            print("There is no such product...")

        else:

            stock = products[0][2]

            #add the amount to the stock
            stock += amount

            query2 = "UPDATE products SET Stock = ? WHERE Name = ?"

            #execute the query2 bu using stock and name
            self.cursor.execute(query2,(stock,name))

            #commit changes
            self.connection.commit()
