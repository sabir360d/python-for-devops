import requests
import json

API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
SYMBOL = "NVDA"

API_URL = (
    f"https://www.alphavantage.co/query"
    f"?function=GLOBAL_QUOTE&symbol={SYMBOL}&apikey={API_KEY}"
)

OUTPUT_FILE = "nvda_stock_price.json"


def fetch_stock_data(url):
    # Fetch stock price data from API
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def process_stock_data(data):
    # Extract meaningful stock information
    quote = data.get("Global Quote", {})

    processed = {
        "symbol": quote.get("01. symbol", "N/A"),
        "price": quote.get("05. price", "N/A"),
        "open": quote.get("02. open", "N/A"),
        "high": quote.get("03. high", "N/A"),
        "low": quote.get("04. low", "N/A"),
        "volume": quote.get("06. volume", "N/A"),
    }

    return processed


def save_to_json_file(data, filename):
    # Save processed stock data to JSON file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def main():
    raw_data = fetch_stock_data(API_URL)
    processed_stock = process_stock_data(raw_data)

    # Print to terminal
    print(f"Stock Price for {processed_stock['symbol']}:\n")
    for key, value in processed_stock.items():
        print(f"{key}: {value}")

    # Save to file
    save_to_json_file(processed_stock, OUTPUT_FILE)
    print(f"\nStock data saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
