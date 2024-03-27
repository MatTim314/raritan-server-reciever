from flask import Flask, request, jsonify, render_template_string
import logging
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)

# In-memory store for logs
log_entries = []

@app.before_request
def log_request_info():
    log_entry = f"{datetime.utcnow()} - {request.remote_addr} - {request.method} - {request.path}"
    log.info(log_entry)
    log_entries.append(log_entry)  # Store log entry

@app.route('/showdata', methods=['POST'])
def show_data():
    data = request.json
    return jsonify({"Received Data": data})

@app.route('/')
def home():
    logs = "<br>".join(log_entries)  # Format log entries for HTML
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Server Logs</title>
    </head>
    <body>
        <h2>Server Connection Logs:</h2>
        <p>{logs}</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
