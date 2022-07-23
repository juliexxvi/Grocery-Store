from unittest import result
from flask import Flask, make_response, request, redirect, render_template, session
import psycopg2
# from hash import hash, check
from functools import wraps

app = Flask(__name__)
app.secret_key = b'b0af2307-0335-442c-acb1-8ac4639ab9ec'
conn = psycopg2.connect("dbname=grocery_store")
cur = conn.cursor()


@app.route('/')
def index():
    page = request.args.get('page')  # http://127.0.0.1:5000/?page=1
    if page is None:
        page = 1
    cur.execute("""SELECT count(*) FROM products""")
    results = cur.fetchall()
    page_count = int(results[0][0] / 36)
    offset = (int(page) - 1) * 36
    cur.execute("""SELECT * FROM products LIMIT 36 OFFSET %s""", [offset])
    results = cur.fetchall()
    products = []
    for row in results:
        products.append({
            "id": row[0],
            "name": row[1],
            "image_url": row[2],
            "price": row[3]/100,
            "brand": row[4],
            "store": row[5],
            "code": row[6],
            "cup_price": row[7],
            "package_size": row[8]
        })
    return render_template(('index.html'), products=products, page_count=page_count, page=page)


if __name__ == "__main__":
    app.run(debug=True)
