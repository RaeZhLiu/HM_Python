import requests

url = "https://www.google.com.hk/search"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"}
paras = {"q": "python"}

# 在请求头中添加user-agent，模拟浏览器发送请求
response = requests.get(url, headers=headers, params=paras)

# response.content.decode() 默认为 utf8 编码
print(response.content.decode())
print(response.request.headers)
print(response.url)
print(len(response.content.decode()))
