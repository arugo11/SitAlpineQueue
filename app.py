from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('form.html')

order_data = {
    'sugar': 0,
    'strawberry': 0,
    'melon': 0,
    'lemon': 0
}

@app.route('/form', methods=['POST'])
def order():
    sugar = int(request.form.get('sugar'))
    strawberry = int(request.form.get('strawberry'))
    melon = int(request.form.get('melon'))
    lemon = int(request.form.get('lemon'))
    
    order_data = {
        '砂糖': sugar,
        'いちご': strawberry,
        'メロン': melon,
        'レモン': lemon
    }

    price = (sugar + strawberry + melon + lemon) * 300
    
    for i in order_data:
        if order_data[i] == 0:
            order_data[i] = "注文なし"
        else:
            order_data[i] = str(order_data[i]) + "つ"
    
    return render_template('order_result.html',order_data = order_data,price = price)
## 実行
if __name__ == "__main__":
    app.run(debug=True)
    db = SQLAlchemy(app) 
    db.create_all()
    from .models import orders