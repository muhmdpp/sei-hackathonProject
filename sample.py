import yfinance as yf
import matplotlib.pyplot as plt

# Choose a stock ticker, e.g., Apple (AAPL)
ticker = yf.Ticker("AAPL")

# Fetch 1 year of daily data
data = ticker.history(period="1y", interval="1d")

# Display the first few rows
print(data.head())


data['Close'].plot(title="AAPL Closing Price - Last 1 Year")
plt.show()
