import json
import httplib2
import urllib

BASE_URL = "https://api.redislabs.com/v1"
SUBSCRIPTIONS = "/subscriptions"
API_KEY = "Armjlu9edjsq139bw4vz628sm5z0wc1isj8pkr91px5pukazxn"
API_SECRET = "S37o6oncstl6r4ccvio1jho58nxcfncpaum6vcstqj4v0bdbu5w"

SUB_DATA = {
    "name": "MGILLESPIE-ex4",
    "paymentMethodId": 9605,
    "cloudProviders": [
      {
        "cloudAccountId": 1, # 6415
        "regions": [
          {
            "region": "us-east-1",
            "networking": {
              "deploymentCIDR": "10.10.1.0/24"
            }
          }
        ]
      }
    ],
    "databases": [
      {
        "name": "cool-db-1",
        "memoryLimitInGb": 1.0
      }
    ]
}

http = httplib2.Http()
headers = {
    'x-api-key': API_KEY,
    'x-api-secret-key': API_SECRET
}
response, content = http.request(BASE_URL + SUBSCRIPTIONS, method="POST", headers=headers, body=json.dumps(SUB_DATA))
# content = json.loads(content.decode("utf-8"))

print("================= RESPONSE =================")
print(response)
print("================= CONTENT =================")
print(content)