import webbrowser

query = input("Enter your query: ")

search_engines_endpoints = {"Google" : f"https://www.google.com/search?q={query}",
                            "Google Date" : f"https://www.google.com/search?q={query}&tbs=cdr:1,cd_min:1/1/0,sbd:1",
                            "Google News" : f"https://www.google.com/search?tbm=nws&q={query}", 
                            "Google Blogs" : f"https://www.google.com/search?q={query}&tbm=nws&tbs=nrt:b",
                            "Google FTP" : f"https://www.google.com/search?q=inurl:ftp -inurl:(http|https) {query}", 
                            "Google Index" : f"https://www.google.com/search?q=intitle:index.of+{query}", 
                            "Google Scholor" : f"https://scholar.google.com/scholar?&q={query}", 
                            "Google Patents" : f"https://patents.google.com/?q={query}", 
                            "Bing" : f'https://www.bing.com/search?q="{query}"', 
                            "Bing News" : f'https://www.bing.com/news/search?q="{query}"', 
                            "Yahoo" : f"https://search.yahoo.com/search?p={query}",
                            "Yandex" : f"https://www.yandex.com/yandsearch?text={query}",
                            "Baidu" : f"https://www.baidu.com/s?wd={query}",
                            "Searx" : f"https://searx.be/search?q={query}&categories=general",
                            "Exalead" : f"http://www.exalead.com/search/web/results/?q={query}",
                            "DuckDuckGo" : f"https://duckduckgo.com/?q={query}&ia=web",
                            "StartPage" : f"https://startpage.com/sp/search?q={query}",
                            "Qwant" : f"https://www.qwant.com/?q={query}&t=web",
                            "Brave" : f"https://search.brave.com/search?q={query}",
                            "Wayback" : f"https://web.archive.org/web/*/{query}",
                            "Ahmia" : f"https://ahmia.fi/search/?q={query}",
                            "Onionland" : f"https://onionlandsearchengine.net/search?q={query}",
                            "Tor.link" : f"https://tor.link/?q={query}"
}

for values in search_engines_endpoints.values():
    webbrowser.open(values)