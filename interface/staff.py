from common.get_keyword import GetKeyword
from common.send_method import Send_Method
from common.login_cooking import Cooking
import allure
import json


@allure.step("员工管理")
class Staff:

    def __init__(self):
        self.AddStaff = "http://test-8timer-api.youlingrc.com/yggl/addygda"
        self.RegularStall = "http://test-8timer-api.youlingrc.com/yggl/ygzz"
        self.QueryStall = "http://test-8timer-api.youlingrc.com/yggl/ygquery"
        self.SelectStall = "http://test-8timer-api.youlingrc.com/yggl/selects_emp"
        self.ImportStaff = "http://test-8timer-api.youlingrc.com/yggl/import_emp_record"
        self.LeaveStall = "http://test-8timer-api.youlingrc.com/yggl/addlzjh"
        self.AffirmLeaveStall = "http://test-8timer-api.youlingrc.com/yggl/qrlz"
        self.LeaveList = "http://test-8timer-api.youlingrc.com/yggl/querylzyg"
        self.GiveUp_Leaving = "http://test-8timer-api.youlingrc.com/yggl/fqlz"
        self.QueryEmp = "http://test-8timer-api.youlingrc.com/yggl/queryemp"

    def query_emp(self, headers):
        """
        查询员工列表
        :return:
        """
        response = Send_Method.send_method(method="get", url=self.QueryEmp, headers=headers)
        return response

    def add_staff(self, json, headers):
        """
        添加员工
        :param json:  {"attgroupid": 0,            # 考勤组id
                        "bmgwId": 0,                # 部门岗位id
                        "currentPage": 0,           # 自定义工号
                        "customNum": 0,             # 自定义工号
                        "jobType": 2,               # 工作性质 0全职、1实习生、2兼职、3劳务派遣、4劳务、5派遣、6外包、7退休返聘
                        "name": "邵华",              # 员工姓名
                        "phone": "15469875698",     # 手机号
                        "rzTime": "2020-11-01",     # 入职日期
                        "sex": 1,                   # 性别 0：男；1：女
                        "syq": 3,                   # 试用期 0:无试用期;1:1个月;2:2个月;3:3个月;4:4个月;5:5个月;6:6个月（有试用期显示选项）
                        "zjNum": "xxxxxxxx",        # 证件号码
                        "zjType": 4                 # 证件类型 0:身份证;1:港澳居民来往内地通行证;2:台湾居民来往大陆通行证;3:外国护照;4:其他
                        }
        :param headers: 登录的cooking
        :return:
        """

        response = Send_Method.send_method(method="post", url=self.AddStaff, data=json, headers=headers)
        return response

    def import_staff(self, json, headers):
        """
        员工导入
        :param json: [
                        {

                            "jobType": 0,                 # 工作性质 0全职、1实习生、2兼职、3劳务派遣、4劳务、5派遣、6外包、7退休返聘
                            "name": "华仔",                # 员工姓名
                            "phone": "101",                # 手机号
                            "rzTime": "",                   # 入职日期
                            "sex": 0,                       # 性别 0：男；1：女
                            "syq": 0,                       # 试用期 0:无试用期;1:1个月;2:2个月;3:3个月;4:4个月;5:5个月;6:6个月（有试用期显示选项）
                            "zjNum": "证件号码",             # 证件号码
                            "zjType": 0                     # 证件类型 0:身份证;1:港澳居民来往内地通行证;2:台湾居民来往大陆通行证;3:外国护照;4:其他
                        }
                    ]
        :param headers: 登录的cooking
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.ImportStaff, data=json, headers=headers)
        return response

    def query_stall(self, json, headers):
        """
        员工查询
        :param json:{   "bmgwid": 101,                  #   部门id
                        "bz": "123",                    #   备注
                        "deptName": "1",                #   部门名
                        "empName": "华仔",                #   员工姓名
                        "empNum": 1,                    #   员工号
                        "headUrl": "url",               #   头像url
                        "jobStatus": 2,                 #   员工状态    1正式、2试用、3离职中、4已离职
                        "jobType": 1,                   #   工作性质    1全职、2实习生、3兼职、4劳务派遣、5劳务、6派遣、7外包、8退休返聘
                        "lzyy": "123",                  #   离职原因
                        "phone": "1",                   #   手机号
                        "query": "1388888888 or 张三",    #   手机号、姓名
                        "rzTime": "1",                  #   入职时间
                        "sex": 1,                       #   性别
                        "upName": "1",                  #   上级部门名
                        "ylzTime": "1"                  #   应离职时间
                        }
        :param headers:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.QueryStall, data=json, headers=headers)
        return response

    def selects_stall(self, json, headers):
        """
        员工列表
        :param json: {
                        bmgwid: ""          #   部门岗位ID
                        currentPage: 2      #  当前第几页
                        jobStatus: ""       #  员工状态3离职中、4已离职
                        jobType: ""         #   工作性质1全职、2实习生、3兼职、4劳务派遣、5劳务、6派遣、7外包、8退休返聘
                        query: ""           #   员工名称 / 手机号
                        totalPage: 10       #   当前页员工数
                        }
        :param headers:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.SelectStall, data=json, headers=headers)
        return response

    def regular_stall(self, json, headers):
        """
        员工转正
        :param json: {  "empNum": 9527,             # 工号
                        "orgCode": 12,              # 企业id
                        "sjzzTime": "2019-12-03",   # 实际转正时间
                        "zzRemark": "有梦想",        # 转正原因
                        "zzTime": "1999-12-03"      # 应转正时间
                      }
        :param headers:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.RegularStall, data=json, headers=headers)
        return response

    def leave_stall(self, json, headers):
        """
        员工离职
        :param json:{
                        empNum: 10003                           # 员工工号
                        jobStatus: 1                            # 员工状态1试用、2正式、3离职中、4已离职
                        jobType: 0                              # 工作性质1全职、2实习生、3兼职、4劳务派遣、5劳务、6派遣、7外包、8退休返聘
                        lzTime: "2020-11-29T16:00:00.000Z"      # 应离职时间
                        lzbz: "离职备注"                          # 离职备注
                        lzyy: "离职原因说明"                       # 离职原因说明
                        name: "李小叶"                            # 员工姓名
                    }
        :param headers:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.LeaveStall, data=json, headers=headers)
        return response

    def leave_list(self, json, headers):
        """
        离职员工列表查询
        :param json: {  currentPage: 2      #  当前第几页
                        jobStatus: ""       #  员工状态3离职中、4已离职
                        query: ""           #   员工名称 / 手机号
                        totalPage: 10       #   当前页员工数
                        }
        :param headers:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.LeaveList, data=json, headers=headers)
        return response

    def giveUp_leaving(self, json, headers):
        """
        员工放弃离职
        :param json:{
                     empNum:10003               # 员工工号
                        }
        :param headers:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.GiveUp_Leaving, data=json, headers=headers)
        return response

    def affirm_leave_stall(self, json, headers):
        """
        确认员工离职
        :param json:{
                    empNum: 10009       # 员工编号
                    }
        :param headers:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.AffirmLeaveStall, data=json, headers=headers)
        return response


if __name__ == "__main__":
    login = {
        "phone": "15797629873",
        "pw": "123456"
    }
    c = Cooking.login_cooking(login)[1]
    print(c)
    a = Staff()
    r = a.query_emp(headers=c)
    print(r.text)
