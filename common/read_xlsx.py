import xlrd
import os
import time
from datetime import datetime
from xlrd import xldate_as_tuple


class ExcelUtil:

    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        try:
            self.table = self.data.sheet_by_name(sheetName)
        except ValueError:
            print("Excel的工资表名称错误，表名称为Sheet1")
        #   获取第一行作为key值
        self.key = self.table.row_values(0)
        #   获取总行数
        self.rowNum = self.table.nrows
        #   获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("excel表格为空")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                #   从第二行开始取对应的values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    valuesX = values[x]
                    ctype = self.table.cell(j, x).ctype
                    if ctype == 2 and valuesX % 1 == 0:  # 如果是整型
                        valuesX = int(valuesX)
                    elif ctype == 3:
                        # 转成datetime对象
                        if valuesX <= 1:
                            valuesX = int(valuesX * 24 * 3600)         # 将浮点数转换成秒
                            # valuesX = (valuesX // 3600, (valuesX % 3600) // 60, valuesX % 60\
                            valuesX = time.strftime('%H:%M:%S', time.gmtime(valuesX))   # 将秒转换成时分秒
                        else:
                            date = datetime(*xldate_as_tuple(valuesX, 0))
                            valuesX = date.strftime('%Y/%d/%m %H:%M:%S')
                    elif ctype == 4:
                        valuesX = True if valuesX == 1 else False
                    s[self.key[x]] = valuesX
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    # filepath="D:\py\hm_outo\common\login.xls"
    propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    filepath = os.path.join(propath, "data", "ygdr.xlsx")
    data = ExcelUtil(filepath)
    print(data.dict_data())

    # datas = data.dict_data()
    # print(datas[0]["手机号"])
    # print(eval(datas[0]["data"]).get("入职时间"))
