from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# basic example stock data route
@app.route('/stocks', methods=['GET'])
def stocks():
    stocks_list = [
        {
            'company': 'AMZN',
            'price': '100',
            'sentiment': '57',
        },
        {
            'company': 'APPL',
            'price': '250',
            'sentiment': '33',
        },
        {
            'company': 'SHOP',
            'price': '200',
            'sentiment': '19',
        },
        {
            'company': 'MSFT',
            'price': '75',
            'sentiment': '95',
        },
        {
            'company': 'TSLA',
            'price': '750',
            'sentiment': '88',
        },
        {
            'company': 'GOOG',
            'price': '900',
            'sentiment': '72',
        },
        {
            'company': 'AMD',
            'price': '32',
            'sentiment': '99',
        },
        {
            'company': 'GME',
            'price': '122',
            'sentiment': '21',
        },
        {
            'company': 'NVDA',
            'price': '116',
            'sentiment': '80',
        },
        {
            'company': 'DIS',
            'price': '420',
            'sentiment': '51',
        }
    ]
    return jsonify(
        {
            'status': 'success',
            'stocks': stocks_list
        }
    )


if __name__ == '__main__':
    app.run()
