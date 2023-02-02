from flask import Flask, render_template , request , redirect ,url_for ,session,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Test"

# >>> 數據庫 <<< #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
class users(db.Model):
    _id = db.Column("id" , db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    def __init__(self,name,email):
        self.name = name
        self.email = email


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/view")
def view():
    return render_template("view.html", values = users.query.all())
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        found_user = users.query.filter_by(name=user).delete()
        for user in found_user:
            user.delete()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user,"")
            db.session.add(usr)
            db.session.commit()
        flash("你登陸了")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("你已經登陸了")
            return redirect(url_for("user"))
            
        return render_template("login.html")
@app.route("/user",methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email 已經儲存了")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html",user=user)
    else:
        flash("你還沒登錄")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    session.pop("email",None)
    flash("你已經登出了","info")
    return redirect(url_for("login"))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)