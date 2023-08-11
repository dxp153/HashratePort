from interface.login import Login
import requests
import json
from common.get_keyword import GetKeyword


class Token:
    # 获取登录的Token

    @staticmethod
    def login_cooking(base_url, data, header):
        response = Login(base_url).login(data, header=header)
        token = GetKeyword().json_path(json.loads(response.text), "$.access_token")
        return response, token

        # for token in response.cookies:
        #     cookies = {'Cookie': 'JSESSIONID=%s' % token.value}
        #     # print("cookies == %s" % cookies)
        #     return response, cookies


if __name__ == "__main__":
    data = {
        "username": "15797629873",
        "password": "dddd1234",
        "grant_type": "password",
        "captcha": 123
    }
    headers = {
        "Content-Length": "71",
        "Host": "183.240.23.97",
        "Authorization": "Basic eXVuc2h1b2lvOnl1bnNodW9pbw==",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    token = Token()
    c = token.login_cooking(data,headers)
    print(c)
