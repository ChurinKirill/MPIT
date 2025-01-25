from flask import Flask
from flask import render_template
from db_api import Database

app = Flask('НейМакет', static_url_path='', static_folder='static')
db = Database()

current_user = {}

def update_score():
    scoreupd = db.get_user('TestUser')
    for k, v in scoreupd.items():
        current_user[k] = v 

def get_products():
    return db.get_products()

@app.route('/')
def start_market():
    userinfo = db.get_user('TestUser', 'gagagager')
    for k, v in userinfo.items():
        current_user[k] = v
    
    _products = get_products()
    print(_products)
    return render_template( 
        'market.html',
        vol=current_user['score'],
        products=_products
    )




app.run(debug=True)