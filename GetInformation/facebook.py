import webbrowser

class Facebook:
    def __init__(self, facebook_username: str):
        self.username = facebook_username

    def get_facebook_detail(self):
        facebook_endpoints = {
        "Timeline" : f"https://www.facebook.com/{self.username}",
        "About" : f"https://www.facebook.com/{self.username}/about",
        "Overview" : f"https://www.facebook.com/{self.username}//about_overview",
        "Work and Education" : f"https://www.facebook.com/{self.username}/about?section=work",
        "Education" : f"https://www.facebook.com/{self.username}/about?section=education",
        "Living" : f"https://www.facebook.com/{self.username}/about?section=living",
        "Location" : f"https://www.facebook.com/{self.username}/about?section=living",
        "Contact Info" : f"https://www.facebook.com/{self.username}/about?section=contact-info",
        "Relationship" : f"https://www.facebook.com/{self.username}/about?section=relationship",
        "Relationship" : f"https://www.facebook.com/{self.username}/about?section=relationship",
        "Family" : f"https://www.facebook.com/{self.username}/about?section=family",
        "Biography" : f"https://www.facebook.com/{self.username}/about?section=bio",
        "Life Events" : f"https://www.facebook.com/{self.username}/about?section=year-overviews",
        "Friend" : f"https://www.facebook.com/{self.username}/friends",
        "Following" : f"https://www.facebook.com/{self.username}/following",
        "Photos" : f"https://www.facebook.com/{self.username}/photos",
        "Photos Album" : f"https://www.facebook.com/{self.username}/photos_albums",
        "Videos" : f"https://www.facebook.com/{self.username}/videos",
        "Reels" : f"https://www.facebook.com/{self.username}/reels",
        "Check-In" : f"https://www.facebook.com/{self.username}/places_visited",
        "Visits" : f"https://www.facebook.com/{self.username}/map",
        "Recent Check-Ins" : f"https://www.facebook.com/{self.username}/places_recent",
        "Sports" : f"https://www.facebook.com/{self.username}/sports",
        "Music" : f"https://www.facebook.com/{self.username}/music",
        "Movies" : f"https://www.facebook.com/{self.username}/movies",
        "TV" : f"https://www.facebook.com/{self.username}/tv",
        "Books" : f"https://www.facebook.com/{self.username}/books",
        "Games" : f"https://www.facebook.com/{self.username}/games",
        "Likes" : f"https://www.facebook.com/{self.username}/likes",
        "Events" : f"https://www.facebook.com/{self.username}/events",
        "Reviews" : f"https://www.facebook.com/{self.username}/reviews",
        "Reviews Given" : f"https://www.facebook.com/{self.username}/reviews_given",
        "Reviews Written" : f"https://www.facebook.com/{self.username}/reviews_written",
        "Reviews Written" : f"https://www.facebook.com/{self.username}/reviews_written",

    }

        for values in facebook_endpoints.values():
            webbrowser.open(values)