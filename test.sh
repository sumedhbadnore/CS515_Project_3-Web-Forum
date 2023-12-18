#!/bin/sh

set -e # exit immediately if newman complains
trap 'kill $PID' EXIT # kill the server on exit

./run.sh &
PID=$! # record the PID

newman run forum_multiple_posts.postman_collection.json -e env.json
newman run forum_post_read_delete.postman_collection.json 
newman run Test.postman_collection.json 