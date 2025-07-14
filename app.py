from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Replace this with your MongoDB connection string
client = MongoClient("mongodb+srv://Sai123:Akd1EOO3ILG4sIZ6@cluster0.i4zvjr1.mongodb.net/webhook_db?retryWrites=true&w=majority&appName=Cluster0")
db = client.webhook_db
collection = db.events

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    author = data.get('sender', {}).get('login', 'unknown')
    timestamp = datetime.utcnow().isoformat()

    from_branch = data.get('pull_request', {}).get('head', {}).get('ref')
    to_branch = data.get('pull_request', {}).get('base', {}).get('ref')

    if event_type == 'push':
        to_branch = data.get('ref').split('/')[-1]

    event = {
        "author": author,
        "event_type": event_type,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }

    collection.insert_one(event)
    return jsonify({"status": "success"}), 200

@app.route('/events', methods=['GET'])
def events():
    result = list(collection.find({}, {'_id': 0}))
    return jsonify(result)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(port=5000)
