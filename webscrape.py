import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

query = input("🔍 Enter a product to search on Amazon: ").strip()
search_url = f"https://www.amazon.de/s?k={query.replace(' ', '+')}"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

print("\n📡 Sending request to Amazon...\n")
response = requests.get(search_url, headers=headers)

if response.status_code != 200:
    print(f"❌ Failed to fetch page (Status Code: {response.status_code})")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all("div", {"data-component-type": "s-search-result"})

products = []

for item in results:

    title_elem = item.h2
    title = title_elem.text.strip() if title_elem else "N/A"

    if title_elem and title_elem.a and title_elem.a.get("href"):
        link = "https://www.amazon.de" + title_elem.a["href"]
    else:
        link = "N/A"

    price_elem = item.find("span", class_="a-offscreen")
    price = price_elem.text.strip() if price_elem else "N/A"

    rating_elem = item.find("span", class_="a-icon-alt")
    rating = rating_elem.text.strip() if rating_elem else "N/A"

    reviews_elem = item.find("span", {"class": "a-size-base"})
    reviews = reviews_elem.text.strip() if reviews_elem else "N/A"

    products.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Reviews": reviews,
        "Link": link
    })

folder_path = "/Users/aliabdeltawab/Documents/Web Scraping"
os.makedirs(folder_path, exist_ok=True)

filename = f"amazon_{query.replace(' ', '_')}.csv"
file_path = os.path.join(folder_path, filename)

df = pd.DataFrame(products)
df.to_csv(file_path, index=False)

print(f"✅ Scraped {len(products)} products and saved to:\n📁 {file_path}")
