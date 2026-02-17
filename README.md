## Binance Futures Trading CLI

A Python Command Line Interface (CLI) tool to place MARKET and LIMIT orders on Binance Futures Testnet.

This project demonstrates API integration, validation, structured logging, and clean CLI-based architecture.

## FEATURES

Place MARKET orders

Place LIMIT orders

Input validation

Proper error handling

Structured logging

Secure API management using .env

Modular and readable code structure

## TECH STACK

Python 3.x

Binance Futures API

python-binance

argparse

logging

python-dotenv

## SETUP INSTRUCTIONS

1. Clone the Repository

git clone https://github.com/Yokeshkumar28/binance-futures-trading-bot.git

cd binance-futures-trading-bot

2. Create Virtual Environment

python -m venv venv

## Activate environment:

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Create .env File

Create a .env file in the root directory and add:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key

Note: Use Binance Futures Testnet API keys only.

## HOW TO RUN

# MARKET Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

# LIMIT Order:

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.003 --price 50000

# VALIDATION & ERROR HANDLING

Validates order type

Ensures price is provided for LIMIT orders

Handles Binance API errors

Handles insufficient balance

Handles minimum notional requirement (>= 100 USDT)

## LOGGING

Logs are stored in the logs/ directory

Each order request and response is logged with timestamps

Errors are logged for debugging

## ASSUMPTIONS

Binance Futures Testnet is used

Minimum notional value must be >= 100 USDT

Sufficient USDT balance must be available

BTCUSDT trading pair tested

## PROJECT STRUCTURE

binance-futures-trading-bot/

cli.py
order_service.py
utils.py
config.py
logs/
.env
requirements.txt
README.md

## LEARNING OUTCOMES

Working with REST APIs

Command Line Interface development

Clean code structure

Exception handling

Logging best practices

Environment variable management

# Author
Yokesh Kumar Kuruva
