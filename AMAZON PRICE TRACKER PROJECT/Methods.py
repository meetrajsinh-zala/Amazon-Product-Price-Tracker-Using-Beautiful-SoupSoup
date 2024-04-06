import sqlite3
import matplotlib.pyplot as plt
import base64
import io

def Filter_data(asin):
    conn = sqlite3.connect('amztracker.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT asin,title,price,rating,date FROM prices WHERE asin = ?''',([str(asin)]))
    row = cursor.fetchall()
    return row

def Filter_data_available_prod(asin):
    conn = sqlite3.connect('amztracker.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT DISTINCT asin,title FROM prices WHERE asin = ?''',([str(asin)]))
    row = cursor.fetchall()
    return row

def Get_All_Data():
    conn = sqlite3.connect('amztracker.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT asin,title,price,rating,date FROM prices''')
    row = cursor.fetchall()
    return row

def Get_All_Available_Product():
    conn = sqlite3.connect('amztracker.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT DISTINCT asin,title FROM prices''')
    row = cursor.fetchall()
    return row

def Get_Particular_Product(asin_clicked):
    conn = sqlite3.connect('amztracker.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM prices WHERE asin = ?''',([str(asin_clicked)]))
    row = cursor.fetchall()
    return row

def Get_All_Praticlar_Labels(asin_clicked):
    conn = sqlite3.connect('amztracker.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT date FROM prices WHERE asin = ?''',([str(asin_clicked)]))
    dates = cursor.fetchall()
    dates = [date[0] for date in dates]
    return dates

def Get_All_Praticlar_Prices(asin_clicked):
    conn = sqlite3.connect('amztracker.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT price FROM prices WHERE asin = ?''',([str(asin_clicked)]))
    prices = cursor.fetchall()
    prices = [price[0] for price in prices]
    return prices

def Chart_Generator(date,price):
    plt.figure(figsize=(15, 6))
    plt.plot(date, price)
    plt.xlabel('Dates')
    plt.ylabel('Price')
    plt.title('Price Graph')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    image_data = buffer.getvalue()
    image_data_b64 = base64.b64encode(image_data).decode('utf-8')
    return image_data_b64