from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API Running"

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    result = data.get("a", 0) + data.get("b", 0)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)