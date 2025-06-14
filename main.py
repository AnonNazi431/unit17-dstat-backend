from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

@app.route("/stats")
def stats():
    return jsonify({
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "requests_per_second": 100,
        "unique_ips": 5,
        "top_ips": [
            {"ip": "192.168.1.10", "count": 50},
            {"ip": "192.168.1.20", "count": 30},
            {"ip": "192.168.1.30", "count": 20}
        ],
        "top_urls": [
            { "url": "/login", "count": 40 },
            { "url": "/api/data", "count": 30 },
            { "url": "/home", "count": 15 }
        ]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # guna PORT dari Railway
    app.run(host="0.0.0.0", port=port)
