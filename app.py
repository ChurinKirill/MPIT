from flask import Flask
from flask import render_template
from flask import request
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
def log_reg():
    return render_template('registr.html', gnev_message='')

@app.route('/reg', methods=['POST'])
def reg():
    name = request.form['name_reg']
    tg = request.form['tg_reg']
    pwd = request.form['pwd_reg']

    res = db.add_user(name, tg, pwd)

    if res['ok']:
        current_user['is_adm'] = False
        current_user['name'] = name
        current_user['age'] = 0
        current_user['score'] = 50
        return app.redirect('/market')
    return render_template('registr.html', gnev_message='Пользователь с таким Телеграмом уже зарегистрирован')



@app.route('/log', methods=['POST'])
def log():
    name = request.form['name_log']
    tg = request.form['tg_log']
    pwd = request.form['pwd_log']

    res = db.get_adm(name, tg, pwd)
    if res['ok']:
        current_user['is_adm'] = True
        current_user['name'] = res['name']
        return app.redirect('/market')
    else:
        res = db.get_user(name, tg, pwd)
        if res['ok']:
            for k, v in res.items():
                current_user[k] = v
            return app.redirect('/market')
        else:
            return render_template('registr.html', gnev_message='Неверное имя или пароль') # возврат к странице входа

@app.route('/market')
def start_market():    
    _products = get_products()
    # print(_products)
    return render_template( 
        'market.html',
        vol=current_user['score'],
        products=_products
    )

@app.route('/basket')
def basket():
    products = db.get_basket(current_user['name'])
    return render_template(
        'cart.html',
        card_items=products,
        vol=current_user['score']
    )




app.run(debug=True)