from common.login_cooking import Token
from common.send_method import Send_Method
import allure
import json


@allure.step("切换企业")
class SwitchCompanies:
    #   测试公司     1：云商互联    3:广东优领科技服务有限公司
    def switch_companies(self, parameter, headers):
        """

        :param parameter: 公司id
        :param headers: cooking
        :return:
        """
        url = "http://test-8timer-api.youlingrc.com/qyzx/changeent"
        if isinstance(parameter, int):
            url = url + "/%s" % parameter
            response = Send_Method.send_method(method="get", url=url, headers=headers)
            return response, parameter
        else:
            print("输入格式错误，请输入企业编号")


if __name__ == "__main__":
    data = {
        "phone": "15797629873",
        "pw": "123456"
    }
    c = Cooking()
    tt = Cooking.login_cooking(data)
    t = tt[0].text
    cc = tt[1]
    s = SwitchCompanies().switch_companies(parameter=3, headers=cc)
    print(s.text)
