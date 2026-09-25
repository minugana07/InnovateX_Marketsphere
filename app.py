from flask import Flask, render_template, request, jsonify
from assessment import assess_market

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/assess", methods=["POST"])
def assess():

    data = request.get_json()

    market_id = data.get("market")

    result = assess_market(market_id)

    if result is None:
        return jsonify({
            "error": "Market not found"
        }), 404

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)