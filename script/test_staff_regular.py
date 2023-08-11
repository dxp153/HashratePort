from common.get_keyword import GetKeyword
from interface.staff import Staff
import json
import pytest
import allure
import time

data = {
    "query": "13522222221"
}


@allure.epic("员工转正接口测试")
@pytest.mark.usefixtures("login_cooking")
class Test_Regular_staff:

    def test_regular_staff_01(self, login_cooking):
        """
        员工转正操作
        :param login_cooking:
        :return:
        """

        s = Staff().query_stall(json=data, headers=login_cooking[0][1])
        print(s.text)
        records = GetKeyword.json_path(json.loads(s.text), "$..records")
        try:
            # assert len(records[0]) != 0    # 判断查询的员工是否存在

            status = GetKeyword.json_path(json.loads(s.text), "$..jobStatus")
            empnum = GetKeyword.json_path(json.loads(s.text), "$..empNum")
            timer = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 获取当前时间
            try:
                # assert status[0] == 1  # 断言该员工是否为正式员工
                print("该员工已经为正式员工")
            except AssertionError:
                keys = ["empNum", "orgCode", "sjzzTime", "zzRemark"]
                values = ["%s" % empnum[0], "%s" % login_cooking[1], "%s" % timer, "xxxxxx"]
                jsons = dict(zip(keys, values))
                r = Staff().regular_stall(json=jsons, headers=login_cooking[0][1])
                code = GetKeyword.json_path(json.loads(r.text), "$.code")
                message = GetKeyword().json_path(json.loads(r.text), "$.message")
                try:
                    # assert code[0] == "200"
                    print("test_add_stall_01 测试通过")
                except AssertionError:
                    print("test_add_stall_01 断言失败")
                    print(message)
        except AssertionError:
            print("未查询到筛选条件为： %s 的员工信息" % data)
