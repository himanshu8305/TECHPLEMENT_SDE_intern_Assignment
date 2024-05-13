from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Configuration for log files and logging levels
LOG_CONFIG = {
    "log1": {"file_path": "log1.log", "level": "info"},
    "log2": {"file_path": "log2.log", "level": "error"},
    "log3": {"file_path": "log3.log", "level": "info"},
    # Add more log configurations as needed
}

def write_log(log_data, log_file):
    with open(log_file, 'a') as f:
        f.write(json.dumps(log_data) + '\n')

@app.route('/api/log', methods=['POST'])
def receive_log():
    data = request.json
    log_level = data.get('level', 'info')
    log_string = data.get('log_string', '')
    timestamp = data.get('timestamp', datetime.utcnow().isoformat())
    metadata = data.get('metadata', {})
    source = metadata.get('source', 'unknown')

    log_data = {
        "level": log_level,
        "log_string": log_string,
        "timestamp": timestamp,
        "metadata": metadata
    }

    if source in LOG_CONFIG:
        log_config = LOG_CONFIG[source]
        if log_level == 'error' or log_level == 'info':  # Validate log level
            if log_level == 'error' or log_config['level'] == 'info':
                write_log(log_data, log_config['file_path'])
                return jsonify({"message": "Log received and written successfully"}), 200
            else:
                return jsonify({"error": "Log level not permitted"}), 400
        else:
            return jsonify({"error": "Invalid log level"}), 400
    else:
        return jsonify({"error": "Invalid log source"}), 400

if __name__ == '__main__':
    app.run(debug=True)
