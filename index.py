from flask import Flask, jsonify, request
import json
import user
import club
import webbrowser

app = Flask(__name__)
#list of json club objects
json_club_list = []
#list of club class ojects
club_object_list = []
#list of user class objects
users = []

with open('club_list.json') as data_file:
    json_club_list = json.load(data_file)
"""
Creates a new club object
@param name the name of the club
@param size the size of the club
@param website the website link of the club
@param time_commitment_grade the time commitment grade of the club
@param club_tags the list of club tags
@param professionalism_grade the professionalism grade of the club
@param interview_required boolean to tell if the club requires interviews
@param interview_grade the interview difficulty grade
@param club_meeting_frequency the meeting frequency of the club
@param join_listserv_link the link to join the listserv of the club
@param application_link the link to apply to the club
@param num_reviews the number of reviews the club has had
@param biography the biography of the club
@return a new club object with the specified parameters
"""
def create_clubs(name, size, website, time_commitment_grade, club_tags,
professionalism_grade, interview_required, interview_grade,
club_meeting_frequency, join_listserv_link, application_link, num_reviews,
biography):
    new_club = club.Club(name, size, website, time_commitment_grade, club_tags,
    professionalism_grade, interview_required, interview_grade,
    club_meeting_frequency, join_listserv_link, application_link, num_reviews,
    biography)
    return new_club

"""
Creates a new user object
@param name the name of the user
@param id the penn id
@param password the password for the user
@param unranked_clubs the list of json club data for the users initially
@param class_year the user's class year
@param undergrad_school the user's undergrad_school
@param pennkey the user's pennkey
@return a new user object with the specified parameters
"""
def create_user(name, id, password, unranked_clubs, class_year,
undergrad_school, pennkey):
    new_user = user.User(name, id, password, unranked_clubs, class_year,
    undergrad_school, pennkey)
    return new_user

"""
Sets up the list of club objects based on the json list
"""
def set_up_clubs_objects_list():
    for club_info in json_club_list:
        curr_club = create_clubs(club_info["name"], club_info["size"],
        "https://www.clubcorp.com/Clubs/Pyramid-Club", 3.7, ["Business","Social Impact"],
        2.4, True, 1.0, "2 hours / week", "https://www.uky.edu/~wallyf/list499.htm",
        "https://explorers.org/about/join/join_the_club", 80,
        "This is the best club on campus")
        club_object_list.append(curr_club)

#Jennifer user object
jennifer = create_user("Jennifer", 11223344, "ilovearun789", json_club_list,
2021, "SEAS", "jbazos")
users = [jennifer]
set_up_clubs_objects_list()

"""
Adds a new user to the list of users
@param new_user the new user the object
"""
def add_user(new_user):
    users.append(new_user)

"""
Find the user in the list of users
@param id the desired user id
@return the desired user, otherwise the future implementation will handle if not
in the list
"""
def find_user(id):
    temp_id = int(id)
    for curr_user in users:
        if curr_user.penn_id == temp_id:
            return curr_user
"""
Finds the club in the list of club class objects
@param club_name the club name
@return the desired club object, otherwise the future implementation will handle
if not in the list
"""
def find_club(club_name):
    for curr_club in club_object_list:
        if curr_club.get_name() == club_name:
            return curr_club

"""
Loads the main page of the
@return a string Welcoming to the page
"""
@app.route('/', methods=['GET'])
def main():
    return "Welcome to PennClubReview"

"""
Loads the Club review api
@return a string Welcoming to the api
"""
@app.route('/api')
def api():
    return "Welcome to the PennClubReview API!."

"""
Shows the json club list data
@return the jsonified club list data
"""
@app.route('/api/clubs', methods=['GET'])
def show_club_list():
    #temp_tuple = (club_list[0]["name"], club_list[0]["size"])
    #return str(temp_tuple[1])
    return jsonify(json_club_list)

"""
Adds to the json club list data and the list of clubs data. Also adds to each
users' ranking of clubs at the end.
@return the jsonified club list data
"""
@app.route('/api/clubs', methods=['POST'])
def add_to_club_list():
    #temp_tuple = (club_list[0]["name"], club_list[0]["size"])
    #return str(temp_tuple[1])
    new_club = {"name" : request.json["name"], "size" : request.json["size"]}
    json_club_list.append(new_club)
    curr_club = create_clubs(new_club["name"], new_club["size"],
    "https://www.clubcorp.com/Clubs/Pyramid-Club", 3.7, ["Business","Social Impact"],
    2.4, True, 1.0, "2 hours / week", "https://www.uky.edu/~wallyf/list499.htm",
    "https://explorers.org/about/join/join_the_club", 80,
    "This is the best club on campus")
    club_object_list.append(curr_club)
    for curr_user in users:
        curr_user.add_to_ranking(new_club)
    return jsonify(json_club_list)

"""
Shows the users' rankings of the clubs
@return the users' json club data rankings
"""
@app.route('/api/rankings', methods=['GET'])
def show_rankings():
    #temp_tuple = (club_list[0]["name"], club_list[0]["size"])
    #return str(temp_tuple[1])
    return jsonify(users[0].get_ranked_clubs())

"""
Changes the index of a users' rankings of the clubs
@return the users' json club data rankings
"""
@app.route('/api/rankings', methods=['POST'])
def change_rankings():
    user_id = request.json["id"] #the id of the user
    curr_user = find_user(user_id)
    #the desired club and it's new index
    curr_user.rank_a_club(request.json["club"], request.json["idx"])
    return jsonify(curr_user.get_ranked_clubs())

"""
Shows the desired user object
@param id the id of the user
@return the desired user object
"""
@app.route('/api/user/<int:id>', methods=['GET'])
def show_user_profile(id):
    # show the user profile for that user
    curr_user = find_user(id)
    return repr(curr_user)

"""
Shows the desired club object
@param club_name the club name
@return the json'ed version of the desired club's info
"""
@app.route('/api/clubs/<string:club_name>', methods=['GET'])
def show_club_profile(club_name):
    # show the user profile for that user
    curr_club = find_club(club_name)
    return jsonify(curr_club.json_the_data())

"""
Launches the website to a club
@param club_name the club's name
@return message to tell us it was sucessfully launched.
"""
@app.route('/api/clubs/<string:club_name>/web', methods=['GET'])
def show_club_website(club_name):
    # show the user profile for that user
    curr_club = find_club(club_name)
    webbrowser.open_new_tab(curr_club.get_website())
    return "loaded link to club website"

"""
Launches the link to join a club's listserv
@param club_name the club's name
@return message to tell us it was sucessfully launched.
"""
@app.route('/api/clubs/<string:club_name>/join', methods=['GET'])
def show_club_join_listserv(club_name):
    # show the user profile for that user
    curr_club = find_club(club_name)
    webbrowser.open_new_tab(curr_club.get_join_listserv_link())
    return "loaded link to join club listserv"

"""
Launches the application page to a club
@param The club's name
@return message to tell us it was sucessfully launched.
"""
@app.route('/api/clubs/<string:club_name>/apply', methods=['GET'])
def show_club_apply_link(club_name):
    # show the user profile for that user
    curr_club = find_club(club_name)
    webbrowser.open_new_tab(curr_club.get_application_link())
    return "loaded link to apply"

if __name__ == '__main__':
    app.run(debug=True)
