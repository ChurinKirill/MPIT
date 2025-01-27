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
    login = request.form['login_reg']
    pwd = request.form['pwd_reg']

    res = db.add_user(name, login, pwd)

    if res['ok']:
        res = db.get_user(login, pwd)
        if res['ok']:
            for k, v in res.items():
                current_user[k] = v
        return app.redirect('/market')
    return render_template('registr.html', gnev_message='Пользователь с таким Телеграмом уже зарегистрирован')



@app.route('/log', methods=['POST'])
def log():
    login = request.form['login_log']
    pwd = request.form['pwd_log']

    res = db.get_adm(login, pwd)
    if res['ok']:
        current_user['is_adm'] = True
        current_user['name'] = res['name']
        return app.redirect('/market')
    else:
        res = db.get_user(login, pwd)
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
    total_p = db.get_basket_val(current_user['name'])
    return render_template(
        'cart.html',
        card_items=products,
        vol=current_user['score'],
        total_amount=len(products),
        total_price = total_p
        )

@app.route('/profile')
def profile():
    return render_template(
        'profile.html',
        vol=current_user['score'],
        name=current_user['name'],
        login=current_user['login']
    )

@app.route('/buy')
def buy():
    id = request.args.get('id')
    db.add_to_basket(current_user['id'], id)
    return app.redirect('/market')

@app.route('/clear')
def clear_basket():
    db.clear_basket(current_user['id'])
    return app.redirect('/basket')

@app.route('/buy_all')
def buy_all():
    total_p = db.get_basket_val(current_user['name'])
    if total_p > current_user['score']:
        gnev_msg = 'На балансе недостаточно НейМарков'
        return app.redirect('/basket')
    current_user['score'] -= total_p
    db.update_score(current_user['id'], current_user['score'])
    return app.redirect('/clear')




app.run(debug=True, host='0.0.0.0')