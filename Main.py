from Bot import BasicBot
import getpass

def main():
    print("🚀 Welcome to the Binance Futures Testnet Trading Bot")

    api_key = input("🔑 Enter your Binance API Key: ")
    api_secret = getpass.getpass("🔐 Enter your Binance API Secret (hidden): ")

    bot = BasicBot(api_key, api_secret)

    while True:
        try:
            order_type = input("\n📌 Order Type (market / limit): ").strip().lower()
            if order_type not in ["market", "limit"]:
                print("❌ Invalid order type.")
                continue

            side = input("📈 Order Side (buy / sell): ").strip().lower()
            if side not in ["buy", "sell"]:
                print("❌ Invalid side.")
                continue

            symbol = input("💱 Trading Symbol (e.g., BTCUSDT): ").strip().upper()
            quantity = float(input("🔢 Quantity: "))

            if order_type == "market":
                result = bot.place_market_order(symbol, side, quantity)
            elif order_type == "limit":
                price = float(input("💰 Limit Price: "))
                result = bot.place_limit_order(symbol, side, quantity, price)

            print(f"\n✅ Order Response:\n{result}")

            again = input("\n📦 Place another order? (y/n): ").strip().lower()
            if again != 'y':
                print("👋 Exiting bot. Check `bot.log` for details.")
                break

        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
