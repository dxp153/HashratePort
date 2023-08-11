import requests
import json


#   封装接口请求方式
class Send_Method:

    @staticmethod
    def send_method(method, url, data=None, headers=None):
        if method == "get" or method == "delete":
            response = requests.request(method=method, url=url, data=data, headers=headers)
            return response
        elif method == "post" or method == "put":
            response = requests.request(method=method, url=url, data=data, headers=headers)
            return response
        elif method == "delete":
            response = requests.request(method=method, url=url, data=data, headers=headers)
            return response
        else:
            print("请求方式错误，请确认请求方式是否与预期一致")
            response = None
            return response

        # if method == "delete":
        #     return response.status_code  # 返回响应状态码
        # else:
        #     return response.json()  # 返回json参数

    @staticmethod
    def format_response(response):
        #   格式化response
        return json.dumps(response, indent=2, ensure_ascii=False)

    @staticmethod
    def gain_cookies(url, data=None):
        #   获取cookies的值
        response = requests.post(url=url, json=data)
        for c in response.cookies:
            cookies = c.value
            # print(cookies)
            return cookies
