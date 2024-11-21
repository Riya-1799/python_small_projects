import statistics

# Dictionary to store stock data
stocks = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}

def print_all():
    """
    Prints all stocks with their prices and average price.
    """
    for stock, price in stocks.items():
        # Ensure the values are a list of numbers
        if not isinstance(price, list) or not all(isinstance(p, (int, float)) for p in price):
            print(f"Error: Stock '{stock}' contains invalid data.")
            continue

        avg = statistics.mean(price)
        print(f"{stock} ==> {price} ==> avg: {round(avg, 2)}")

def add():
    """
    Adds a new stock or updates an existing stock with new prices.
    """
    stock = input("Enter the stock name: ").strip()
    price = input("Enter the price of the stock (comma-separated for multiple prices): ").strip()

    # Split prices, remove whitespace, and convert to floats
    try:
        prices = [float(p.strip()) for p in price.split(',')]
    except ValueError:
        print("Invalid price input. Please enter numeric values separated by commas.")
        return

    # Add or update stock data
    if stock in stocks:
        stocks[stock].extend(prices)
    else:
        stocks[stock] = prices

    print_all()

def main():
    """
    Main function to handle user operations.
    """
    op = input("Enter the operation you want to perform (add/displayall): ").lower()
    if op == "add":
        add()
    elif op == "displayall":
        print_all()
    else:
        print("Invalid input, please choose from the options.")

if __name__ == "__main__":
    main()
