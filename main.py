from flask import Flask
from monero.wallet import Wallet
import math

app = Flask(__name__)
#from app import routes
@app.route('/')
@app.route('/index')
def index():
    return 'Здарова всем!!!'

@app.route('/test')
def test():
     return 'Testing....'
    

app.run()


#w = Wallet(port=38083)
#w.balance()

