from flask import Flask, jsonify, request

app = Flask(__name__)

dishes = [
    {"id": 1, "name": "Pizza", "price": 10.99},
    {"id": 2, "name": "Burger", "price": 8.99},
    {"id": 3, "name": "Pasta", "price": 12.99}
]

@app.route('/dishes', methods=['GET'])
def get_dishes():
    return jsonify(dishes)

@app.route('/dishes/<int:id>', methods=['GET'])
def get_dish(id):
    dish = next((d for d in dishes if d['id'] == id), None)
    return jsonify(dish) if dish else ('', 404)

@app.route('/dishes', methods=['POST'])
def add_dish():
    new_dish = request.get_json()
    dishes.append(new_dish)
    return jsonify(new_dish), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
 
