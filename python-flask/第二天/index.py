from flask import Flask, render_template, request , redirect ,session ,url_for
import random
app = Flask(__name__)
app.secret_key = "Test"
@app.route("/",methods=["POST","GET"])
def home(): #用來回應首頁連線函式
    if request.method == "POST":
        return render_template("game.html",number=request.form["number"])
    else:
        return render_template("game.html")

#啟動網站伺服器
if __name__ == "__main__":
    app.run()