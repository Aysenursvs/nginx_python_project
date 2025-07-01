import requests

for _ in range(5):
    response = requests.get("http://localhost/", headers={"User-Agent": "haha-bot", "Accept": "*/*"}, timeout=(1, 1))

    print(response.status_code)
    print(type(response.content))
    print(response.request.headers)
    #print(response.text)
    print(response.headers)
    try:
        print(response.json())
    except ValueError:
        print("JSON yanıtı alınamadı.")