from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('SAQ/form.html')

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
    
    # ここでorder_dataを処理するロジックを記述する
    
    return render_template('SAQ/order_result.html',order_data = order_data,price = price)


