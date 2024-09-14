from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_order(order_id):
    conn = sqlite3.connect('happy_burguer.db')
    c = conn.cursor()
    c.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
    order = c.fetchone()
    conn.close()
    return order


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['GET'])
def order():
    order_id = request.args.get('order_id')
    order = get_order(order_id)
    return render_template('order.html', order=order)


if __name__ == '__main__':
    app.run(debug=True)
