# CS 515-A 2023 - Project 3 - Web Forum

## Submitted By

- Name: Rahul Sohandani
- Email: rsohanda@stevens.edu

- Name: Sumedh Badnore
- Email: sbadnore@stevens.edu

- Name: Gowlikar Vishal
- Email: Vgowlika@stevens.edu

## Github URL

[Github Respository](https://github.com/sumedhbadnore/CS_515_Project_3)

## Description


This project employs the `Flask` framework for the backend, which provides diverse JSON REST API endpoints. These endpoints are designed to support the functionality of a web forum.

## Steps for installation

- Install python ,flask, Newman, Postman
- Make sure your flask server is running

## Hours spent on project

- Rahul Sohandani: 15 hours
- SumedhBadnore : 15 hours
- vishal gowlikar : 15 hours

## How the code was tested

- Initially, we conducted manual testing by thoroughly examining each endpoint to ensure functionality across various use cases.
- Upon transitioning the code to GitHub, we embraced GitHub Actions for automated test execution.
- Postman collections were employed for endpoint testing, validating their expected functionality.
- GitHub workflows were configured to simulate the gradescope environment, where postman collection tests were executed.
- Subsequently, we ran the tests on gradescope, ensuring successful completion of all test cases.

## Unresolved bugs or issues

- We did not encounter any major issues as such.

## Extensions Implemented

### Users and User Keys 

- This feature enables the creation of users while maintaining a record of all the posts attributed to them.
- Posts now include an additional user key, indicating the user responsible for their creation.

### Replies

- Users now have the ability to reply to other posts by adding a `replyId` key in the post, indicating the post being responded to.
- Posts with replies will include the IDs of the posts that have replied to them.

### Date Time Search

- This extension facilitates searching for posts made between a specified start time and end time.

### Threded Search
- Threaded Search allows for the display of entire threads, including all posts with their respective replies.

### User Search
- Users can search for all posts made by a specific user using the user's ID.

## Endpoints

### Endpoint #1: create a post with `POST /post`

- The default behavior functions as intended. Allows to create a post.
- Option to add `userid` specifying the user that made the post.
- Oprtion to specify `replyId` specifying a post to be replied to.

### Endpoint #2: read a post with `GET /post/{id}` 

- A GET request to `/post` returns the post with the specified id.

### Endpoint #3: delete a post with `DELETE /post/{{id}}/delete/{{key}}`

- A DELETE request to `/post/{{id}}/delete/{{key}}` is meant to delete the post with id id.

### Endpoint #4: create a user with `POST /user/create`

- A POST request to `/user/create` will create a user with the following fields:

- `username`: a string that is the username of the user to create. 
- `userid`: a unique id assigned to every user.
- `user_key`: a unique string assigned to every user.

### Endpoint #5: Search user between a particular time period `GET /searchposts`

- A GET request to `/searchposts` allows to search posts between a start time and an end time.
- This is how search has to be made `hosts/searchposts?start_datettime=2023-12-14 22:48:00&end_datetime=2023-12-14 22:52:00`.

### Endpoint #6: Threaded Search `GET /thread/{{id}}`

- A GET request to `/thread/{{id}}` allows for search for threaded replies from the post with the specified `id`.

### Endpoint #7: Searching all posts with a user `GET /user/search/{{userid}}`

- A GET request to `/user/search/{{userid}}` searches all the posts associated with a specified user.
