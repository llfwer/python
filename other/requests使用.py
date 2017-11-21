import requests

response = requests.get("https://www.baidu.com")
print('response类型 : ', type(response))
print('返回码 : ', response.status_code)
print('text类型 : ', type(response.text))
print('text : ', response.text)
print('cookies : ', response.cookies)
print('content : ', response.content)
print('content.decode("utf-8") : ', response.content.decode("utf-8"))
