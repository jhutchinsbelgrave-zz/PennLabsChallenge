"""
Overall this would be the data that is presented to the viewers. We can give
users the ability to do w.e whether it's filter data on a club or be put
"""

class Club(object):
    name = "" #name of the club
    size = 0 #number of members
    website = "" #links to their website

    #grade based out of 4 to determine the time commitment
    time_commitment_grade = 0.0

    #list of tags associated with the clubs (i.e. tech, social impact, service, etc.)
    club_tags = []

    #grade based out of 4 to determine level of professionalism of the club.
    #In the future, this can be implemented as a slider instead of a number
    professionalism_grade = 0.0

    #determines if the club requires an interview or not
    interview_required = True

    #grade based out of 4 to determine the difficulty of the interview(s) for the club
    interview_grade = 0.0

    #Will be either N/A if not available, otherwise
    club_meeting_frequency = ""

    #Will be the link to join their listserv
    join_listserv_link = ""

    #link to their applications
    application_link = ""

    #Not enough time to implement, but averages ranking of club across all members
    overall_rank = 0.0

    #The number of times this club has been reviewed. Will be reset each year or semester
    #Prior to being cleared will have its data stored to keep yearly club data
    num_reviews = 0

    #biography of the club
    biography = ""

    #sponsors of the club. Will be implemented in the future
    sponsors = []

    #Not enough time, but the available pennkeys that can review a club
    #In the future, this will be linked to a database for faster access
    list_of_accepted_ids = []

    #json prepared list of the differnt data points
    json_version = []

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
    """
    def __init__(self, name, size, website, time_commitment_grade, club_tags,
    professionalism_grade, interview_required, interview_grade,
    club_meeting_frequency, join_listserv_link, application_link, num_reviews,
    biography):
        self.name = name
        self.size = size
        self.website = website
        self.time_commitment_grade = float(time_commitment_grade)
        self.club_tags = club_tags
        self.professionalism_grade = float(professionalism_grade)
        self.interview_required = interview_required
        self.interview_grade = float(interview_grade)
        self.club_meeting_frequency = club_meeting_frequency
        self.join_listserv_link = join_listserv_link
        self.application_link = application_link
        self.num_reviews = num_reviews
        self.biography = biography

    """
    Gets the club's name
    @return the club's name
    """
    def get_name(self):
        return self.name

    """
    Gets the club's size
    @return the club's size
    """
    def get_size(self):
        return self.size

    """
    Gets the club's website link
    @return the club's website link
    """
    def get_website(self):
        return self.website

    """
    Gets the club's time commitment grade
    @return the club's time commitment grade
    """
    def get_time_commitment_grade(self):
        return self.time_commitment_grade

    """
    Gets the club's tags
    @return the list of club's tags
    """
    def get_club_tags(self):
        return self.club_tags

    """
    Gets the club's professionalism grade
    @return the club's professionalism grade
    """
    def get_professionalism_grade(self):
        return self.professionalism_grade

    """
    Checks if the club requires interviews
    @return True if the club requires interviews, otherwise false
    """
    def get_interview_required(self):
        return self.interview_required

    """
    Gets the club's interview grade
    @return the club's interview grade
    """
    def get_interview_grade(self):
        return self.interview_grade

    """
    Gets the club's meeting frequency
    @return the club's meeting frequency
    """
    def get_club_meeting_frequency(self):
        return self.club_meeting_frequency

    """
    Gets the club's joining the listserv link
    @return the club's joining the listserv link
    """
    def get_join_listserv_link(self, ):
        return self.join_listserv_link

    """
    Gets the club's application link
    @return the club's application link
    """
    def get_application_link(self):
        return self.application_link

    """
    Gets the club's number of reviews
    @return the club's number of reviews
    """
    def get_num_reviews(self):
        return self.num_reviews

    """
    Gets the club's biography
    @return the club's biography
    """
    def get_bio(self):
        return self.biography

    """
    Sets the club's name
    @param name the club's name
    """
    def set_name(self, name):
        self.name = name

    """
    Sets the club's size
    @param size the club's size
    """
    def set_size(self, size):
        self.size = size

    """
    Sets the club's website
    @param website the club's website
    """
    def set_website(self, website):
        self.website = website
    """
    Changes the club's time_commitment_grade
    @param time_commitment_grade the club's new grade being assigned
    """
    def add_to_time_commitment_grade(self, time_commitment_grade):
        temp_grade = self.time_commitment_grade * num_reviews
        num_reviews = num_reviews + 1
        temp_grade = temp_grade + time_commitment_grade
        self.time_commitment_grade = temp_grade / num_reviews

    """
    Prepares the class to be jsonified
    @return the club's data in a json ready format
    """
    def json_the_data(self):
        json_version = [{
        "name": self.name,
        "size": self.size,
        "website": self.website,
        "time_commitment_grade": self.time_commitment_grade,
        "club_tags": self.club_tags,
        "professionalism_grade": self.professionalism_grade,
        "interview_required": self.interview_required,
        "interview_grade": self.interview_grade,
        "club_meeting_frequency": self.club_meeting_frequency,
        "join_listserv_link": self.join_listserv_link,
        "application_link": self.application_link,
        "num_reviews": self.num_reviews,
        "biography": self.biography }]

        return json_version

    #For the sake of this implementation, we won't implement the rest of the functions
