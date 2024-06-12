from flask import Flask, request, jsonify, render_template, redirect, url_for
from ice_cream_parlor import IceCreamParlor

app = Flask(__name__)
parlor = IceCreamParlor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cart')
def cart():
    cart_items = parlor.view_cart()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/search')
def search():
    keyword = request.args.get('keyword', '')
    results = parlor.search_flavors(keyword)
    return render_template('search.html', results=results, keyword=keyword)

@app.route('/add_allergen', methods=['GET', 'POST'])
def add_allergen():
    if request.method == 'POST':
        name = request.form['name']
        parlor.add_allergen(name)
        return redirect(url_for('index'))
    return render_template('add_allergen.html')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    flavor_id = request.form['flavor_id']
    quantity = request.form['quantity']
    parlor.add_to_cart(flavor_id, quantity)
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
