from flask import Flask, jsonify, request, render_template
from registor import look_food
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def main():
    return render_template("index.html")
@app.route("/api/lookFood", methods=['POST']) # json ingredients 안에 리스트로 와야함
def food_lookat():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No data"}), 400
    ingredients = data.get("ingredients", [])
    res = look_food(ingredients)
    print(res)
    return jsonify(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=999, debug=True)