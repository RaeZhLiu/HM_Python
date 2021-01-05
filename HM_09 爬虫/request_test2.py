import requests


if __name__ == '__main__':
    r1 = requests.get("https://api.github.com/events")
    # r = requests.post("http://httpbin.org/post", data={"key":"value"})
    payload = {"q": "python"}
    header = {"user-agent": "user-agent: Mozilla/5.0 \
        (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/87.0.4280.67 Safari/537.36"}
    r = requests.get("https://www.google.com.hk/search", headers=header, params=payload)

    print(r.url)

    print(r1.text)
    print(r1.content)
    print(r.content.decode())
    print(r.request.headers)
    print(r.headers)
