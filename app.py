from flask import Flask, jsonify, request
from datetime import datetime
import secrets

print("Server running!")
app = Flask(__name__)

assign_id = 0
all_posts = {}

@app.route('/post', methods = ['POST'])
def new_post():
    global assign_id, all_posts
    file_type = request.headers.get('Content-Type')

    if (file_type == 'application/json'):
        input_data = request.get_json()

        if not 'msg' in input_data:
            return jsonify({'err': 'Missing msg field'}), 400
        else:
            input_msg = input_data['msg']

            post_id = assign_id
            assign_id += 1
            post_key = secrets.token_hex(16)
            post = {
                'id': post_id,
                'key': post_key,
                'timestamp': datetime.utcnow().isoformat(),
                'msg': input_msg
            }
            print(input_msg)     # Testing purpose
            print(post_key)      # Testing purpose   
            all_posts[post_id] = post

            return jsonify({
                'id': post_id,
                'key': post_key,
                'timestamp': post['timestamp']
            })

    else:
        return jsonify({'err': 'Bad request'}), 400
    
@app.route('/post/<int:inp_id>', methods = ['GET'])
def get_post(inp_id):
    global all_posts

    if inp_id not in all_posts:
        return jsonify({'err': 'Post not found'}), 404
    
    else:
        my_post = all_posts[inp_id]
        return jsonify({
            'id': my_post.get('id'),
            'timestamp': my_post.get('timestamp'),
            'msg': my_post.get('msg')
        })