import requests

url = "http://www.baidu.com"

response = requests.get(url)

# response.text = response.content.decode("程序预测的编码")
# response.encoding = "utf8"
# print(response.text)

# response.content.decode() 默认为 utf8 编码
# print(response.content.decode())

print(response.url)
print(response.request.headers)
print(response.headers)
print(response.cookies)

