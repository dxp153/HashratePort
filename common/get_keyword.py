"""
通过关键字获取接口的返回值
需要安装一个 jsonpath 的库
"""
import jsonpath


class GetKeyword:

    @staticmethod
    def json_path(data, keyword):
        """

        :param data: 数据源
        :param keyword: 关键字
        :return:
        """
        return jsonpath.jsonpath(data, f"{keyword}")
