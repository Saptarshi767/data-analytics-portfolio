import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Sample Amazon product URLs (replace with real ones for actual use)
PRODUCT_URLS = [
    "https://www.amazon.in/dp/B09V4MXBSN",  # Example: iPhone 13
    "https://www.amazon.in/dp/B0C9J8PVX5"   # Example: Samsung Galaxy S23
]


def get_product_info(url):
    """Scrape product title, price, and availability from an Amazon product page."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find(id="productTitle")
        title = title.get_text(strip=True) if title else "N/A"
        price = soup.find("span", {"class": "a-price-whole"})
        price = price.get_text(strip=True) if price else "N/A"
        availability = soup.find(id="availability")
        availability = availability.get_text(strip=True) if availability else "N/A"
        return {"url": url, "title": title, "price": price, "availability": availability}
    except Exception as e:
        return {"url": url, "title": "Error", "price": "Error", "availability": str(e)}


def main():
    results = []
    for url in PRODUCT_URLS:
        print(f"Scraping: {url}")
        info = get_product_info(url)
        print(info)
        results.append(info)
        time.sleep(2)  # Be polite to Amazon's servers
    df = pd.DataFrame(results)
    df.to_csv("amazon_price_sample.csv", index=False)
    print("\nResults saved to amazon_price_sample.csv")

if __name__ == "__main__":
    main() 