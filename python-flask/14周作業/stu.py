from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def stu(): #用來回應首頁連線函式
    return render_template("stu.html")

@app.route("/stu_return", methods=['POST'])#建立 接收表單 回應方式
def stu_return(): #用來回應絕對值表單連線函式
    N = request.form['n']
    S = request.form['sex']
    E = request.form['expert']
    I = request.form.getlist('intr')
    
    return render_template("stu_return.html", sex=S, intr=I, n=N, expert=E)
#啟動網站伺服器
app.run(debug=True)