import requests
import pytest

@pytest.mark.get_employees1
def test_get_employees1(get_employees_url, auth_headers):

  # logowanie do api
  
  response = requests.get(url=get_employees_url, headers=auth_headers)
  response_body = response.json()
  assert response.status_code == 200

  # coś tu jest nie tak