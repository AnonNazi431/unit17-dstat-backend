from flask import Flask, jsonify
from flask_cors import CORS
import psutil
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/api/live")
def live_stats():
    net = psutil.net_io_counters()
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    return jsonify({
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_percent": cpu,
        "memory_percent": mem.percent,
        "bytes_sent": net.bytes_sent,
        "bytes_recv": net.bytes_recv
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
