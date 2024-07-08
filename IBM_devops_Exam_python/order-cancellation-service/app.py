from flask import Flask, jsonify, request

app = Flask(__name__)

cancellations = []

@app.route('/cancellations', methods=['GET'])
def get_cancellations():
    return jsonify(cancellations)

@app.route('/cancellations/<int:id>', methods=['GET'])
def get_cancellation(id):
    cancellation = next((c for c in cancellations if c['id'] == id), None)
    return jsonify(cancellation) if cancellation else ('', 404)

@app.route('/cancellations', methods=['POST'])
def add_cancellation():
    new_cancellation = request.get_json()
    cancellations.append(new_cancellation)
    return jsonify(new_cancellation), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
 
