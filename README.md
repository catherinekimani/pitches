# Pitches

##### By Catherine Kimani

![catherine](/app/static/images/pitches.png)

### Pitches App

## Table of Content

+ [Description](#description)
+ [Live Link](#live-link)
+ [User Story](#user-story)
+ [BDD](#bdd)
+ [Installation Requirement](#Installation)
+ [Technology Used](#technology-used)
+ [Licence](#licence)
+ [Authors Info](#author-Info)

## Description
<P> This is a flask application that allows users to post one minute pitches and also allows users who are signed in to like,dislikes and comment on a pitch.The app also allows users to create pitches of different categories</p>

## Live Link

https://kate-pitches-world.herokuapp.com/

## User Story

* As a user, I would like to see the pitches other people have posted.
* As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
* As a user, I would like to be signed in for me to leave a comment
* As a user, I would like to receive a welcoming email once I sign up.
* As a user, I would like to view the pitches I have created in my profile page.
* As a user, I would like to comment on the different pitches and leave feedback.
* As a user, I would like to submit a pitch in any category.
* As a user, I would like to view the different categories.

## BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | *On page load* | Get all posts, Select between signup and login on the right side|
| Select SignUp| *Email,Username,Password* | Redirect to login|
| Select Login | *Username* and *password* | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | *Comment* | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

## Installation

### Requirements

* Make sure you have access to a browser

* Make Sure you have access to internet

### Installation Process

[Go Back to the top](#pitches)

## Technology Used
* HTML - which was used to build the structure of the pages.

* CSS - which was used to style the pages incuding the left aside navigation bar

* Python 

* Flask

## Licence

MIT License

Copyright (c) [2022] [MIT License](LICENSE)

[Go Back to the top](#pitches)

## Authors Info

Linked - [Catherine Kimani](https://www.linkedin.com/incatherine-kimani-5464ba1b6)

[Go Back to the top](#pitches)
