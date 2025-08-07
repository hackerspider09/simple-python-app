from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "UP"}), 200

@app.route('/', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"}), 200


@app.route('/host', methods=['GET'])
def getHost():
    # time.sleep(2)
    s= socket.gethostname()
    ip_address = socket.gethostbyname(s)

    return jsonify(f"Hello Host name : {s}, Host addr : {ip_address}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
