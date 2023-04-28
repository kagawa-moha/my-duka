from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

try:
    conn = psycopg2.connect("dbname='myduka' user='postgres' host='localhost' password='12345678'")
    print("Database Connected Successfully")
except Exception as e:
    print("I am unable to connect to the database",e)

@app.route("/save-products")
def save_products():
    pass


@app.route('/')
def home():
     return render_template('index.html')

@app.route('/products')
def products():
    cur = conn.cursor()
    cur.execute("""SELECT *  from products;""")
    products = cur.fetchall()
    return render_template('products.html', products=products)

app.run()
