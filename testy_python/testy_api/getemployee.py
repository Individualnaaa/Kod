import requests

base_url = "http://127.0.0.1:8000/api"
employees_url = f"{base_url}/employees"

login_url = f"{base_url}/login"

my_headers1 = {
  'Content-Type': 'application/json'
}

my_payload2 = {
  "username": "admin",
  "password": "admin"
}

my_headers = {
  'Content-Type': 'application/json'
}

my_payload = {
}

response = requests.get(employees_url, headers=my_headers, json=my_payload)
print(response.json())

#to be continued