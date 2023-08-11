from common.login_cooking import Cooking
from common.send_method import Send_Method
from common.get_keyword import GetKeyword
from common.value_replace import Value_Replace
import allure
import random
import requests
import json
import ast


@allure.step("获取员工上级主管")
class Competent:

    def __init__(self):
        self.url = "http://test-8timer-api.youlingrc.com/yggl/loginerChargers"

    def competent(self, headers):
        """
        获取员工上级主管
        :param headers:
        :return:
        """
        response = Send_Method.send_method(method="get", url=self.url, headers=headers)
        return response

