from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name", "Recruto")
    message = request.args.get("message", "Давай дружить")
    return f"<h1>Hello {name}! {message}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)