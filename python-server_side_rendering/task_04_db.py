from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def sql_source():
    try:
        conn = sqlite3.connect("products.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Products")
        data = cursor.fetchall()

        products = [dict(row) for row in data]

        return products
    except sqlite3.Error:
        return []

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def item():
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            items = data.get('items', [])
    except FileNotFoundError:
        items = []

    return render_template('items.html', items=items)


@app.route('/products')
def product():
    source = request.args.get("source")
    id = request.args.get("id")
    if source == 'json':
        with open("products.json", "r") as file:
            data = json.load(file)
    elif source == 'csv':
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
    elif source == 'sql':
        data = sql_source()
    else:
        return render_template('product_display.html', products=[],
                               wrong=True, no_id=False)

    if data:
        if id:
            products = []
            for product in data:
                if str(product.get("id")) == str(id):
                    products.append(product)
                    break
            if products == []:
                return render_template('product_display.html',
                                       products=products,
                                       wrong=False, no_id=True)
        else:
            products = data

    return render_template('product_display.html',
                           products=products,
                           wrong=False, no_id=False)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
