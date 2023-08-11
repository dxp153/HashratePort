from common.get_keyword import GetKeyword
from interface.attendance_group_setting import AttGroupSetting
import json
from common.read_xlsx import ExcelUtil
import os
import pytest
import allure


@allure.epic("新增班次接口测试")
@pytest.mark.usefixtures("login_cooking")
class Test_shift_setting:

    def test_shift_setting_01(self, login_cooking):
        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(propath, "data", "新增班次.xlsx")
        data = ExcelUtil(str.lower(filepath)).dict_data()
        n = len(data)
        x = 0
        while n == x + 1:
            jsons = data[x]
            #   新增班次
            response = AttGroupSetting().shift_setting(jsons=jsons, header=login_cooking[0][1])
            # print(response.text)
            x += 1
        #   查询该班次
        j = {
            "currentPage": 1,
            "total": 1,
            "totalPage": 50
        }
        r = AttGroupSetting().shift_data_list(jsons=j, header=login_cooking[0][1])
        # print(r.text)
        #   获取公司所有班次信息
        pages = GetKeyword.json_path(json.loads(r.text), "$..name")
        page = pages[0]
        #   删除测试班次
        while page in pages:
            s = 0
            xx = len(pages)
            while s < xx:
                l = pages[s]
                if l != "测试测试": break
                ls = GetKeyword.json_path(json.loads(r.text), "$..id")
                i = ls[s]
                res = AttGroupSetting().delete_shift(number=i, header=login_cooking[0][1])
                s += 1
            print(pages[s])
            break

