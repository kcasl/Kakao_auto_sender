import requests
import json

# 카카오톡 메시지 API
# url = "https://kauth.kakao.com/oauth/token"
# data = {
#     "grant_type": "refresh_token",
#     "client_id": "9a5a0c59cbeafab3b4993b5e446d92c3",
#     "refresh_token": "QRuCzg2UW8Du7GZ35yxK4XkFRr2NSFahLYUJ7lmyCj1ymAAAAYsQBAYI"
# }
# response = requests.post(url, data=data)
# tokens = response.json()
# # kakao_code.json 파일 저장
# with open("kakao_code.json", "w") as fp:
#     json.dump(tokens, fp)
    
# # 카카오 API 엑세스 토큰
# with open("kakao_code.json", "r") as fp:
#     tokens = json.load(fp)    
# print(tokens["access_token"])
    
# url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
# header = {"Authorization": 'Bearer ' + tokens["access_token"]}
# result = json.loads(requests.get(url, headers=header).text)
# friends_list = result.get("elements")
# print(friends_list)   
     

# print(friends_list)

# url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
# headers = {
#     "Authorization": "Bearer " + "{U9yCk6Zbprabc_poNGX8eWRPzK1P8UpJcjZEPjrtCj1ymAAAAYsQBAYJ}",

# }
# data={
#     'receiver_uuids': '["{}"]'.format(friend_id),
#     "template_object": json.dumps({
#         "object_type":"text",
#         "text":"test001\n죽창\n죽창(竹槍, bamboo spear)또는 대나무창은 대나무를 깎아 만든 창이다. 죽창은 대나무를 적당한 길이로 자른 다음, 끝부분을 비스듬히 깎거나 또는 그 둘레 일부를 가시돋치게 곤두세워서 만들며, 불에 쬐는 정도로 단단하게 경화 처리할 수 있는 간이 무기이다.",
#         "link":{
#             "web_url" : "https://www.google.co.kr/search?q=죽창",
#             "mobile_web_url" : "https://www.google.co.kr/search?q=죽창"
#         },
#         "button_title": "링크 열기"
#     })
# }
# response = requests.post(url, headers=headers, data=data)
# if response.json().get('result_code') == 0:
#     print('메시지를 성공적으로 보냈습니다.')
# else:
#     print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

with open("kakao_token.json","r") as fp:
    tokens = json.load(fp)

# print(tokens)
# print(tokens["access_token"])

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

# GET /v1/api/talk/friends HTTP/1.1
# Host: kapi.kakao.com
# Authorization: Bearer {ACCESS_TOKEN}

headers={"Authorization" : "Bearer " + tokens["access_token"]}

result = json.loads(requests.get(friend_url, headers=headers).text)

print(type(result))
print("=============================================")
print(result)
print("=============================================")
friends_list = result.get("elements")
print(friends_list)
# print(type(friends_list))
print("=============================================")
print(friends_list[0].get("uuid"))
friend_id = friends_list[0].get("uuid")
print(friend_id)