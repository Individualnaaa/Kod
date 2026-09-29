import requests

class BaseApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def set_auth_headers(self, auth_headers):
        self.session.headers.update(auth_headers)

    def delete(self, endpoint, headers=None):
        return self.delete(url=f"{self.base_url}{endpoint}, headers=headers")