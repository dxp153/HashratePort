from common.get_keyword import GetKeyword
from interface.staff import Staff
from common.read_xlsx import ExcelUtil
import os
import json
import pytest
import allure


@allure.epic("导入员工列表接口测试")
@pytest.mark.usefixtures("login_cooking")
class Test_import_stall:

    def test_import_stall_01(self, login_cooking):

        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(propath, "data", "ygdr.xlsx")
        data = ExcelUtil(str.lower(filepath))
        datas = data.dict_data()
        n = len(datas)
        x = 0
        jsons = []
        while x <= n-1:

            values = list(datas[int("%s" % x)].values())
            importData = ["name", "phone", "sex", "zjType", "zjNum", "jobType", "syq", "rzTime", ]
            d = dict(zip(importData, values))
            sex = {"男": 0, "女": 1}
            if d["sex"] in sex.keys():
                d["sex"] = sex["%s" % d["sex"]]
            else:
                print("性别错误")
            syq = {"无试用期": 0, "1个月": 1, "2个月": 2, "3个月": 3, "4个月": 4, "5个月": 5, "6个月": 6}
            if d["syq"] in syq.keys():
                d["syq"] = syq["%s" % d["syq"]]
            else:
                print("试用期错误")
            zjType = {"身份证": 0, "港澳居民来往内地通行证": 1, "台湾居民来往大陆通行证": 2, "外国护照": 3, "其他": 4}
            if d["zjType"] in zjType.keys():
                d["zjType"] = zjType["%s" % d["zjType"]]
            else:
                print("证件类型错误")
            jobType = {"全职": 0, "实习生": 1, "兼职": 2, "劳务派遣": 3, "劳务": 4, "派遣": 5, "外包": 6, "退休返聘": 7}
            if d["jobType"] in jobType.keys():
                d["jobType"] = jobType["%s" % d["jobType"]]
            else:
                print("工作类型错误")
            x += 1
            jsons.append(d)
        response = Staff().import_staff(json=jsons, headers=login_cooking[0][1])
        print(response.text)
        code = GetKeyword.json_path(json.loads(response.text), "$.code")
        message = GetKeyword().json_path(json.loads(response.text), "$.message")
        try:
            assert (code[0] == "200")
            assert (message[0] == "导入员工档案成功!")
            print("test_add_stall_01 测试通过")
        except AssertionError:
            print("test_add_stall_01 断言失败")
            print(message)
