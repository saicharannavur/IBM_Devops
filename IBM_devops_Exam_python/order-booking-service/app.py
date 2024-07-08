from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = next((o for o in orders if o['id'] == id), None)
    return jsonify(order) if order else ('', 404)

@app.route('/orders', methods=['POST'])
def add_order():
    new_order = request.get_json()
    orders.append(new_order)
    return jsonify(new_order), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
 
