
#stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such
# as pe ratio and price to book ratio. These are calculated as

with open("stocks.csv", "r") as f, open("output.csv","w") as out:
    out.write("Company name, PE Ratio, PB Ratio\n")
    next(f)
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        Eps = float(tokens[2])
        bookvalue = float(tokens[3])
        pe = round(price / Eps, 2)
        pb = round(price / bookvalue, 2)
        out.write(f"{stock},{pe},{pb}\n")
