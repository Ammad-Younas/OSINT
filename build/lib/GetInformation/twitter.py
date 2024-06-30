import webbrowser

class Twitter:
    def __init__(self, twitter_username: str):
        self.username = twitter_username
          
    def get_twitter_detail(self):
        twitter_endpoints = {
        "Profile" : f"https://www.twitter.com/{self.username}",
        
    }

        for values in twitter_endpoints.values():
            webbrowser.open(values)