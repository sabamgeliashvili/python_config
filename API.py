from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    response = {'message': 'Hello, World!'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
