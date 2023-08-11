from common.login_cooking import Cooking
from common.send_method import Send_Method
from common.get_keyword import GetKeyword
from common.value_replace import Value_Replace
import allure
import random
import requests
import json
import ast


@allure.step("审批模块")
class Approve:

    def __init__(self):
        self.list = "http://test-8timer-api.youlingrc.com/spmk/list_approval_g"
        self.Particulars = "http://test-8timer-api.youlingrc.com/spmk/select_custom_approval"
        self.InitiateApproval = "http://test-8timer-api.youlingrc.com/spmk/start_approval"
        self.SelectApproval = "http://test-8timer-api.youlingrc.com/spmk/select_my_approve"
        self.RemoveApproval = "http://test-8timer-api.youlingrc.com/spmk/revoke_approval/"

    def approval_list(self, headers):
        """
        查看能发起的审批列表
        :param headers: cooking
        :param json_path: json_path
        :return:response,response中某个参数的值
        """
        # response = requests.get(url=self.url, headers=self.headers)
        response = Send_Method.send_method(method="get", url=self.list, headers=headers)
        return response

    def approval_particulars(self, id, headers):
        """
        查看审批详情
        :param headers:
        :param list_path:想要查询的审批单的id所在的json_path
        :return:
        """
        url = self.Particulars + "/%s" % id
        # print(url)
        response = Send_Method.send_method(method="get", url=url, headers=headers)
        t = response.text
        r = json.loads(t)
        # print("r = %s" % r)
        return response

    def approval_initiate(self, jsons, headers):
        """
        发起审批
        :param jsons:{  "approveName": "审批名称",
                        "assoType": 1,
                        "digest": "摘要",
                        "froms": "数组",              #  approval_particulars   中的    particulars_json_parameters
                        "initiator": "发起人名称",
                        "requestData": "申请数据",
                        "router": {
                            "children": [],
                            "className": "",
                            "condition": [],
                            "execute": "",
                            "flow": true,
                            "name": "",
                            "relation": []
                        },
                            "title": "标题"
                        }
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.InitiateApproval, data=jsons, headers=headers)
        return response

    def select_approval(self, jsons, headers):
        """
        查询审批列表
        :param json: {
                        "currentPage": 0,
                        "empNum": 0,            # 结束时间
                        "endTime": "",
                        "offset": 0,
                        "orgCode": 0,
                        "query": "",            # 关键字 标题/审批人名称/审批总汇id
                        "startTime": "",        # 开始时间
                        "sts": 0,               # 状态 0审批中 1审批撤销 2审批通过/审批完成 3审批拒绝 4 已审批 5全部
                        "totalPage": 0,
                        "type": 0               # 0我发起的 1抄送我的 2我审批的 3全部
                        }
        :param headers:
        :return:
        """
        response = Send_Method.send_method(method="post", url=self.SelectApproval, data=jsons, headers=headers)
        return response

    def remove_approal(self, id, headers):
        """
        审批撤回
        :param id: 审批单id
        :param headers:
        :return:
        """

        RemoveApproal = "%s%s" % (self.RemoveApproval, id)
        response = Send_Method.send_method(method="put", url=RemoveApproal, headers=headers)
        return response


if __name__ == "__main__":
    data = {
        "phone": "15797629873",
        "pw": "123456"
    }
    list_path = "$.data[2].spmkCustomApprovals[0].id"
    c = Cooking.login_cooking(data)[1]
    g = GetKeyword()
    e = Approve()
    l = e.approval_list(c)
    print(l.text)
    j = g.json_path(json.loads(l.text), "$..spmkCustomApprovals..id")
    print(j)




















    # r = random.choice(j)
    # num = j.index(r)
    # print(r)
    # print(num)
    # n = g.json_path(json.loads(l.text), "$..spmkCustomApprovals..name")
    # name = n[r]
    # print(name)











    # t2 = e.approval_particulars(list_path, c)
    # print("t2=", t2.text)
    # t = GetKeyword.json_path(json.loads(t2.text), "$.data.froms")  # $.data.froms：审批详情的数组，位于json中的位置
    # new = {}
    # for i in t[0]:
    #     new = i
    #     if new["inputId"] == "Explain":
    #         new["label"] = ""
    # print("t[0]= %s" % t[0])
    # v = Value_Replace()
    # vv = v.check_json_value(json.loads(t2.text), "froms", t[0])
    # print("vv=", vv)
