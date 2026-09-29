# import requests
# # METODA http, endpoint, headers, body



# import pytest

# @pytest.mark.api_login

# def test_logowanie(base_url, login_payload):
#     login_url = f"{base_url}/login"


# response = requests.post(url=login_url, json=login_payload)
# print(response.json())

# # lub definiujemy response_body = response.json() i potem wklejamy w miejscu response.json
# assert response.status_code == 200
# assert 'access_token' in response.json()
# assert response.json()['access_token']
# assert response.body['expires_in'] == 600


# # tu popoprawić!!!!! czemu nie robi mi się wcięcie w login_url