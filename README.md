# CS 515-A 2023 - Project 3 - Web Forum

## Submitted By

- Name: Rahul Sohandani
- Email: rsohanda@stevens.edu

- Name: Sumedh Badnore
- Email: sbadnore@stevens.edu

- Name: Gowlikar Vishal
- Email: Vgowlika@stevens.edu

## Github URL

[Github Respository] (https://github.com/sumedhbadnore/CS_515_Project_3)

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


