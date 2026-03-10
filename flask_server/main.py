from flask import Flask, request, jsonify
from core.data_engine import DataEngine
import pandas as pd

app = Flask(__name__)

engine = DataEngine()


@app.route("/health")
def health():
    return jsonify({"status": "running"})


@app.route("/load", methods=["POST"])
def load_dataset():
    dataset = request.get_json()
    return jsonify(engine.load_dataset(dataset))


@app.route("/upload-csv", methods=["POST"])
def upload_csv():

    if "file" not in request.files:
        return jsonify({"status": "error", "message": "No file uploaded"})

    file = request.files["file"]

    df = pd.read_csv(file)
    engine.df = df

    return jsonify({
        "status": "success",
        "records": len(df),
        "fields": list(df.columns)
    })


@app.route("/fields")
def fields():
    return jsonify(engine.get_fields())


@app.route("/records")
def records():

    limit = request.args.get("limit")

    if limit:
        limit = int(limit)

    return jsonify(engine.get_records(limit))


@app.route("/stats/<field>")
def stats(field):
    return jsonify(engine.get_stats(field))


@app.route("/filter")
def filter_records():

    field = request.args.get("field")
    value = request.args.get("value")

    return jsonify(engine.filter_records(field, value))


@app.route("/summary")
def summary():
    return jsonify(engine.dataset_summary())


@app.route("/dataset-info")
def dataset_info():
    return jsonify(engine.dataset_info())


@app.route("/correlations")
def correlations():
    return jsonify(engine.correlations())


@app.route("/profile")
def profile():
    return jsonify(engine.profile_dataset())


if __name__ == "__main__":
    app.run(debug=True)
