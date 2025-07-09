from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive():
    print("Received:", request.data.decode())
    return '', 204

if __name__ == '__main__':
    # あらかじめ自己署名証明書を作成する:
    #   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 1 -nodes
    app.run(port=8081, ssl_context=('cert.pem', 'key.pem'))
