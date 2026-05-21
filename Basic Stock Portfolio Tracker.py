# 1. Define a hardcoded dictionary of stock prices
stock_prices = {
    "GOLD": 160000,
    "SILVER": 270000,
    "BANKNIFTY": 53153,  # <-- Fixed typo from BNAKNIFTY to BANKNIFTY
    "TATA": 2324
}

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", list(stock_prices.keys()))

# 2. Get input from the user
# .strip() automatically removes any accidental extra spaces typed by the user
stock_name = input("Enter the stock name you own (e.g., GOLD): ").upper().strip()
quantity = int(input("Enter the quantity of shares you own: "))

# 3. Calculate total investment
if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_value = quantity * price
    
    output_text = f"Stock: {stock_name} | Quantity: {quantity} | Price: ₹{price} | Total Investment Value: ₹{total_value}"
    print("\n" + output_text)
    
    # 4. Save result to a text file natively on Windows
    # Added encoding="utf-8" to fix the UnicodeEncodeError caused by the ₹ symbol
    with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
        file.write(output_text)
    print("💾 Saved successfully to 'portfolio_summary.txt'")
    
else:
    print("❌ Stock ticker not found in our directory.")