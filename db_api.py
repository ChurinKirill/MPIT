import psycopg2

conn_params = {
    'dbname': 'mpit_neimrkmerch',
    'user': 'postgres',
    'password': '123',
    'host': 'localhost',
    'port': 5432
}

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='mpit_neimarkmerch', user='postgres', password='123', host='localhost', port=5432)
        self.cursor = self.conn.cursor()

    def update_score(self, uid, score):
        query = f"""
        update users
        set uscore = {score}
        where id = '{uid}'"""
        self.cursor.execute(query)
        self.conn.commit()

    def get_user(self, login, pwd):
        query = f"""
        SELECT id, uname, uage, uscore, login
        FROM users
        WHERE login='{login}' AND pwd='{pwd}';"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            return {'ok': False}
        return {'ok': True, 'id': rows[0][0], 'name': rows[0][1], 'age': rows[0][2], 'score': rows[0][3], 'login':rows[0][4]}
    
    def get_adm(self, name, pwd):
        query = f"""
        SELECT name
        FROM admins
        WHERE name='{name}' AND pwd='{pwd}'"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            return {'ok': False}
        return {'ok': True, 'name': rows[0][0]}

    def add_user(self, name, login, pwd):
        query = f"""
        SELECT utg_username
        FROM users;"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        valid = True
        for row in rows:
            if tg == row[0]:
                valid = False
                break
        if valid:
            query = f"""
            INSERT INTO users (uname, uage, uscore, login, pwd, verified)
            VALUES ('{name}', 0, 50, '{login}', '{pwd}', 0);"""
            self.cursor.execute(query)
            self.conn.commit()
            return {'ok': True}
        else:
            return {'ok': False}

    def get_money(self, name):
        query = f"""
        SELECT uscore
        FROM users
        WHERE uname='{name}"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        return {'score': rows[0][0]}
    
    def get_products(self):
        query = f"""
        SELECT id, name, amount, description, price
        FROM products"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        res = []
        i = 1
        for row in rows:
            res.append({'i': i, 'pid': row[0], 'title': row[1], 'amount': row[2], 'description': row[3], 'price': row[4]})
            i += 1
        return res
    
    def get_users(self):
        query = f"""
        SELECT (uname, uage, login, uscore, verified)
        FROM users
        ORDER BY verified"""
        self.cursor.execute()
        self.conn.commit()
        rows = self.cursor.fetchall()
        res = []
    
    def get_basket(self, name):
        query = f"""
        select
            users.uname as name,
            products.name as 
            pname,
            products.amount as amount,
            products.price as price
        from basket
        inner join users on basket.uid = users.id
        inner join products on basket.pid = products.id
        where users.uname = '{name}';"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        res = []
        for row in rows:
            res.append({'pname': row[1], 'amount': row[2], 'price': row[3]})
        return res
    
    def get_basket_val(self, name):
        query = f"""
        select
            sum(products.price)
        from basket
        inner join users on basket.uid = users.id
        inner join products on basket.pid = products.id
        where users.uname = '{name}';"""
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchall()[0][0]
    
    def add_to_basket(self, uid, pid):
        query = f"""
        insert into basket (uid, pid)
        values ({uid}, {pid});"""
        self.cursor.execute(query)
        self.conn.commit()
    
    def clear_basket(self, uid):
        query = f"""
        delete from basket
        where uid={uid};"""
        self.cursor.execute(query)
        self.conn.commit()




# db = Database()
# db.get_adm('TestAdmin', 'gagagagernnnnadm')