import requests
import json

url = 'https://eifvcd.deta.dev/'
data = {
    'x': 3,
    'y': 4
}

def main():
    res = requests.post(url, json.dumps(data))
    print(res.json())

if __name__ == '__main__':
    main()

# リクエスト
# curl --request GET \
#                      --url https://eifvcd.deta.dev/ \
#                      --header 'Content-Type: application/json' \
#                      --header 'X-API-Key:ここにapikey'
