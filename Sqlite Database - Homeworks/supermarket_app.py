#supermarket application

from supermarket import *

print("""
************************************
Welcome to the Supermarket

Operations;

1.Show Products

2.Find Product

3.Add Product

4.Delete Product

5.Make Discount

6.Make Raise

7.Add Stock

q for exit
************************************
""")

supermarket = Supermarket()

while True:

    operation = input("Operation: ")

    if operation == "q":

        print("Farewell...")

        #if the operation is 'q', end the program
        break

    elif operation == "1":

        print("Please wait...")
        time.sleep(2)

        supermarket.show_products()

    elif operation == "2":

        name = input("Product Name: ")

        print("Please wait...")
        time.sleep(2)

        supermarket.find_product(name)

    elif operation == "3":

        name = input("Product Name: ")
        category = input("Category: ")
        stock = int(input("Stock: "))
        price = float(input("Price: "))

        #define the new product object by using inputs
        new_product = Product(name,category,stock,price)

        print("Please wait...")
        time.sleep(2)

        supermarket.add_product(new_product)
        print("The product is added...")

    elif operation == "4":

        name = input("Product Name: ")

        answer = input("Are you sure(Y/N): ")

        if answer == "Y":

            print("Please wait...")
            time.sleep(2)

            supermarket.delete_product(name)
            print("The product is deleted...")

    elif operation == "5":

        name = input("Product Name: ")
        amount = float(input("Amount: "))

        print("Please wait...")
        time.sleep(2)

        supermarket.make_discount(name,amount)
        print("Done...")

    elif operation == "6":

        name = input("Product Name: ")
        amount = float(input("Amount"))

        print("Please wait...")
        time.sleep(2)

        supermarket.make_raise(name,amount)
        print("Done...")

    elif operation == "7":

        name = input("Product name: ")
        amount = float(input("Amount: "))

        print("Please wait...")
        time.sleep(2)

        supermarket.add_stock(name,amount)
        print("Done...")

    else:

        print("Invalid operation...")

