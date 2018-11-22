import pymysql

class Mysqlpython():
    def __init__(self,database,host='localhost',user='root',password='123456',charset='utf8',port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port 

    def open(self):
        self.db = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database,charset=self.charset,port=self.port)
        #封装一个游标对象
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def zhixing(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        self.db.commit()
        self.close()

    def All(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        result = self.cur.fetchall()
        self.close()
        return result
    
    def Many(self,sql,n,L=[]):
        self.open()
        self.cur.execute(sql,L)
        result = self.cur.fetchmany(n)
        self.close()
        return result

