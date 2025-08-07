from flask import Flask, jsonify, request

app = Flask(__name__)

# Oddiy API endpoint
@app.route('/salom', methods=['GET'])
def salom_ber():
    return jsonify({"javob": "Salom, dunyo!"})

# Parametr bilan API
@app.route('/ko‘paytir', methods=['GET'])
def kopaytir():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({"natija": a * b})

if __name__ == '__main__':
    app.run(debug=True)