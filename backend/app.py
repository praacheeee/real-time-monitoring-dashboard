from flask import Flask, jsonify
import psutil
from flask_cors import CORS

# Create the app first
app = Flask(__name__)

# Enable CORS AFTER creating app
CORS(app)

@app.route("/stats")
def stats():
    data = {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "processes": [
            {
                "pid": p.info["pid"],
                "name": p.info["name"],
                "cpu": p.info["cpu_percent"],
                "memory": p.info["memory_percent"]
            }
            for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
        ]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
