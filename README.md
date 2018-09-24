# Penn Server Challenge

## Installation
Here are the dependencies for this project:
  1. This project was run on python 2.7.0. and Flask 1.0.2. From flask:
    a. flask
    b. request
    c. jsonify

  2. The following are imports that should already come packaged in python 2.7.0,
  but if not here they are for your own personal download:
    a. json
    b. webbrowser
    c. base64 (user.py)

  3. The remaining imports in index.py are already packaged in the zip when you
  download from git

## implementation
club_list.json:
  1. Traditional json data as initially provided for the Challenge
  2. Nothing here has changed

fun.py:
  1. modulo() divides successfully without using the % operator
  2. question_mark() successfully checks if the given string meets the desired
  conditions

user.py:
  1. This file represents the user class
  2. Within this file, we have a handful of class fields meant to represent the
  currently desired user information as requested in the Challenge and some
  hopefully future additions to the user data.
  3. The object can be be initialized by the User() method with the given
  parameters. These were all common identifiers for users that we care the most
  about and can be used for future data analytics based on class year, undergrad
  school, and even overall rankings for clubs across all users.
  4. There are a handful of getter and setter methods well documented within
  those classes as well.

  In the future: If I had more time, I would expand upon the data that we can
  gather and present for a user. Such as comments or profiles connected to the
  Penn Labs platform

club.py:
  1. The importance of this file is to meet the requirements of adding a new
  feature to the PennClubReview Page. It represents a way for us to add more
  data to the clubs without having to see it all as json data. While my
  design of the club class is complete, there's still more I wished to complete,
  which will be discussed in the "In the Future Section".
  2. This file also represents the club class
  3. In this file, there are various class fields collecting a handful of data
  points that the users of the review site will either care most about or would
  like to have the easiest access to seeing. There is room for much expansion in
  regards to the type of information we collect on clubs and analyzing the data
  surrounding certain clubs such as their interview processes, their time
  commitment, and much more.
  4. Some, if not all, data points can be gathered and changed by the getter
  and setter methods of this class.

  In the Future: I hope to implement a comments section for each of the clubs,
  which will be stored in a database. I also hope to have more user data
  collected across the years, so users can see how this club is viewed by the
  entirety of the community. Aside from the implementation of manipulating the
  data within the class that I already commented for, there's also room for
  to allow club to add documents that users can have to learn about the club
  and make their work more accessible or even learn about upcoming events.


index.py:

  1. This file runs the application
  2. It does all of the following:
    a. There's a user object for Jennifer
    b. Implement Jennifer's rankings of the clubs in club_list
    c. Implements a route at GET /api/clubs  that will serve the list of clubs in
    JSON format (refer to Python docs for JSON formatting.
    d. Implements a route at POST /api/clubs that will create a new club, with its
    club information specified as parameters in the request body.
    e. Implements a route at POST /api/rankings that will change the ranking of
    a specified club in Jennifer's rankings (that you implemented in the third
    step).
    f. Implements a route at GET /api/rankings that will serve Jennifer's
    rankings in JSON format.
    g. Implements a route at GET /api/user/:id that will return a user whose id
    is specified as a route parameter (i.e. :id ).
    h. Implememnts a handful of GET functions for accessing user and club object
    data in json format

  In the future: I hope to implement a database to store the json data, the club
  class object information, and the user information. This will make the files
  much more lightweight in the future. Furthermore, I would like to build a more
  user-friendly interface for easy interaction with the web application.
