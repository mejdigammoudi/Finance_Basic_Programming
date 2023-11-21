# stock
ticker = "AAPL"
opening_price = 142.7
closing_price = 143.2
volume = 1200000
print(ticker, opening_price, closing_price, volume)

# currency exchange rate
Currency_pair = "EUR/USD"
Buying_rate = 1.1825
Selling_rate = 1.1830
print(Currency_pair, Buying_rate, Selling_rate)

# portfolio List 1
stocks = ["AAPL", "MSFT", "GOOGL"]
stocks.append("IBM")
print(stocks)

# portfolio List 2
stocks = ["TSLA", "AMZN", "FB"]
stocks. append("NVDA")
stocks. append("AMD")
print(stocks)

# stock Dictionary
stock_dic = {"ticker": "AAPL", "opening_price": 142.7, "closing_price": 143.2, "volume": 1200000}
print(stock_dic)

# bond Dictionary
stock_dic = {"Issuer": "DB", "Maturity Date": "Tomorrow", "Coupon Rate": 8.2, "Face Value": 100}
print(stock_dic)

# the daily returns
stock_prices = [105, 107, 104, 106, 103]
for i in range(1, len(stock_prices)):
    daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i-1]
print(daily_return)

# average return over the entire period
stock_prices = [105, 107, 104, 106, 103]
avg = 0
for i in range(1, len(stock_prices)):
    daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i-1]
    avg = daily_return + avg
print(avg / 5)

# number of years required for this investment to reach a value of 1000
principal = 500
rate = 0.07
years = 0
while principal < 1000:
    principal *= (1 + rate)
    years += 1
print(years)

# final value of the investment after those years
principal = 500
rate = 0.07
while principal < 1000:
    principal *= (1 + rate)
print(principal)

# whether to buy this bond or not
bond_yield = 3.8
if bond_yield > 4.0:
    print("Buy the bond.")
else:
    print("Do not buy the bond.")

# consider buying the bond if its yield is exactly 4
bond_yield = 3.8
if bond_yield >= 4.0:
    print("Buy the bond.")
else:
    print("Do not buy the bond.")

# the trading suggestion for this stock
pe_ratio = 17
if pe_ratio < 15:
    print("Buy the stock.")
elif pe_ratio > 25:
    print("Sell the stock.")
else:
    print("Hold the stock.")

# buying the stock if the P/E ratio is between 14 and 16, and selling if it’s between 23 and 27
pe_ratio = 17
if 14 <= pe_ratio <= 16:
    print("Buy the stock.")
elif 23 <= pe_ratio <= 27:
    print("Sell the stock.")
else:
    print("Hold the stock.")