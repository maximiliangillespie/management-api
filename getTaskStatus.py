import json
import httplib2

BASE_URL = "https://api.redislabs.com/v1"
TASKS = "/tasks/"
API_KEY = "Armjlu9edjsq139bw4vz628sm5z0wc1isj8pkr91px5pukazxn"
API_SECRET = "S37o6oncstl6r4ccvio1jho58nxcfncpaum6vcstqj4v0bdbu5w"

http = httplib2.Http()
headers = {
    'x-api-key': API_KEY,
    'x-api-secret-key': API_SECRET
}
task_id = "e30f8575-3e2c-455d-8458-b6f31219dab5"
response, content = http.request(BASE_URL + TASKS + task_id, method="GET", headers=headers)
content = json.loads(content.decode("utf-8"))

print("================= RESPONSE =================")
print(response)
print("================= CONTENT =================")
print(content)