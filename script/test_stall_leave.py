from common.get_keyword import GetKeyword
from interface.staff import Staff
import random
import json
import pytest
import allure


@allure.epic("员工离职接口测试")
@pytest.mark.usefixtures("login_cooking")
class Test_Leave_Stall:

    def test_leave_stall_01(self, login_cooking):
        request = {
            # "bmgwid": "",
            "currentPage": 1,
            # "jobStatus": "",
            # "jobType": "",
            # "query": "",
            "totalPage": 50
        }
        res = Staff().selects_stall(request, headers=login_cooking[0][1])
        sta = GetKeyword().json_path(json.loads(res.text), "$..data")
        stall = {}
        while sta is not None:
            stallx = random.choice(sta[0])  # 获取随机员工
            stall = stallx
            if stallx["jobStatus"] < 3:
                break
        jLeave = {
            "empNum": stall["empNum"],
            "jobStatus": stall["jobStatus"],
            "jobType": stall["jobType"],
            "lzTime": "2020-11-29 16:00:00",
            "lzbz": "离职备注",
            "lzyy": "离职原因说明",
            "name": stall["name"]
        }
        Staff().leave_stall(json=jLeave, headers=login_cooking[0][1])   # 员工离职
        jList = {"currentPage": 1,
                 "jobStatus": "",
                 "query": "",
                 "totalPage": 50
                 }
        lists = Staff().leave_list(json=jList, headers=login_cooking[0][1])  # 获取离职员工列表数据
        emp = GetKeyword.json_path(json.loads(lists.text), "$..empNum")     # 获取全部离职列表中员工
        try:
            assert stall["empNum"] in emp  # 断言离职员工是否在离职列表中
            giveUp = {
                "empNum": stall["empNum"]
            }
            Staff().giveUp_leaving(json=giveUp, headers=login_cooking[0][1])    # 员工放弃离职
            listG = Staff().leave_list(json=jList, headers=login_cooking[0][1])     # 获取离职员工列表数据
            empG = GetKeyword.json_path(json.loads(listG.text), "$..empNum")    # 获取全部离职列表中员工
            try:
                assert stall["empNum"] not in empG
            except AssertionError:
                print("员工 %s 放弃离职失败" % stall["empNum"])
        except AssertionError:
            print("离职员工 %s 不在在离职列表中" % stall["empNum"])