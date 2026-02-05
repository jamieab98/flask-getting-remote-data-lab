import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def load_json(self):
        response = requests.get(self.url)
        return response.json()

    def get_response_body(self):
        data = json.dumps(self.get_response_body(), indent=1)
        return data

g = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
print(g.get_response_body())
print(g.load_json())