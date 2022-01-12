from flask import jsonify
from app import app


@app.route('/')
@app.route('/index')
def index():
    stock_tickers = [
        {
            'name': 'AMZN',
            'price': '100',
        },
        {
            'name': 'APPL',
            'quantity': '250',
        },
        {
            'name': 'SHOP',
            'quantity': '200',
        },
        {
            'name': 'MSFT',
            'quantity': '75',
        }
    ]
    return jsonify(
        {
            'status': 'success',
            'shopping_list': stock_tickers
        }
    )