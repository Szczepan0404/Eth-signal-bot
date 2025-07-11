import os
import time
import ccxt
import pandas as pd
import ta
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

exchange = ccxt.binance()

def get_eth_data():
    ohlcv = exchange.fetch_ohlcv('ETH/USDT', timeframe='15m', limit=100)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    return df

def analyze_and_notify():
    df = get_eth_data()
    rsi = df['rsi'].iloc[-1]

    if rsi < 30:
        message = f'📈 RSI = {rsi:.2f} — SYGNAŁ: LONG'
        send_telegram(message)
    elif rsi > 70:
        message = f'📉 RSI = {rsi:.2f} — SYGNAŁ: SHORT'
        send_telegram(message)
    else:
        print(f'RSI = {rsi:.2f} — brak sygnału')

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

if __name__ == '__main__':
    while True:
        analyze_and_notify()
        time.sleep(900)  # co 15 minut
