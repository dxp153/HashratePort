from common.send_method import Send_Method
from common.login_cooking import Cooking
from common.get_keyword import GetKeyword
import allure
import json


@allure.step("考勤组设置")
class AttGroupSetting:

    def __init__(self):
        self.ShiftSetting = "http://test-8timer-api.youlingrc.com/kqmk/Shif"
        self.ShiftDataList = "http://test-8timer-api.youlingrc.com/kqmk/ShiftDataList"
        self.DeleteShift = "http://test-8timer-api.youlingrc.com/kqmk/Shif"
        self.PunchAddress = "http://test-8timer-api.youlingrc.com/kqmk/InGroupPunchAddress"
        self.PunchWiFi = "http://test-8timer-api.youlingrc.com/kqmk/InGroupPunchWIFI"
        self.GroupMachine = "http://test-8timer-api.youlingrc.com/kqmk/AttGroupMachine"
        self.AttGroupList = "http://test-8timer-api.youlingrc.com/kqz/AttGroupList"
        self.AttendanceGroup = "http://test-8timer-api.youlingrc.com/kqmk/AttendanceGroup"

    def shift_setting(self, jsons, header):
        """
        新增班次信息接口
        :param jsons:{  "beiz": "备注",
                        "endTime": "休息结束时间 休息结束时间",
                        "id": 101,
                        "isSbdk1Cr": 	上班1是否次日（0：否；1：是） 上班1是否次日（0：否；1：是）,
                        "isSbdk2Cr":    上班2是否次日（0：否；1：是） 上班2是否次日（0：否；1：是,
                        "isSbdk3Cr":    上班3是否次日（0：否；1：是） 上班3是否次日（0：否；1：是,
                        "isWzwd":       是否开启晚走晚到(0：否；1：是) 是否开启晚走晚到(0：否；1：是),
                        "isXbdk":       是否下班不用打卡(0：否；1：是),
                        "isXbdk1Cr": 	下班1是否次日（0：否；1：是） 下班1是否次日（0：否；1：是）,
                        "isXbdk2Cr":	下班2是否次日（0：否；1：是） 下班2是否次日（0：否；1：是）,
                        "isXbdk3Cr": 	下班3是否次日（0：否；1：是） 下班3是否次日（0：否；1：是）,
                        "isXiuxi":      是否开启休息时间（0：否；1：是） 是否开启休息时间（0：否；1：是）,
                        "kgcdfzs":      旷工迟到分钟数 旷工迟到分钟数,
                        "luryid": 	    录入人员 录入人员,
                        "lusjTime":     录入时间 录入时间,
                        "name": "班次名称",
                        "qyid": 企业id,
                        "sbdk1": "上班1",
                        "sbdk2": "上班2",
                        "sbdk3": "上班3",
                        "sbqjjs1": "上班1区间结束",
                        "sbqjjs2": "上班2区间结束",
                        "sbqjjs3": "上班3区间结束",
                        "sbqjks1": "上班1区间开始",
                        "sbqjks2": "上班2区间开始",
                        "sbqjks3": "上班3区间开始",
                        "sbwd1": "下班晚到，大于0启用 ---> 1/2/3  最大值为3)",
                        "sbwd2": "下班晚到，大于0启用 ---> 1/2/3  最大值为3)",
                        "sbwd3": "下班晚到，大于0启用 ---> 1/2/3  最大值为3)",
                        "startTime": 休息开始时间 休息开始时间,
                        "sxbcs": 上下班次数(1/2/3 最大值为3),
                        "xbdk1": "下班1",
                        "xbdk2": "下班2",
                        "xbdk3": "下班3",
                        "xbqjjs1": "下班1区间结束",
                        "xbqjjs2": "下班2区间结束",
                        "xbqjjs3": "下班3区间结束",
                        "xbqjks1": "下班1区间开始",
                        "xbqjks2": "下班2区间开始",
                        "xbqjks3": "下班3区间开始",
                        "xbwz1": "下班晚走，大于0启用 ---> 1/2/3  最大值为3)",
                        "xbwz2": "下班晚走，大于0启用 ---> 1/2/3  最大值为3)",
                        "xbwz3": "下班晚走，大于0启用 ---> 1/2/3  最大值为3)",
                        "yxcdfzs": 允许迟到分钟数 允许迟到分钟数,
                        "yzcdfzs": 严重迟到分钟数 严重迟到分钟数
                    }
        :param header:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.ShiftSetting, data=jsons, headers=header)
        return response

    def shift_data_list(self, jsons, header):
        """
        获取公司所有班次信息
         :param jsons: {
                        "currentPage": 1
                        "total": 1
                        "totalPage": 50
                        }
        :param header:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.ShiftDataList, data=jsons, headers=header)
        return response

    def delete_shift(self, number, header):
        """
        删除班次
        :param number:
        :param header:
        :return:
        """
        url = "%s/%s" % (self.DeleteShift, number)
        print(url)
        response = Send_Method.send_method(method="delete", url=url, headers=header)
        return response

    def group_machine(self, header):
        """
        获取当前企业考勤机信息
        :param header:
        :return:
        """
        response = Send_Method.send_method(method="get", url=self.GroupMachine, headers=header)
        return response

    def punch_address(self, header):
        """
        获取当前企业全部打卡地址信息
        :param header:
        :return:
        """
        response = Send_Method.send_method(method="get", url=self.PunchAddress, headers=header)
        return response

    def punch_wifi(self, header):
        """
        获取当前企业全部打卡wifi
        :param header:
        :return:
        """
        response = Send_Method.send_method(method="get", url=self.PunchWiFi, headers=header)
        return response

    def att_group_list(self, jsons, header):
        """
        获取考勤组列表
        :param jsons: {
                        pageNum:	 # 当前页
                        pageSize:    # 每页条数
                        }
        :param header:
        :return:
        """
        response = Send_Method.send_method(method="get", url=self.AttGroupList, data=jsons, headers=header)
        return response

    def attendance_group(self, jsons, header):
        """
        新增考勤组
        :param jsons:{
                        "PagetransferDate":""
                        "advanceDays":""
                        "attFreeWorkdays":[]
                        "attMustPunchData":[]
                        "attMustPunchShifid":[]
                        "attNonPunchData":[]
                        "attRemind":""
                        "attRemindUserids":[]
                        "attShifts":[]
                        "attWeekdays":[1,2,3,4,5]					#	一周打卡日
                        "attWeekdaysShifts	":[805,805,805,805,805]	#	每日对应的打卡班次
                        "attadds":[4,19,29]							#	考勤地址
                        "attgroupid":52
                        "attmachines":[2,6]							#	考勤机编号
                        "atttype":1
                        "attuserids":[6,10352,10356]				#	考勤组人员
                        "attwifis":[1]								#	考勤WiFi
                        "fieldpersonnel":1                          #	外勤  1：开启 0：关闭
                        "id":52                                     #   考勤组id
                        "leastworkTime":""
                        "legalholidays":0
                        "maxOvertimeTime":""
                        "name":"考勤组名称"                          #   考勤组名称
                        "newAttTime":""
                        "normalWorkTime":""
                        "optscheduling":0
                        "overtimeRulesId":1                         #   加班规则id
                        "promptingMode":[]
                        "remCycleDays":""
                        "remarks":""
                        "reminderTime":""
                        "restdayclock":0                            #   休息日打卡   1：开启 0：关闭
                        "schedules":[]
                        }
        :param header:
        :return:
        """

        response = Send_Method.send_method(method="post", url=self.AttendanceGroup, data=jsons, headers= header)
        return response
