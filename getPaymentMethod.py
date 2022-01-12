import json
import httplib2

BASE_URL = "https://api.redislabs.com/v1"
LOGS = "/payment-methods"
API_KEY = "Armjlu9edjsq139bw4vz628sm5z0wc1isj8pkr91px5pukazxn"
API_SECRET = "S37o6oncstl6r4ccvio1jho58nxcfncpaum6vcstqj4v0bdbu5w"

http = httplib2.Http()
headers = {
    'x-api-key': API_KEY,
    'x-api-secret-key': API_SECRET
}
response, content = http.request(BASE_URL + LOGS, method="GET", headers=headers)
content = json.loads(content.decode("utf-8"))

print("================= RESPONSE =================")
print(response)
print("================= CONTENT =================")
print(content)