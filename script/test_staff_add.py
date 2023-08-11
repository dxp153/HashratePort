from common.get_keyword import GetKeyword
from interface.staff import Staff
import json
import pytest
import allure

data = {
    "attgroupid": 0,  # 考勤组id
    "bmgwId": 0,  # 部门岗位id
    "currentPage": 0,  # 自定义工号
    "customNum": 0,  # 自定义工号
    "jobType": 2,  # 工作性质 0全职、1实习生、2兼职、3劳务派遣、4劳务、5派遣、6外包、7退休返聘
    "name": "邵邵华",  # 员工姓名
    "phone": "15469875679",  # 手机号
    "rzTime": "2020-11-01",  # 入职日期
    "sex": 1,  # 性别 0：男；1：女
    "syq": 3,  # 试用期 0:无试用期;1:1个月;2:2个月;3:3个月;4:4个月;5:5个月;6:6个月（有试用期显示选项）
    "zjNum": "xxxxxxxx",  # 证件号码
    "zjType": 4  # 证件类型 0:身份证;1:港澳居民来往内地通行证;2:台湾居民来往大陆通行证;3:外国护照;4:其他
}


@allure.epic("添加员工接口测试")
@pytest.mark.usefixtures("login_cooking")
class Test_add_stall:
    """
    添加员工接口测试
    """
    def test_add_stall_01(self, login_cooking):
        """
        正常添加企业中不存在的员工
        :param login_cooking: 获取登录返回参数
        :return:
        """
        s = Staff().add_staff(json=data, headers=login_cooking[0][1])
        code = GetKeyword.json_path(json.loads(s.text), "$.code")
        message = GetKeyword().json_path(json.loads(s.text), "$.message")
        try:
            assert (code[0] == "200")
            print("test_add_stall_01 测试通过")
        except AssertionError:
            print("test_add_stall_01 断言失败")
            print(message)

