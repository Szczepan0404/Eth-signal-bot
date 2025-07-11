# ETH RSI Telegram Bot 📈📉

Bot, który analizuje rynek ETH/USDT na podstawie wskaźnika RSI i wysyła sygnały LONG/SHORT na Telegram.

## 🔧 Jak działa

- Dane z Binance (15-minutowe)
- RSI < 30 → SYGNAŁ: LONG
- RSI > 70 → SYGNAŁ: SHORT
- Powiadomienie co 15 minut (jeśli sygnał)

## 🚀 Jak uruchomić na Render

1. Zaloguj się do [Render.com](https://render.com)
2. Stwórz nowe **Web Service**
3. Połącz z repozytorium GitHub (z tym projektem)
4. Ustaw:

   - **Build Command:** *(zostaw puste)*
   - **Start Command:** `python main.py`
   - **Environment:**
     - `TELEGRAM_TOKEN=...` (z @BotFather)
     - `CHAT_ID=...` (Twój ID z getUpdates)

5. Wybierz plan **Free** i kliknij **Deploy**

Bot będzie działać 24/7 🎉
