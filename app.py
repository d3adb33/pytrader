from flask import Flask, render_template
from coinbaseapi import get_current_price

app = Flask(__name__)

@app.route('/')
def index():
    #return "Hello World - I am the PyTrader!"
    btc_usd_price = get_current_price("BTC-USD")
    #eth_usd_price = get_current_price('ETH-USD')
    return render_template('index.html', btc_price=btc_usd_price)

if __name__ == '__main__':
    app.run(debug=True)