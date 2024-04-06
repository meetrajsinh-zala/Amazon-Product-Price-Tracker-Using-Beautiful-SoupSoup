**Amazon Product Price Tracker with Flask Web App (using SQLite3)**

This project builds upon the previous version by incorporating Flask to create a user-friendly web application for tracking Amazon product prices. 
It utilizes Beautiful Soup for web scraping and provides a web interface for managing tracked products and viewing price history. 
SQLite3 is used as a lightweight database to store product information and price history.

**Features:**
        Track prices of your desired Amazon products through a web interface.
        Leverage Beautiful Soup for efficient web scraping.
        View price history of tracked products.
        Store product data and price history in a SQLite3 database.

**Prerequisites:**
              Python 3 (download from https://www.python.org/downloads/)
              Beautiful Soup 4 (pip install beautifulsoup4)
              Requests (pip install requests) (for making HTTP requests)
              Flask (pip install Flask)
              SQLite3 (typically included with Python)

**Clone the repository:**

Bash:
    git clone [ URL ]

**Install dependencies:**

Bash:
    cd amazon-product-price-tracker
    pip install -r requirements.txt

**Run the application:**

Bash:
    python app.py
