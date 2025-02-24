import requests
import random
import time

# CoinGecko API endpoint
API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Supported cryptocurrencies
CRYPTOS = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "dogecoin": "DOGE"
}

# Fetch real-time price from CoinGecko
def get_crypto_price(crypto_id):
    try:
        response = requests.get(API_URL, params={"ids": crypto_id, "vs_currencies": "usd"})
        data = response.json()
        return data[crypto_id]["usd"]
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

# Simulate price changes over days
def simulate_price(initial_price, days=7):
    prices = [initial_price]
    for _ in range(days - 1):
        # Random fluctuation between -10% and +15%
        change = random.uniform(-0.10, 0.15)
        new_price = prices[-1] * (1 + change)
        prices.append(max(new_price, 0))  # Price can't go below 0
    return prices

# Main simulation function
def run_simulation(crypto_id, investment):
    initial_price = get_crypto_price(crypto_id)
    if not initial_price:
        return
    
    print(f"\nStarting price of {CRYPTOS[crypto_id]}: ${initial_price:.2f}")
    print(f"Your investment: ${investment:.2f}")
    
    # Calculate initial coin amount
    coins = investment / initial_price
    
    # Simulate prices for 7 days
    price_history = simulate_price(initial_price)
    
    # Display daily results
    print("\nDay-by-day simulation:")
    for day, price in enumerate(price_history, 1):
        value = coins * price
        print(f"Day {day}: ${price:.2f} per {CRYPTOS[crypto_id]} | Portfolio: ${value:.2f}")
        time.sleep(1)  # Pause for dramatic effect
    
    # Final result
    final_value = coins * price_history[-1]
    profit = final_value - investment
    print(f"\nFinal portfolio value: ${final_value:.2f}")
    print(f"Profit/Loss: ${profit:.2f} ({(profit / investment * 100):.2f}%)")

# User input
print("Welcome to Crypto Price Simulator!")
print("Available cryptocurrencies:", ", ".join(CRYPTOS.values()))
crypto_choice = input("Choose a crypto (BTC, ETH, DOGE): ").upper()
investment = float(input("How much to invest (in USD)? "))

# Validate input and run
crypto_id = [k for k, v in CRYPTOS.items() if v == crypto_choice]
if crypto_id and investment > 0:
    run_simulation(crypto_id[0], investment)
else:
    print("Invalid input! Use BTC, ETH, or DOGE and a positive investment amount.")

# Example run:
# Welcome to Crypto Price Simulator!
# Available cryptocurrencies: BTC, ETH, DOGE
# Choose a crypto (BTC, ETH, DOGE): BTC
# How much to invest (in USD)? 1000
# Starting price of BTC: $50000.00
# Your investment: $1000.00
# Day-by-day simulation:
# Day 1: $50000.00 per BTC | Portfolio: $1000.00
# Day 2: $47500.00 per BTC | Portfolio: $950.00
# ...
# Final portfolio value: $1125.43
# Profit/Loss: $125.43 (12.54%)
