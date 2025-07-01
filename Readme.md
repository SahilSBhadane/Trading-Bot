# 🧠 Binance Futures Testnet Trading Bot

A Python-based automated trading bot designed for the Binance Futures Testnet. The bot executes trades based on basic market logic using Binance's official API and supports real-time logging of all trading activity.

---

## 🚀 Features

- Connects to Binance Futures Testnet via API keys
- Places long/short orders based on customizable strategy logic
- Supports configurable leverage and margin type
- Logs real-time trade activity to `bot.log`
- Easy to set up and extend for advanced strategies

---

## 💠 Tech Stack

- **Language:** Python 3.11
- **Library:** `python-binance`
- **Platform:** Binance Futures (Testnet)
- **Logging:** Built-in Python `logging` module

---

## ⚙️ How It Works

1. Connects to the Binance Futures Testnet using your API key and secret.
2. Fetches the current price of the selected trading pair (e.g., BTC/USDT).
3. Based on a basic predefined logic (like price threshold or random execution), it places:
   - `BUY` orders (long)
   - `SELL` orders (short)
4. Trade activity is logged into `bot.log` for review and debugging.

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/binance-futures-trading-bot.git
cd binance-futures-trading-bot
pip install -r requirements.txt
```

---

## 🔑 API Setup

1. Create a Binance Testnet account: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Generate API Key and Secret
3. Paste your keys in `config.py` (or wherever you've stored them)

```python
API_KEY = 'your_api_key_here'
API_SECRET = 'your_api_secret_here'
```

---

## ▶️ Usage

```bash
python main.py
```

The bot will start and continuously check price data to make buy/sell decisions. Output will be saved in `bot.log`.

---

## 📁 Files Overview

```
🔽 main.py             # Main bot logic
🔽 config.py           # API keys and config
🔽 bot.log             # Trading activity logs
🔽 requirements.txt    # Python dependencies
🔽 README.md           # Project documentation
```

---

## ⚠️ Disclaimer

This bot is built for educational purposes and works **only** on Binance's **Futures Testnet**. **Do not** use it on live accounts without thorough testing and modification. Trading cryptocurrencies involves financial risk.

