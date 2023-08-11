from common.get_keyword import GetKeyword
from interface.approve import Approve
from interface.competent import Competent
import json
import pytest
import allure
import time
from common.yaml_translation import yamlUtil


@allure.epic("发起审批接口测试")
@pytest.mark.usefixtures("login_cooking")
class Test_Initiate_Approval:

    @pytest.mark.parametrize("yaml", yamlUtil("../data/approval_initiate.yml").read_yaml())
    def test_initiate_approval_01(self, login_cooking, yaml):
        """
        发起审批并撤销
        :param login_cooking:
        :return:
        """
        request = [
            {"value": "若因公到外地出差，无法到公司打卡考勤，可提交出差审批"},
            {"value": "2020-11-1"},
            {"value": "2020-11-1"},
            {"value": 8},
            {"value": "星星"},
            {"value": "点点"},
            {"value": "从现在起"},
            {"value": ""},
            {"value": []}
        ]

        ApprovalId = "$..spmkCustomApprovals..id"
        Approvalname = "$..spmkCustomApprovals..name"
        inputID = "$..inputId"
        froms = "$.data..froms"
        router = "$.data..router"
        assoType = "$.data..assoType"
        username = "$..name"
        cooking = login_cooking[0][1]
        r = Approve().approval_list(cooking)
        id = GetKeyword.json_path(json.loads(r.text), ApprovalId)  # 获取全部可发起审批的ID
        name = GetKeyword.json_path(json.loads(r.text), Approvalname)  # 获取全部可发起审批的name
        p = Approve().approval_particulars(id[0], cooking)  # 获取第一个审批的详情
        fromss = GetKeyword.json_path(json.loads(p.text), froms)  # 接口所需的froms参数
        froms = json.dumps(fromss[0], ensure_ascii=False)
        router = GetKeyword.json_path(json.loads(p.text), router)
        assoType = GetKeyword.json_path(json.loads(p.text), assoType)  # 接口所需的assoType参数
        inputID = GetKeyword.json_path(json.loads(p.text), inputID)  # 获取审批详情每一项的inputID
        timer = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        requestData = dict(zip(inputID, request))
        requestData['__startTime'] = {"value": "%s" % timer}   # 开始时间，结束时间变为自动获取
        requestData['__endTime'] = {"value": "%s" % timer}  # requestData   申请数据
        requestData = json.loads(json.dumps(requestData))
        r = Competent().competent(cooking)
        c = GetKeyword.json_path(json.loads(r.text), "$..data[-1:]")  # 获取审批人数据
        competent = c[0]
        competent['id'] = competent.pop("leaderEmpNum")  # 将上级主管中的leaderEmpNum 替换成ID
        competent['name'] = competent.pop("charge")     # 将上级主管中的charge 替换成name
        router[0]["children"][0]["relation"][0]["users"] = competent  # 接口所需的router参数
        user = GetKeyword.json_path(json.loads(login_cooking[0][0].text), username)  # 发起人姓名
        title = "%s的%s测试审批" % (user[-1], name[0])  # titles
        data = {
            "approveName": "%s" % name[0],
            "assoType": int("%s" % assoType[0]),
            "froms": json.loads(froms),
            "initiator": user[-1],
            "requestData": requestData,
            "router": router[0],
            "title": "%s" % title
        }
        j = json.loads(json.dumps(data, ensure_ascii=False))
        Approve().approval_initiate(jsons=j, headers=cooking)   # 发起审批
        jsonS = {
            "sts": 0,
            "type": 0
        }
        sList = Approve().select_approval(jsons=jsonS, headers=cooking)  # 查询待审批列表
        tit = GetKeyword.json_path(json.loads(sList.text), "$..title")
        print(tit)
        try:
            assert tit[0] == title
            print("审批发起成功")
            id = GetKeyword.json_path(json.loads(sList.text), "$..id")
            Approve().remove_approal(id=id[0], headers=cooking)             # 撤销之前审批
            jsonS["sts"] = 1
            rList = Approve().select_approval(jsons=jsonS, headers=cooking)  # 查询撤销审批列表
            rID = GetKeyword.json_path(json.loads(rList.text), "$..id")
            try:
                assert id[0] == rID[0]
                print("审批撤销成功")
            except AssertionError:
                print("未发现审批号%s的审批" % id[0])
        except AssertionError:
            print("%s发起失败" % title)