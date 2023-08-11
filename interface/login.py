from common.send_method import Send_Method
from common.get_keyword import GetKeyword
import requests
import json


#   用户登录
class Login:

    def __init__(self, method="post"):
        self.method = method
        self.url = "http://183.240.23.97/api/auth/oauth/token"

    def login(self, data, header):
        response = Send_Method.send_method(self.method, self.url, data=data, headers=header)
        # print("Login response == %s" % response)
        return response

    def login_json(self, data, header):
        """
        获取接口返回参数
        :param data: 输入的账号密码，json格式
        :param parameter: 要获取的值
        :return:
        """
        requests = self.login(data, header)
        return requests


if __name__ == "__main__":
    d = {
        "username":"15797629873",
        "password":"ddd123456",
        "grant_type":"password",
        "captcha":123
    }
    headers = {
        "Content-Length": "71",
        "Host": "183.240.23.97",
        "Authorization": "Basic eXVuc2h1b2lvOnl1bnNodW9pbw==",
        "Content-Type": "application/x-www-form-urlencoded"
            }
    header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN",
        "Authorization": "Basic eXVuc2h1b2lvOnl1bnNodW9pbw==",
        "Connection": "keep-alive",
        "Content-Length": "71",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "183.240.23.97",
        "Origin": "http://183.240.23.97",
        "Referer": "http://183.240.23.97/computing-market-user-web/",
        "Request-Start": "1691398608221",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "tenantCode": "",
        "Cookie": '_xsrf=2|56fe217e|e5545a034accad735b2c7d0cc738b13b|1689322827; username-183-240-23-97-25042="2|1:0|10:1689668504|28:username-183-240-23-97-25042|44:NjRmNWFkZDczOGM2NDZkYWJhOTU4MjZjOTYwOTQ1YTM=|f653c574de73aeefbf03f2270987423881259e1b4179ea421067b23c5b51e385"; username-183-240-23-97-25023="2|1:0|10:1690164971|28:username-183-240-23-97-25023|44:NGRjNmFjZDE3NjkxNDkwNWIwYzc1MWY2YTE1NzYwMDE=|78a5567369f4fa857acbcf4892cfa6fadfc58d981cb296b4a8e758f9e5f5b414"; username-183-240-23-97-25031="2|1:0|10:1690272695|28:username-183-240-23-97-25031|44:ZWU2MzMxZGU2YmVlNGMyMTljMDRmMWJhZTRmODViYTk=|7cbfe85c6bf07f2a3c94a88e3a5d22e42c1973410e2442304afb4f54169a946c"; username-183-240-23-97-25047="2|1:0|10:1690359467|28:username-183-240-23-97-25047|44:MzFjYzYzMzRkNTU3NDUxNTgxODg4OTUwNjY2ZjhmMzA=|08af76ff6510bb181469ed9fe5ea12eaf3997d8b61ceb958d12debc3061161a9"; username-183-240-23-97-25053="2|1:0|10:1690535132|28:username-183-240-23-97-25053|192:eyJ1c2VybmFtZSI6ICI3M2VmNzczNmU1NGI0NDY3ODUxMzZmZTkxNDI2NmU4NiIsICJuYW1lIjogIkFub255bW91cyBUaGViZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIFRoZWJlIiwgImluaXRpYWxzIjogIkFUIiwgImNvbG9yIjogbnVsbH0=|01da07736f3134306f957a58fcb6add42e1ab034d3175234d2ad35f9b5010624"; username-183-240-23-97-25036="2|1:0|10:1690538781|28:username-183-240-23-97-25036|200:eyJ1c2VybmFtZSI6ICI0NGExMjBiZmYxODY0YWRlOTE4ZTEzM2IyNGViOTM5NiIsICJuYW1lIjogIkFub255bW91cyBMeXNpdGhlYSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEx5c2l0aGVhIiwgImluaXRpYWxzIjogIkFMIiwgImNvbG9yIjogbnVsbH0=|f5fa2c279b581078bd7b2da4dc5a71a9c3982679ba06bb72fedc4fe80098beba"; username-183-240-23-97-25032="2|1:0|10:1690538792|28:username-183-240-23-97-25032|192:eyJ1c2VybmFtZSI6ICJmZGJmMTA2MTA0Mzg0OTA2ODcyNWYwZmIyY2Y2N2RjMCIsICJuYW1lIjogIkFub255bW91cyBBb2VkZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFvZWRlIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|f8ef8868e2f4bfeb8b5a8fab802ff03e611edb9da17ec057d9e57b5d2f4af92e"',
    }
    login = Login()
    print(login.login_json(data=d, header=headers).text)
    print(requests.post(url="http://183.240.23.97/api/auth/oauth/token",data=d,headers=headers).text)
    print(requests.request(method="post",url="http://183.240.23.97/api/auth/oauth/token",data=d,headers=headers).text)