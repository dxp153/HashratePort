import pytest
from common.yaml_translation import yamlUtil
from common.send_method import Send_Method
import requests


# 主机列表查询
class Host_List:

    def __init__(self, base_url):
        self.url = "%s/api/computing-market/scinstance/computingPowerPurchasePage?" % base_url

    def filtrate_host_list(self, url_prar, header):
        """

        :param url_prar:    order:
                            orderField:
                            page: 1                 展示第 X 页
                            limit: 10               每页 X 条数据
                            priceMethod: 1
                            regionId:
                            gpuModelId:
                            gpuNum:
                            gpuCardAvailable:
                            minPrice: 1             价格区间min
                            maxPrice: 2             价格区间max
                            sort:
                            isRent: false
                            lookCanRent: 0
                            onlineSort:
                            priceSort:
                            _t: 1691995527915

        """

        url = self.url + url_prar
        print(url)
        response = Send_Method.send_method(method='get', url=url, headers=header)
        return response
