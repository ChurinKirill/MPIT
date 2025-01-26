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

    def get_user(self, name, tg, pwd):
        query = f"""
        SELECT uname, uage, uscore
        FROM users
        WHERE uname='{name}' AND utg_username='{tg}' AND pwd='{pwd}';"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            return {'ok': False}
        return {'ok': True, 'name': rows[0][0], 'age': rows[0][1], 'score': rows[0][2]}
    
    def get_adm(self, name, tg, pwd):
        query = f"""
        SELECT name
        FROM admins
        WHERE name='{name}' AND atg_username='{tg}' AND pwd='{pwd}'"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            return {'ok': False}
        return {'ok': True, 'name': rows[0][0]}

    def add_user(self, name, tg, pwd):
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
            INSERT INTO users (uname, uage, uscore, utg_username, pwd, verified)
            VALUES ('{name}', 0, 50, '{tg}', '{pwd}', 0);"""
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
        SELECT (uname, uage, utg_username, uscore, verified)
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



# db = Database()
# db.get_adm('TestAdmin', 'gagagagernnnnadm')