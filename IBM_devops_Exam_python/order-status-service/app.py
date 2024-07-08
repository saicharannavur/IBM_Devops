from flask import Flask, jsonify, request

app = Flask(__name__)

order_statuses = []

@app.route('/statuses', methods=['GET'])
def get_statuses():
    return jsonify(order_statuses)

@app.route('/statuses/<int:id>', methods=['GET'])
def get_status(id):
    status = next((s for s in order_statuses if s['id'] == id), None)
    return jsonify(status) if status else ('', 404)

@app.route('/statuses', methods=['POST'])
def add_status():
    new_status = request.get_json()
    order_statuses.append(new_status)
    return jsonify(new_status), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
 
