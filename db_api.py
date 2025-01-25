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

    def get_user(self, name, pwd):
        query = f"""
        SELECT uname, uage, uscore
        FROM users
        WHERE uname='{name}' AND pwd='{pwd}';"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        return {'name': rows[0][0], 'age': rows[0][1], 'score': rows[0][2]}

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
        SELECT name, amount, description, price
        FROM products"""
        self.cursor.execute(query)
        self.conn.commit()
        rows = self.cursor.fetchall()
        res = []
        i = 1
        for row in rows:
            res.append({'i': i, 'title': row[0], 'amount': row[1], 'description': row[2], 'price': row[3]})
            i += 1
        return res

db = Database()
db.get_user('TestUser', 'gagagager')