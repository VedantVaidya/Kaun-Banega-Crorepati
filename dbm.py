import pymysql as p

def getcon():
    return p.connect(host="localhost",user="root",password="",port=3306,database="gamezone")

def reguser(t):
    c=getcon()
    cur=c.cursor()
    qur="insert into users values(%s,%s,%s,%s,%s)"
    cur.execute(qur,t)
    c.commit()
    c.close()

def details(id):
    c=getcon()
    cur=c.cursor()
    qur="select name,email,id,money from users where id=%s"
    cur.execute(qur,id)
    a=cur.fetchall()
    c.commit()
    c.close()
    return(a[0])

def logindata(id):
    c=getcon()
    cur=c.cursor()
    qur="select password from users where id=%s"
    cur.execute(qur,id)
    a=cur.fetchall()
    c.commit()
    c.close()
    return(a)

def addMoney(money,id):
    c=getcon()
    cur=c.cursor()
    qur="select money from users where id=%s"
    cur.execute(qur,id)
    a=cur.fetchall()
    toadd=int(a[0][0])+int(money)
    t=(toadd,id)
    qur2="update users set money=%s where id=%s"
    cur.execute(qur2,t)
    c.commit()
    c.close()

def subMoney(money,id):
    c=getcon()
    cur=c.cursor()
    qur="select money from users where id=%s"
    cur.execute(qur,id)
    a=cur.fetchall()
    tosub=int(a[0][0])-int(money)
    t=(tosub,id)
    qur2="update users set money=%s where id=%s"
    cur.execute(qur2,t)
    c.commit()
    c.close()

def detailsforadmin():
    c=getcon()
    cur=c.cursor()
    qur="select * from users"
    cur.execute(qur)
    a=cur.fetchall()
    c.commit()
    c.close()
    return(a)


def deluser(id):
    c=getcon()
    cur=c.cursor()
    qur="delete from users where id=%s"
    cur.execute(qur,id)
    c.commit()
    c.close()

def toedit(id):
    c=getcon()
    cur=c.cursor()
    qur="select * from users where id=%s"
    cur.execute(qur,id)
    a=cur.fetchall()
    c.commit()
    c.close()
    return(a[0])

def upd(t):
    c=getcon()
    cur=c.cursor()
    qur="update users set name=%s,email=%s,password=%s,id=%s,money=%s where id=%s"
    cur.execute(qur,t)
    c.commit()
    c.close()
