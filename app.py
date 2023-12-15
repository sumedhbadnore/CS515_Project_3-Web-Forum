from flask import Flask, jsonify, request
from datetime import datetime
import secrets
import threading

print("Server running!")
app = Flask(__name__)

assign_post_id = 0
assign_user_id = 0
all_posts = {}
users = {}
lock_state = threading.Lock()

@app.route('/post', methods = ['POST'])
def new_post():
    with lock_state:
        global assign_post_id, all_posts, users
        file_type = request.headers.get('Content-Type')

        if (file_type == 'application/json'):
            input_data = request.get_json()

            if 'msg' in input_data:
                if 'userid' in input_data:
                    if input_data['userid'] in users:
                        input_msg = input_data['msg']
                        user_id = input_data['userid']
                        post_id = assign_post_id
                        assign_post_id += 1
                        post_key = secrets.token_hex(16)
                        post = {
                            'id': post_id,
                            'key': post_key,
                            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            'msg': input_msg,
                            'userid': user_id
                        }
                        print(input_msg)     # Testing purpose
                        print(post_key)      # Testing purpose   
                        all_posts[post_id] = post

                        return jsonify({
                            'id': post_id,
                            'key': post_key,
                            'timestamp': post['timestamp'],
                            'userid': user_id
                        })
                else:
                    pass
                input_msg = input_data['msg']

                post_id = assign_post_id
                assign_post_id += 1
                post_key = secrets.token_hex(16)
                post = {
                    'id': post_id,
                    'key': post_key,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
                return jsonify({'err':'Missing msg field'}), 400
        
        else:
            return jsonify({'err':'Bad request'}), 400
    
@app.route('/post/<int:inp_id>', methods = ['GET'])
def get_post(inp_id):
    with lock_state:
        global all_posts

        if inp_id not in all_posts:
            return jsonify({'err':'Post not found'}), 404
        
        else:
            my_post = all_posts[inp_id]
            return jsonify({
                'id': my_post.get('id'),
                'timestamp': my_post.get('timestamp'),
                'msg': my_post.get('msg')
            })
        
@app.route('/post/<int:inp_id>/delete/<string:inp_key>', methods = ['DELETE'])
def delete_post(inp_id, inp_key):
    with lock_state:
        global all_posts

        if inp_id not in all_posts:
            return jsonify({'err':'Post not found'}), 404
        
        else:
            my_post = all_posts[inp_id]
            if my_post['key'] == inp_key:
                del all_posts[inp_id]
                print("Deleted Successfully!")          # Testing purpose
                return jsonify({
                    'id': my_post.get('id'),
                    'key': my_post.get('key'),
                    'timestamp': my_post.get('timestamp')
                })
            
            else:
                return jsonify({'err':'Forbidden'}), 403
            
@app.route('/user/create', methods = ['POST'])
def create_user():
    with lock_state:
        global users, assign_user_id
        file_type = request.headers.get('Content-Type')

        if (file_type == 'application/json'):
            input_data = request.get_json()

            if 'username' in input_data:
                if input_data['username'] in users:
                    return jsonify({'err':'User already exists'}), 403
                
                user_name = input_data['username']
                user_id = assign_user_id
                assign_user_id += 1
                user_key = secrets.token_hex(2)
 
                user = ({
                    'username': user_name,
                    'userid': user_id,
                    'userkey': user_key,
                    'timestamp': datetime.utcnow().isoformat()
                })
                users[user_id] = user
                
                print('User created successfully.')        # Testing purpose

                return jsonify({
                    'username': user_name,
                    'userid': user_id,
                    'userkey': user_key,
                    'timestamp': datetime.utcnow().isoformat()
                })
            
            else:
                return jsonify({'err':'Missing username field'}), 400
        else:
            print("Triggered")
            return jsonify({'err':'Bad request'}), 400

@app.route('/searchposts')
def search_date_time():
    with lock_state:
        start_datetime_str = request.args.get('start_datetime')
        end_datetime_str = request.args.get('end_datetime')

        try:
            start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M:%S") if start_datetime_str else None
            end_datetime = datetime.strptime(end_datetime_str, "%Y-%m-%d %H:%M:%S") if end_datetime_str else None

            filtered_posts = []

            # print(all_posts)

            for post in all_posts:
                my_post = all_posts[post]
                post_timestamp = datetime.strptime(my_post.get("timestamp"), "%Y-%m-%d %H:%M:%S")

                if start_datetime and post_timestamp < start_datetime:
                    continue

                if end_datetime and post_timestamp > end_datetime:
                    continue

                filtered_posts.append(my_post)

            return jsonify({"posts": filtered_posts})
        except ValueError:
            return jsonify({"err": "Invalid datetime format. Use YYYY-MM-DD HH:MM:SS"}), 400

if __name__ == '__main__':
    app.run(debug=True)