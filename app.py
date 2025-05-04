from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return 'Backend attivo!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)