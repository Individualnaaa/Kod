import requests
import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.post_employee
def test_post_employees(get_employees_url, auth_headers, post_payload):
  
  logger.info(f"Wysyłanie POST do {get_employees_url} z danymi: {post_payload}")
 
  response = requests.post(url=get_employees_url, headers=auth_headers, json=post_payload)
  response_body = response.json()

  logger.info(
        f"Otrzymano status {response.status_code}, odpowiedź: {response_body}"
    )
  assert response.status_code == 200


  for key, value in post_payload.items():
    assert response_body[key] == value
  assert 'id' in response_body
  assert isinstance(response_body['id'], int)

  #zmienic loggery totalnie!!!!!!