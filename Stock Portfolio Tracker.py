"""
Project: Stock Portfolio Tracker
Author: Lakshay Gupta

Description:
This program calculates the total investment value of a
user's stock portfolio using predefined stock prices.
It also saves the portfolio details to a text file.

Concepts Used:
- Dictionary
- Loops
- Input Validation
- File Handling
"""
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
    "NFLX": 420
}

portfolio = {}

print("=" * 55)
print("            STOCK PORTFOLIO TRACKER")
print("=" * 55)

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    try:
        number_of_stocks = int(input("\nHow many different stocks do you own? : "))

        if number_of_stocks > 0:
            break
        else:
            print("Please enter a number greater than 0.")

    except ValueError:
        print("Invalid input! Please enter a number.")

for i in range(number_of_stocks):

    print(f"\nStock {i + 1}")

    while True:
        stock_name = input("Enter Stock Name: ").upper()

        if stock_name in stock_prices:
            break
        else:
            print("Stock not available. Please choose from the list.")

    while True:
        try:
            quantity = int(input("Enter Quantity: "))

            if quantity >= 0:
                break
            else:
                print("Quantity cannot be negative.")

        except ValueError:
            print("Please enter a valid integer.")

    portfolio[stock_name] = quantity

print("\n")
print("=" * 55)
print("              PORTFOLIO SUMMARY")
print("=" * 55)

total_investment = 0

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(f"{stock:<10} {quantity:>3} shares x ${price:<4} = ${investment}")

print("-" * 55)
print(f"Total Investment Value = ${total_investment}")
print("=" * 55)

try:
    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 35 + "\n\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock:<10} {quantity} shares x ${price} = ${investment}\n"
            )

        file.write("\n")
        file.write(f"Total Investment = ${total_investment}")

    print("\nPortfolio has been saved to 'portfolio.txt'.")

except Exception as e:
    print("Error saving file:", e)

print("\nThank you for using Stock Portfolio Tracker!")