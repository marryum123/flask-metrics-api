from flask import Flask, jsonify, request
import json
import logging
import os

logging.basicConfig(
    filename="/home/marryum32/mysite/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)

@app.before_request
def log_request():
    logging.info("Request received: %s %s", request.method, request.path)

@app.route("/metrics")
def get_metrics():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "sample_metrics.json")

        with open(file_path, "r") as file:
            metrics = json.load(file)

        return jsonify(metrics)

    except Exception as e:
        logging.error("Failed to load metrics: %s", e)
        return jsonify({"error": "Unable to load metrics"}), 500