import requests
from bs4 import BeautifulSoup
import json

def scrape_interest_rates(base_url, pages=3):
    all_rates = []

    for page in range(1, pages + 1):
        url = f"{base_url}/page/{page}/"
        print(f"Scraping {url} ...")

        response = requests.get(url)
        if response.status_code != 200:
            print(f" Failed to fetch {url}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # Example: Assuming interest rates are in a table with id="interest-rates"
        table = soup.find("table", id="interest-rates")
        if not table:
            print(f"Interest rates table not found on {url}")
            continue

        rows = table.find_all("tr")
        for row in rows[1:]:  # Skip table header row
            cols = row.find_all("td")
            if len(cols) < 3:
                continue
            product = cols.get_text(strip=True)
            rate = cols[1].get_text(strip=True)
            tenure = cols[2].get_text(strip=True)

            all_rates.append({
                "product": product,
                "rate": rate,
                "tenure": tenure
            })

    return all_rates

if __name__ == "__main__":
    base_url = "http://example-bank-website.com/interest-rates"
    rates = scrape_interest_rates(base_url, pages=3)

    with open("interest_rates.json", "w", encoding="utf-8") as f:
        json.dump(rates, f, ensure_ascii=False, indent=4)

    print(f"Scraping complete! Saved {len(rates)} interest rate records into interest_rates.json")
