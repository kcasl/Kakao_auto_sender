import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "db5ff0cf50d61cb7a4057b9cc5c91f7e",
    "redirect_uri" : "https://localhost:3000",
    "code"         : "5biqN3HLGZ3AcTJYn01ExwLxVJ5bCzp3t0MWPnbhvcJsoQurezN7dktQVJQK3urQTHTaFAoqJY8AAAGLHRqrcA"
    
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)

with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp)