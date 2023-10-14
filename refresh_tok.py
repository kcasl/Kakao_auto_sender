import requests
import json

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "refresh_token",
    "client_id"  : "9a5a0c59cbeafab3b4993b5e446d92c3",
    "refresh_token" : "C_MAzGRb6XNuIZzy4_2ggIBwTi7hN8XmteIqGOg8Cj1z7AAAAYsP3jy0"
}
response = requests.post(url, data=data)

print(response.json())