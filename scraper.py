"""
CodeAlpha Internship - Task 1: Web Scraping
Scrapes book information from https://books.toscrape.com/
and saves the results to books_data.csv.

Educational use: Books to Scrape is a practice website created for scraping.
"""

import csv
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "books_data.csv"
MAX_PAGES = 3  # Start with 3 pages. Increase later if needed.

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; CodeAlphaLearningScraper/1.0)"
}


def get_page(url):
    """Download a page and return its HTML, or None if a request fails."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        print(f"Could not retrieve {url}: {error}")
        return None


def extract_books(html, page_url):
    """Extract book details from one catalogue page."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for item in soup.select("article.product_pod"):
        title_element = item.select_one("h3 a")
        price_element = item.select_one(".price_color")
        availability_element = item.select_one(".availability")
        rating_element = item.select_one("p.star-rating")

        if title_element is None:
            continue

        title = title_element.get("title", "").strip()
        product_url = urljoin(page_url, title_element.get("href", ""))
        price_text = price_element.get_text(strip=True) if price_element else ""
        availability = (
            " ".join(availability_element.stripped_strings)
            if availability_element else "Unknown"
        )
        rating = (
            rating_element.get("class", [])[-1]
            if rating_element and len(rating_element.get("class", [])) > 1
            else "Unknown"
        )

        # Keep the original price text and also provide a numeric value for analysis.
        price_numeric = (
            price_text.replace("£", "").replace("Â", "").strip()
            if price_text else ""
        )
        try:
            price_numeric = float(price_numeric)
        except ValueError:
            price_numeric = ""

        books.append({
            "title": title,
            "price_text": price_text,
            "price_gbp": price_numeric,
            "rating": rating,
            "availability": availability,
            "product_url": product_url,
        })

    return books


def find_next_page(html, current_url):
    """Return the next catalogue page URL, or None when there is no next page."""
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")
    if next_link is None:
        return None
    return urljoin(current_url, next_link.get("href", ""))


def main():
    all_books = []
    current_url = BASE_URL
    pages_visited = 0

    while current_url and pages_visited < MAX_PAGES:
        print(f"Scraping page {pages_visited + 1}: {current_url}")
        html = get_page(current_url)
        if html is None:
            break

        page_books = extract_books(html, current_url)
        all_books.extend(page_books)
        pages_visited += 1

        current_url = find_next_page(html, current_url)
        if current_url and pages_visited < MAX_PAGES:
            time.sleep(1)  # Be polite: pause between requests.

    if not all_books:
        print("No books were collected. Check your internet connection and try again.")
        return

    fieldnames = [
        "title", "price_text", "price_gbp",
        "rating", "availability", "product_url"
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_books)

    print(f"\nFinished. Collected {len(all_books)} books from {pages_visited} page(s).")
    print(f"Dataset saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
