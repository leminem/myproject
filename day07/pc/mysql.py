import sqlite3
class Mysql(object):
    def __init__(self):
        self.conn=sqlite3.connect('douban.db')
        self.cursor=self.conn.cursor()
    def execute_sql(self,sql,data):
        self.cursor.execute(sql,data)
        self.conn.commit()
    def create_table(self,sql):
        sql = ''' CREATE TABLE BOOK
                   (id  integer primary key autoincrement,
                   name varchar(30),
                   author varchar(30),
                   public varchar(30),
                   content text,
                   page varchar(30),
                   price varchar(30),
                   public_year varchar(30),
                   isbn varchar(30)
                   );'''
        self.cursor.execute(sql)
        self.conn.commit()
    def __del__(self):
        self.cursor.close()
        self.conn.close()
if __name__ == '__main__':
    mysql=Mysql()
    # sql='INSERT INTO BOOK(name,author,public,content,page,price ,public_year,isbn)'\
    #                  'VALUES(?,?,?,?,?,?,?,?)'
    # data=('aa','yy','uyu','uou','uyu','ugu','uua','ubu')
    # mysql.execute_sql(sql,data)
    # c=conn.cursor()
