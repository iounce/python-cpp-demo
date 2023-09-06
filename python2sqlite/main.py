import sqlite3

class Sqlite():
    def __init__(self, db='data.db'):
        self.db = db
        self.conn = None
        self.cur = None

    def open(self):
        result = True

        try:
            self.conn = sqlite3.connect(self.db)
        except Exception as e:
            self.conn = None
            result = False
            print(e)

        if not result:
            return result

        try:
            self.cur = self.conn.cursor()
        except Exception as e:
            self.cur = None
            result = False
            print(e)

        return result

    def insert(self, sql):
        commit = True
        try:
            self.cur.execute(sql)
        except Exception as e:
            commit = False
            print(e)

        if commit:
            self.conn.commit()

    def insert_batch(self, sql):
        commit = True
        try:
            self.cur.executescript(sql)
        except Exception as e:
            commit = False
            print(e)

        if commit:
            self.conn.commit()

    def query(self, sql):
        result = None

        try:
            res = self.cur.execute(sql)
        except Exception as e:
            res = None
            print(e)

        if res:
            result = res.fetchall()

        return result
    
    def execute(self, sql):
        commit = True
        try:
            self.cur.execute(sql)
        except Exception as e:
            commit = False
            print(e)

        if commit:
            self.conn.commit()
            
    def create(self, sql):
        self.execute(sql)
        
    def delete(self, sql):
        self.execute(sql)

    def close(self):
        if self.cur:
            self.cur.close()

        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    db = Sqlite('data.db')
    if db.open():
        db.create('''
                  create table tb_test(id integer primary key, name varchar(32) not null, age int not null);
                  ''')
        db.insert('''
                  insert into tb_test('name', 'age') values('Jack', 22);
                  ''')
        result = db.query('''
                       select * from tb_test;
                       ''')
        print(result)