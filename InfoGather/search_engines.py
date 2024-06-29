import webbrowser

class Search_Engine:
    def __init__(self, query: str):
        self.query = query

    def get_details(self):
        search_engines_endpoints = {"Google" : f"https://www.google.com/search?q={self.query}",
                            "Google Date" : f"https://www.google.com/search?q={self.query}&tbs=cdr:1,cd_min:1/1/0,sbd:1",
                            "Google News" : f"https://www.google.com/search?tbm=nws&q={self.query}", 
                            "Google Blogs" : f"https://www.google.com/search?q={self.query}&tbm=nws&tbs=nrt:b",
                            "Google FTP" : f"https://www.google.com/search?q=inurl:ftp -inurl:(http|https) {self.query}", 
                            "Google Index" : f"https://www.google.com/search?q=intitle:index.of+{self.query}", 
                            "Google Scholor" : f"https://scholar.google.com/scholar?&q={self.query}", 
                            "Google Patents" : f"https://patents.google.com/?q={self.query}", 
                            "Bing" : f'https://www.bing.com/search?q="{self.query}"', 
                            "Bing News" : f'https://www.bing.com/news/search?q="{self.query}"', 
                            "Yahoo" : f"https://search.yahoo.com/search?p={self.query}",
                            "Yandex" : f"https://www.yandex.com/yandsearch?text={self.query}",
                            "Baidu" : f"https://www.baidu.com/s?wd={self.query}",
                            "Searx" : f"https://searx.be/search?q={self.query}&categories=general",
                            "Exalead" : f"http://www.exalead.com/search/web/results/?q={self.query}",
                            "DuckDuckGo" : f"https://duckduckgo.com/?q={self.query}&ia=web",
                            "StartPage" : f"https://startpage.com/sp/search?q={self.query}",
                            "Qwant" : f"https://www.qwant.com/?q={self.query}&t=web",
                            "Brave" : f"https://search.brave.com/search?q={self.query}",
                            "Wayback" : f"https://web.archive.org/web/*/{self.query}",
                            "Ahmia" : f"https://ahmia.fi/search/?q={self.query}",
                            "Onionland" : f"https://onionlandsearchengine.net/search?q={self.query}",
                            "Tor.link" : f"https://tor.link/?q={self.query}"
    }

        for values in search_engines_endpoints.values():
            webbrowser.open(values)
        
    