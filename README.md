# CodeAlpha Web Scraping Project

## Project Overview

This project was completed as part of the CodeAlpha Data Analytics Internship. It demonstrates how to collect structured data from a website using Python web scraping libraries and save the extracted information in CSV format for further analysis.

The project scrapes book information from [Books to Scrape](https://books.toscrape.com/), a website designed for practising web scraping.

## Objectives

- Extract book information from web pages.
- Use Python to retrieve and parse HTML content.
- Store scraped data in a structured CSV file.
- Validate the dataset for missing values and duplicate records.
- Prepare the dataset for further data analysis.

## Tools and Technologies

- **Python** — programming language.
- **Requests** — retrieves web page content.
- **BeautifulSoup** — parses HTML and extracts information.
- **Pandas** — loads and validates the resulting dataset.
- **VS Code** — development environment.

## Data Collected

The scraper extracts the following fields:

| Column | Description |
|---|---|
| `title` | Title of the book |
| `price_text` | Price as displayed on the website |
| `price_gbp` | Numeric book price in pounds sterling |
| `rating` | Book rating |
| `availability` | Availability status |
| `product_url` | Link to the book's product page |

## Project Structure

```text
CodeAlpha_WebScraping/
├── scraper.py
├── validate_dataset.py
├── requirements.txt
├── books_data.csv
├── README.md
└── .gitignore
```

## Installation and Setup

1. Install Python.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Create and activate a virtual environment.

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

5. Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run the Project

Run the scraper to collect the book data:

```bash
python scraper.py
```

The extracted data is saved to `books_data.csv`.

Run the dataset validation script:

```bash
python validate_dataset.py
```

The validation script reports the dataset dimensions, column names, data types, missing values, duplicate rows, price statistics and rating distribution.

## Data Validation

The scraped dataset was checked for:

- Number of rows and columns.
- Data types and column names.
- Missing values.
- Duplicate records.
- Price statistics.
- Distribution of book ratings.
- Missing titles, prices and product URLs.


## Skills Demonstrated

- Web scraping
- HTML parsing
- Data collection
- CSV data handling
- Data validation and quality checks
- Python scripting

## Acknowledgements

- [Books to Scrape](https://books.toscrape.com/) — practice website used for this project.


**Author:** Timilehin Ogundele

**Project:** CodeAlpha Data Analytics Internship — Web Scraping Task