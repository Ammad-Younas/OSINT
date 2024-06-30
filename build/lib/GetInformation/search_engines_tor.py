import webbrowser

class Search_Engine_Tor:
    def __init__(self, query: str):
        self.query = query
        
    def get_details(self):
        search_engines_tor_endpoints = {"Torch" : f"https://torch4st4l57l2u2vr5wqwvwyueucvnrao4xajqr2klmcmicrv7ccaad.onion/search?query={self.query}&action=search",
                            "Torr66" : f"https://www.tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion/search?q={self.query}",
                            "Haystack" : f"https://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q={self.query}", 
                            "SearchDemon" : f"https://srcdemonm74icqjvejew6fprssuolyoc2usjdwflevbdpqoetw4x3ead.onion/search?q={self.query}",
                            "Exavator" : f"https://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion/search/{self.query}",
                            "GDark" : f"https://zb2jtkhnbvhkya3d46twv3g7lkobi4s62tjffqmafjibixk6pmq75did.onion/gdark/search.php?query={self.query}",
                            "Hidden Reviews" : f"https://u5lyidiw4lpkonoctpqzxgyk6xop7w7w3oho4dzzsi272rwnjhyx7ayd.onion/?s={self.query}",
                            "Phobos" : f"https://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query={self.query}",
                            "Submarine" : f"https://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term={self.query}",
                            "DeepSearch" : f"https://searchgf7gdtauh7bhnbyed4ivxqmuoat3nm6zfrg3ymkq6mtnpye3ad.onion/search?q={self.query}",
                            "OnionCenter" : f"https://5qqrlc7hw3tsgokkqifb33p3mrlpnleka2bjg7n46vih2synghb6ycid.onion/index.php?a=search&q={self.query}",
                            "FreshOnion" : f"https://freshonifyfe4rmuh6qwpsexfhdrww7wnt5qmkoertwxmcuvm4woo4ad.onion/?query={self.query}",
    }

        print("Tor Browser is required for this search!")
        for values in search_engines_tor_endpoints.values():
            webbrowser.open(values)