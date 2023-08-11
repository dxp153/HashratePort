from common.get_keyword import GetKeyword
from interface.attendance_group_setting import AttGroupSetting
from interface.staff import Staff
import json
import pytest
import allure


@allure.epic("新增考勤组接口")
@pytest.mark.usefixtures("login_cooking")
class Test_attendance_add:

    def test_att_add_01(self, login_cooking):
        JSESSIONID = login_cooking[0][1]
        shift = AttGroupSetting().shift_data_list(jsons={"currentPage": 1, "total": 1, "totalPage": 50},
                                                  header=JSESSIONID)
        bc_id = GetKeyword.json_path(json.loads(shift.text), "$..id")  # 获取当前企业的所有班次id
        address = AttGroupSetting().punch_address(header=JSESSIONID)
        kq_address = GetKeyword.json_path(json.loads(address.text), "$..id")  # 获取当前企业的所有打卡地址的id
        wifi = AttGroupSetting().punch_wifi(header=JSESSIONID)
        kq_wifi = GetKeyword.json_path(json.loads(wifi.text), "$..id")  # 获取当前企业的所有打卡wifi的id
        machine = AttGroupSetting().group_machine(header=JSESSIONID)
        kq_machine = GetKeyword.json_path(json.loads(machine.text), "$..id")  # 获取当前企业的所有考勤机的id
        staff = Staff().query_emp(headers=JSESSIONID)
        staff_id = GetKeyword.json_path(json.loads(staff.text), "$..empNum")  # 获取当前企业的所有员工id
        jsons = {
            "attWeekdays": [1, 2, 3, 4, 5, 6],  # 一周打卡日期
            "attWeekdaysShifts": [bc_id[0], bc_id[0], bc_id[0], bc_id[0], bc_id[0], bc_id[0]],  # 每日对应的打卡日期
            "attadds": kq_address,  # 考勤地址
            "attmachines": kq_machine,  # 考勤机编号
            "atttype": 1,   # 考勤组类型
            "attuserids": staff_id[:5],  # 考勤组内成员id
            "attwifis": kq_wifi,     # 考勤WiFi
            "fieldpersonnel": 1,    # 外勤
            "name": "测试测试考勤组",  # 考勤组名称
            "legalholidays": 0,
            "optscheduling": 0,
            "overtimeRulesId": 1,   # 加班规则id
            "restdayclock": 0,   # 休息日打卡
        }
        print(json.dumps(jsons))
        x = AttGroupSetting().attendance_group(jsons=jsons, header=JSESSIONID)
        print(x.text)

