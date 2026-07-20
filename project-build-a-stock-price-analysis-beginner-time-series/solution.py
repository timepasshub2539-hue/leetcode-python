import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT"]
data = yf.download(tickers, start="2022-01-01", end="2024-01-01")

close = data["Close"]
volume = data["Volume"]

close.plot(figsize=(10, 5), title="Closing Price"); plt.show()

weekly = close.resample("W").last()
monthly = close.resample("ME").last()

close["AAPL_MA20"] = close["AAPL"].rolling(20).mean()
close["AAPL_MA200"] = close["AAPL"].rolling(200).mean()
close[["AAPL","AAPL_MA20","AAPL_MA200"]].plot(figsize=(10,5)); plt.show()

volume.plot(figsize=(10, 5), title="Trading Volume"); plt.show()
