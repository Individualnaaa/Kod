# import requests
# # METODA http, endpoint, headers, body



# import pytest

# @pytest.mark.api_login
# def test_get_employees():
#     base_url = "http://127.0.0.1:8000/api"
#     get_employees_url = f"{base_url}/login"

# #logowanie do api


#     login_url = f"{base_url}/login"

#     my_payload = {
#         "username": "admin",
#         "password": "admin"
#     }

#     login_response = requests.post(login_url, json=my_payload)
#     access_token = login_responde.json()['access_token']


#     auth_headers = {
#         'Content-Type': 'application/json'
#         'Authorization': f'Bearer {access_token}'
#     }


# response = requests.post(url=get_employee_url, headers=auth_headers)
# print(response.json())

# # lub definiujemy response_body = response.json() i potem wklejamy w miejscu response.json
# assert response.status_code == 200
# assert 'access_token' in response.json()
# assert response.json()['access_token']
# assert response.body['expires_in'] == 600

# # coś nie działa ze spacjami