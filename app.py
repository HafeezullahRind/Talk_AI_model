import sys

print(sys.path)

sys.path.append('E:/Python/Python')

from flask import Flask, jsonify, request

from prediction import chatbot_response

app = Flask(__name__)



@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    message = data['message']
    response = chatbot_response(message)
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



