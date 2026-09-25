from flask import Flask, render_template, request, jsonify
from assessment import assess_market

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/assessment")
def assessment():
    return render_template("assessment.html")


@app.route("/comparison")
def comparison():
    return render_template("comparison.html")


@app.route("/strategy")
def strategy():
    return render_template("strategy.html")


@app.route("/risks")
def risks():
    return render_template("risks.html")


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