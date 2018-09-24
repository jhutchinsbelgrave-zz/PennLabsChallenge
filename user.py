import base64

class User(object):

    name = "" # The user's name
    penn_id = 0 # The user's penn id
    pennkey = "" # The user's pennkey
    encoded_password = "" # The user's encoded_password
    class_year = 0 # The user's class year
    undergrad_school = "" # The user's undergrad_school
    ranked_clubs = [] # The user's ranked_clubs

    # The class "constructor" - It's actually an initializer
    """
    Creates a new user object
    @param name the name of the user
    @param id the penn id
    @param password the password for the user
    @param unranked_clubs the list of json club data for the users initially
    @param class_year the user's class year
    @param undergrad_school the user's undergrad_school
    @param pennkey the user's pennkey
    """
    def __init__(self, name, id, password, unranked_clubs, class_year,
    undergrad_school, pennkey):
        self.name = name
        self.penn_id = id
        self.encoded_password = base64.b64encode(password)
        self.ranked_clubs = unranked_clubs
        self.class_year = class_year
        self.undergrad_school = undergrad_school
        self.pennkey = pennkey

    """
    Moves the json club object
    @param club the club name of the desired club to be switched
    @param new_idx the new index for the club data to be moved to
    """
    def rank_a_club(self, club, new_idx):
        for club_info in self.ranked_clubs:
            if(club_info["name"] == club):
                try:
                    self.ranked_clubs.remove(club_info)
                    self.ranked_clubs.insert(new_idx, club_info)
                except ValueError:
                    pass
                break
    """
    Adds the club json data to the list of ranked clubs
    @param club the club json data
    """
    def add_to_ranking(self, club):
        self.ranked_clubs.append(club)

    """
    Gets the desired user id
    @return the desired user id
    """
    def get_id(self):
        return self.id

    """
    Gets the desired user password
    @return the desired user decoded password
    """
    def get_password(self):
        return self.base64.b64decode(encoded_password)

    """
    Gets the desired user's ranked json club data
    @return the desired user's club rankings json data
    """
    def get_ranked_clubs(self):
        return self.ranked_clubs
