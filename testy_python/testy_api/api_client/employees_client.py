from base_api_client import BaseApiClient

class EmployeesClient(BaseAPIClient):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/employees"

    def create_employee(self, post_payload):
        return self.post(self.endpoint, json=post_payload)

