import webbrowser

query = input("Enter your username: ")

facebook_endpoints = {
    "Timeline" : f"https://www.facebook.com/{query}",
    "About" : f"https://www.facebook.com/{query}/about",
    "Overview" : f"https://www.facebook.com/{query}//about_overview",
    "Work and Education" : f"https://www.facebook.com/{query}/about?section=work",
    "Education" : f"https://www.facebook.com/{query}/about?section=education",
    "Living" : f"https://www.facebook.com/{query}/about?section=living",
    "Location" : f"https://www.facebook.com/{query}/about?section=living",
    "Contact Info" : f"https://www.facebook.com/{query}/about?section=contact-info",
    "Relationship" : f"https://www.facebook.com/{query}/about?section=relationship",
    "Relationship" : f"https://www.facebook.com/{query}/about?section=relationship",
    "Family" : f"https://www.facebook.com/{query}/about?section=family",
    "Biography" : f"https://www.facebook.com/{query}/about?section=bio",
    "Life Events" : f"https://www.facebook.com/{query}/about?section=year-overviews",
    "Friend" : f"https://www.facebook.com/{query}/friends",
    "Following" : f"https://www.facebook.com/{query}/following",
    "Photos" : f"https://www.facebook.com/{query}/photos",
    "Photos Album" : f"https://www.facebook.com/{query}/photos_albums",
    "Videos" : f"https://www.facebook.com/{query}/videos",
    "Reels" : f"https://www.facebook.com/{query}/reels",
    "Check-In" : f"https://www.facebook.com/{query}/places_visited",
    "Visits" : f"https://www.facebook.com/{query}/map",
    "Recent Check-Ins" : f"https://www.facebook.com/{query}/places_recent",
    "Sports" : f"https://www.facebook.com/{query}/sports",
    "Music" : f"https://www.facebook.com/{query}/music",
    "Movies" : f"https://www.facebook.com/{query}/movies",
    "TV" : f"https://www.facebook.com/{query}/tv",
    "Books" : f"https://www.facebook.com/{query}/books",
    "Games" : f"https://www.facebook.com/{query}/games",
    "Likes" : f"https://www.facebook.com/{query}/likes",
    "Events" : f"https://www.facebook.com/{query}/events",
    "Reviews" : f"https://www.facebook.com/{query}/reviews",
    "Reviews Given" : f"https://www.facebook.com/{query}/reviews_given",
    "Reviews Written" : f"https://www.facebook.com/{query}/reviews_written",
    "Reviews Written" : f"https://www.facebook.com/{query}/reviews_written",

}

for values in facebook_endpoints.values():
    webbrowser.open(values)