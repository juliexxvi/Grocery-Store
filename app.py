from unittest import result
from flask import Flask, make_response, request, redirect, render_template, session
import psycopg2
# from hash import hash, check
from functools import wraps

app = Flask(__name__)
app.secret_key = b'b0af2307-0335-442c-acb1-8ac4639ab9ec'
conn = psycopg2.connect('dbname=grocery_store')
cur = conn.cursor()


@app.route('/')
def index():
    current_page = request.args.get('page')  # http://127.0.0.1:5000/?page=1
    if current_page is None:
        current_page = 1
    cur.execute("""SELECT count(*) FROM products""")
    results = cur.fetchall()
    page_count = int(results[0][0] / 36)
    offset = (int(current_page) - 1) * 36
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

    return render_template(('index.html'), products=products, page_count=page_count, current_page=current_page)


@app.route('/check-out', methods=['GET', 'POST'])
def check_out():
    if request.method == 'GET':
        return render_template('check-out.html')
    # if request.method == 'POST':


@app.route('/add-to-cart-action', methods=['POST'])
def add_to_cart_action():
    current_page = request.args.get('page')
    product_id = request.args.get('product-id')
    total_quantity = session.get('total_quantity')
    quantity = int(request.form.get('quantity'))
    if total_quantity is None:
        session['total_quantity'] = quantity
        if quantity != 0:
            session['cart'] = [{
                'id': product_id,
                'quantity': quantity
            }]
        else:
            session['cart'] = []
    else:
        arr = session.get('cart')
        session['total_quantity'] = int(
            session['total_quantity']) + quantity
        if quantity != 0:
            arr.append({
                'id': product_id,
                'quantity': quantity
            })
        session['cart'] = arr
    print(session.get('cart'))
    return redirect(f'/?page={current_page}')


if __name__ == '__main__':
    app.run(debug=True)
