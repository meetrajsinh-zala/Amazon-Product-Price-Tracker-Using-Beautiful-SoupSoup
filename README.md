# Amazon Product Price Tracker with Flask Web App (using SQLite3)

This project enhances the previous version by incorporating Flask to create a user-friendly web application for tracking Amazon product prices. It uses Beautiful Soup for web scraping and provides a web interface for managing tracked products and viewing price history. SQLite3 is utilized as a lightweight database to store product information and price history.

## Features
- **Track Prices:** Monitor prices of your desired Amazon products through an intuitive web interface.
- **Web Scraping:** Utilize Beautiful Soup to efficiently scrape product price data from Amazon.
- **Price History:** Access and view the historical price data of tracked products.
- **Database Storage:** Store product information and price history in an SQLite3 database.

## Prerequisites
- **Python 3:** [Download Python 3](https://www.python.org/downloads/)
- **Beautiful Soup 4:** Install via pip
  ```bash
  pip install beautifulsoup4
  pip install requests
  pip install Flask
  ```
  
## Setup Instructions

### Clone the Repository
Clone the project repository to your local machine.

```bash
git clone [URL]
```

### Install Dependencies
Navigate to the project directory and install the required Python packages.

```bash
cd amazon-product-price-tracker
pip install -r requirements.txt
```

### Run the Application
Start the Flask web application.

```bash
python app.py
```
