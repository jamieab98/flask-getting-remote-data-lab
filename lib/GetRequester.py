import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response = requests.get(self.url)
        data = json.dumps(response.json(), indent=1)
        return data

g = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
print(g.load_json())