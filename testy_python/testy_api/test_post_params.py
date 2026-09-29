import requests
import pytest

@pytest.mark.post_employee
def test_post_employees(get_employees_url, auth_headers, post_payload):
  response = requests.post(url=get_employees_url, headers=auth_headers, json=post_payload)
  response_body = response.json()
  assert response.status_code == 200

  for key, value in post_payload.items():
    assert response_body[key] == value
  assert 'id' in response_body
  assert isinstance(response_body['id'], int)