import requests

URLS = ["https://api.github.com", "http://localhost/"]
for url in URLS:

    response = requests.get(url)

    if response:
        print(str(response.status_code) + " --> Succesful!")
    else:
        raise Exception(f"Non-success status code: {response.status_code}")

    content_of_response = response.content
    print(type(content_of_response))
    print(response.text)
    print(response.headers)
    print(response.headers["Content-Type"])
    print(response.headers["Server"])
    print("##################################################################")
