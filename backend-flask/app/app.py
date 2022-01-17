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
            'text': 'AMZN',
            'price': '100',
        },
        {
            'text': 'APPL',
            'price': '250',
        },
        {
            'text': 'SHOP',
            'price': '200',
        },
        {
            'text': 'MSFT',
            'price': '75',
        },
        {
            'text': 'TSLA',
            'price': '750',
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
