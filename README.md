# Binance Futures Trading CLI

A Python CLI tool to place MARKET and LIMIT orders on Binance Futures Testnet.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Error handling
- Logging support
- Secure API management using .env

---

## Setup Instructions

1. Clone the repository

git clone https://github.com/Yokeshkumar28/binance-futures-trading-bot.git
cd binance-futures-trading-bot

2. Create virtual environment

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Create .env file

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key

Note: Use Binance Futures Testnet API keys.

---

## How to Run

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

### LIMIT Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.003 --price 50000

---

## Assumptions

- Binance Futures Testnet is used.
- Minimum notional value must be >= 100 USDT.
- Valid API keys are required.
- BTCUSDT pair tested.

---

## Logs

Log files are stored in the logs directory.
