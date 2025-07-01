import requests

response = requests.get("https://api.github.com")

if response:
    print(str(response.status_code) + " --> Succesful!")
else:
    raise Exception(f"Non-success status code: {response.status_code}")

content_of_response = response.json()
for key, val in content_of_response.items():
    print(key + ":" + str(val))
print(response.headers)