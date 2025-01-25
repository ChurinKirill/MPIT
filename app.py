from flask import Flask
from flask import render_template
from db_api import Database

app = Flask('НейМакет')
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
    
    products = get_products()
    
    return [current_user, products]





app.run(debug=True)