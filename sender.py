import requests
import json

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + "{U9yCk6Zbprabc_poNGX8eWRPzK1P8UpJcjZEPjrtCj1ymAAAAYsQBAYJ}",

}
data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"test001\n히히\n줄 채우기",
        "link":{
            "web_url" : "https://www.google.co.kr/search?q=죽창",
            "mobile_web_url" : "https://www.google.co.kr/search?q=죽창"
        },
        "button_title": "링크 열기"
    })
}
response = requests.post(url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))