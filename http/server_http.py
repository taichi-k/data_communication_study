from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive():
    print("Received:", request.data.decode())
    return '', 204

if __name__ == '__main__':
    app.run(port=8081)
