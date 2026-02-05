import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def load_json(self):
        response = requests.get(self.url)
        return response.content

    def get_response_body(self):
        data = json.dumps(self.load_json(), indent=1)
        return data

g = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
print(g.load_json())