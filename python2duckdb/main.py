import duckdb

class DuckDb():
    def __init__(self, db='data.db'):
        self.db = db
        self.conn = None

    def open(self):
        result = True

        try:
            self.conn = duckdb.connect(self.db)
        except Exception as e:
            self.conn = None
            result = False
            print(e)

        return result

    def insert(self, sql):
        try:
            self.conn.execute(sql)
        except Exception as e:
            print(e)

    def insert_batch(self, sql):
        try:
            self.conn.execute(sql)
        except Exception as e:
            print(e)

    def query(self, sql):
        result = None

        try:
            res = self.conn.execute(sql)
        except Exception as e:
            res = None
            print(e)

        if res:
            result = res.fetchall()

        return result
    
    def execute(self, sql):
        try:
            self.conn.execute(sql)
        except Exception as e:
            print(e)

    def create(self, sql):
        self.execute(sql)
        
    def delete(self, sql):
        self.execute(sql)

    def close(self):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    db = DuckDb('data.db')
    if db.open():
        db.create('''
                  create sequence seq;
                  create table tb_test(id integer primary key default nextval('seq'), name varchar(32) not null, age int not null);
                  ''')
        db.insert('''
                  insert into tb_test(name, age) values('Jack', 22);
                  ''')
        result = db.query('''
                       select * from tb_test;
                       ''')
        print(result)