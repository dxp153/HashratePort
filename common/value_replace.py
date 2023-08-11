
import json


class Value_Replace:

    # def __init__(self, json_data):
    #     self.json_data = json.loads(json_data)

    # def json_data(self, sendjson):
    #     """
    #     将获取的json转换成字典格式
    #     :param sendjson:
    #     :return:
    #     """
    #     data = json.loads(sendjson)
    #     return data

    # 遍历json文件所有的key对应的value,存储到一个字典中
    def json_text(self, json_data):
        # dic = self.json_data(sendjson=json_data)
        # json_data = self.json_dataN
        d = {}
        if isinstance(json_data, dict):
            for key in json_data:
                if isinstance(json_data[key], dict):
                    print("****key--：%s ,value--: %s" % (key, json_data[key]))
                    # 递归调用
                    # json_text(json_data[key])
                    d[key] = json_data[key]
                else:
                    print("****key--：%s ,value--: %s" % (key, json_data[key]))
                    d[key] = json_data[key]

    # 遍历json字典key值后，查到key则修改值value
    def check_json_value(self, json_data, key, value):
        # dic = self.json_data(sendjson=json_data)
        # json_data = self.json_data
        new = {}
        for k, v in json_data.items():
            if isinstance(v, dict):
                self.check_json_value(v, key, value)
            if k == key:
                new[k] = value
                print("****key--：%s ,value--: %s" % (k, new))
            else:
                new[k] = v
        return new





















