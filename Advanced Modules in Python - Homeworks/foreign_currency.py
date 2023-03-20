import requests
from bs4 import BeautifulSoup

#define an empty list for buy and sell values
buy_sell = list()

url = "https://kur.doviz.com/serbest-piyasa/"

#take the currency as an input
currency = input("Currency: ")

response = requests.get(url + currency)

html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

general_values = soup.find_all("div", {"class" : "text-xl font-semibold text-white"})
buy_sell_values = soup.find("div", {"class" : "text-md font-semibold text-white mt-4"})

#append just values that we want to the list
for value in buy_sell_values:

    value = value.text
    value = value.strip()
    value = value.replace(",",".")

    if len(value) > 1:

        buy_sell.append(value)

print("""
Welcome to the Foreign Currency Application

Operations;

1. Convert

2. Buy

3. Sell

q for exit
""")

while True:

    #take the operation as an input
    operation = input("Operation: ")
    operation = operation.upper()

    if operation == "Q":

        print("Farewell...")
        break

    elif operation == "CONVERT":

        for value in general_values:

            value = value.text
            value = value.replace(",",".")
            print("USD to TL:",value)

    elif operation == "BUY":

        amount = float(input("Amount: "))

        buy_sell[0] = float(buy_sell[0])

        result = amount * buy_sell[0]

        print("You need to pay {} TL...".format(result))

    elif operation == "SELL":

        amount = float(input("Amount: "))

        buy_sell[1] = float(buy_sell[1])

        result = amount / buy_sell[1]

        print("You will get {} TL...".format(result))

    else:

        print("Invalid operation...")


