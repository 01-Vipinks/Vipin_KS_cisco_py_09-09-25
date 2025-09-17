"""
Web scraper module for Banking Management System.

Contains function to scrape interest rates from paginated webpages.
"""

import requests
from bs4 import BeautifulSoup

def scrape_interest_rates(base_url, pages=1):
    """
    Scrape interest rates from given base_url over multiple pages.

    Args:
        base_url (str): Base URL of the interest rates page.
        pages (int): Number of pages to scrape.

    Returns:
        list: List of dicts with product, rate, tenure.
    """
    all_rates = []
    for page in range(1, pages + 1):
        url = f"{base_url}/page/{page}/"
        response = requests.get(url, timeout=10)  # added timeout to avoid hanging
        if response.status_code != 200:
            continue
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", id="interest-rates")
        if not table:
            continue
        rows = table.find_all("tr")[1:]  # skip header
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 3:
                product = cols[0].get_text(strip=True)
                rate = cols[1].get_text(strip=True)
                tenure = cols[2].get_text(strip=True)
                all_rates.append({
                    "product": product,
                    "rate": rate,
                    "tenure": tenure
                })
    return all_rates
