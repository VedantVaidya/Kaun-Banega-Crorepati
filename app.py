from flask import *
import dbm
import random
app=Flask(__name__,static_folder='static')

class idgen:
    count=1011

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/home")
def home():
    id=request.args.get("id")
    a=dbm.details(id) 
    return render_template("home.html",t=a)

@app.route("/wrong")
def wrong():
    id=request.args.get("id")
    money=request.args.get("money")
    dbm.addMoney(money,id)
    return render_template("wrong.html",id=id)





@app.route("/registerattempt",methods=["post"])
def registerattempt():
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    money=0
    id=idgen.count
    t=(name,email,password,id,money)
    dbm.reguser(t)
    idgen.count+=1
    elist=(name,email,id)
    return render_template("details.html",tp=elist)


@app.route("/loginattempt",methods=["post"])
def loginattempt():
    id=request.form["id"]
    password=request.form["password"]
    print(id,password)
    passcheck=dbm.logindata(id)
    print(passcheck)
    if len(passcheck) == 0:
        return redirect("/login")
    elif password in passcheck[0]: 
        return redirect(f"/home?id={id}")

@app.route("/play")
def play():
    id=request.args.get("id")
    q=int(request.args.get("q"))
    if q>=10:
        money="10000000"
        dbm.addMoney(money,id)
        return render_template("gamecomplete.html",id=id)
    elif q<11:
        op=("+","-","*")
        question=str(random.randint(0,9))+random.choice(op)+str(random.randint(0,9))+random.choice(op)+str(random.randint(0,9))
        ans=eval(question)  
        options=[ans,ans+random.randint(1,100),ans+random.randint(1,100),ans+random.randint(1,100)]
        random.shuffle(options)
    t=(question,options,ans,id,q)
    return render_template("play.html",t=t)

@app.route("/submit")
def submit():
    money=("0","1000","5000","10000","50000","160000","320000","640000","1250000","5000000","10000000")
    ans=request.args.get("ans")
    rans=request.args.get("rans")
    id=request.args.get("id")
    q=request.args.get("q")
    if ans==rans:
        q=int(q)+1
        t=(id,q,money[q])
        return render_template("correct.html",t=t)
    else:
        q=int(q)
        return redirect(f"/wrong?id={id}&money={money[q]}")

@app.route("/transfer")
def balance():
    id=request.args.get("id")
    a=dbm.details(id)
    return render_template("transfer.html",i=a)

@app.route("/trans",methods=["post"])
def trans():
    id=request.args.get("id")
    id2=request.form["id2"]
    money=request.form["money"]
    a=dbm.details(id)
    if int(a[3])<int(money):
        return redirect(f"/transfer?id={id}")
    dbm.subMoney(money,id)
    dbm.addMoney(money,id2)
    return redirect(f"/transfer?id={id}")  

@app.route("/adminlogin")
def adminlogin():
    return render_template("adminlogin.html")

@app.route("/adlog",methods=["post"])
def adlog():
    adminkey=request.form["adminkey"]
    if adminkey=="vedantthegreatestvaidya":
        return redirect("/admin87654321")
    else:
        return redirect("/adminlogin")

@app.route("/admin87654321")
def admin():
    a=dbm.detailsforadmin()
    return render_template("admin.html",t=a)

@app.route("/del")
def dele():
    id=request.args.get("id")
    dbm.deluser(id)
    return redirect("/admin87654321")

@app.route("/edit")
def edit():
    id=request.args.get("id")
    a=dbm.toedit(id)
    return render_template("edit.html",i=a)

@app.route("/update", methods=["post"])
def update():
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    id=request.form["id"]
    money=request.form["money"]
    t=(name,email,password,id,money,id)
    dbm.upd(t)
    return redirect("/admin87654321")




if __name__=="__main__":
    app.run(debug=True)


#create database gamezone;
#create table users(name varchar(20),email varchar(20),password varchar(20),id varchar(20),money varchar(20));