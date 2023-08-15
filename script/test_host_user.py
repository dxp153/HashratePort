from interface.host_list import Host_List
from common.get_keyword import GetKeyword
import traceback
import json
import pytest
import allure
from common.yaml_translation import yamlUtil


@allure.epic("主机列表接口")
@pytest.mark.usefixtures("login_token")
class Test_Host_List:
    """
    接口登录用例
    """

    @allure.story("主机列表查询")
    @pytest.mark.parametrize('para', yamlUtil("../data/host_list.yml").read_yaml())
    def test_host_list_filtrate(self, login_token, base_url,  para):
        """
        用户登录
        :return:
        """
        print(login_token)
        i = 0
        with allure.step(para[i]['case']):
            url_prar = para[i]['input']['url']
            headers = para[i]['input']['headers']
            print(login_token[0])
            headers['Authorization'] = 'Bearer ' + login_token[0][0]
            code1 = para[i]['input']['code']
            msg1 = para[i]['input']['msg']
            i += 1
            response = Host_List(base_url).filtrate_host_list(url_prar, headers)
            t = response.text
            code = GetKeyword().json_path(json.loads(t), "$.code")
            msg = GetKeyword().json_path(json.loads(t), "$.msg")
            if msg:
                assert (code[0] == code1)
                assert (msg[0] == msg1)
                print("测试通过 code==%s,%s" % (code, msg))



                # try:
                #     assert (code[0] == code1)
                #     assert (msg[0] == msg1)
                # except AssertionError:
                #     print("test_host_list_filtrate 断言失败")
                #     print("code == %s" % code)
                #     traceback.print_exc()
                # else:
                #     print("测试通过 code==%s,%s" % (code, msg))