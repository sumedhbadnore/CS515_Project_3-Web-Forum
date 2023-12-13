from flask import Flask, jsonify
from datetime import datetime

print("Server running!")
app = Flask(__name__)

all_posts = {}

@app.route('/post', methods = ['POST'])
def new_post():
    temp_id = 1
    temp_key = "dkjfe234"
    post = {
        'id': temp_id,
        'key': temp_key,
        'timestamp': datetime.utcnow().isoformat(),
        'msg': "Hello World!"
    }

    all_posts[0] = post
    return jsonify({
        'id': temp_id,
        'key': temp_key,
        'timestamp': post['timestamp']
    })
