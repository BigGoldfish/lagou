#encoding=utf-8
'''
    根据地名和职位名搜索
    保存前30页内容到xlsx
'''
import json
import requests
import time
from openpyxl import Workbook
from settings import *

def GetResponse():
    response = requests.post(url, data = para, headers = headers, cookies = cookies)
    time.sleep(2)
    response_json = json.loads(response.text)
    return response_json 

def GetLable(result, lable):
    LableList = result[lable]
    Lable = ''
    if (LableList == [] or LableList[0] == '""'):
        Lable = '无'
    else:
        for item in LableList:
            Lable = Lable + item + ','
        Lable = Lable[:-1]
    return Lable

def GetContent():
    content = []
    response_json = GetResponse()
    for pn in range(1, 31):
        print('正在保存第{}页\n'.format(pn))
        if (pn != '1'):
            para['first'] = 'false'
        para['pn'] = str(pn)
        response_json = GetResponse()
        results = response_json['content']['positionResult']['result']
        for result in results:
            company = result['companyFullName']
            financeStage = result['financeStage']
            companySize = result['companySize']
            companyLabel = GetLable(result, 'companyLabelList')
            district = result['district']
            positionName = result['positionName']
            education = result['education']
            positionLable = GetLable(result, 'positionLables')
            jobNature = result['jobNature']
            salary = result['salary']
            workYear = result['workYear']
            content.append([company, financeStage, companySize, companyLabel, district, positionName, education, positionLable, jobNature, salary, workYear])
        print('完成！\n')
    return content

def save_xlsx(content):
    wb = Workbook()
    ws = wb.active
    ws.title = filename
    ws.append(['公司名称','融资情况','公司规模','公司标签','区域','职位名称','学历','职位标签','工作性质','薪资','工作年限'])
    for item in content:
        ws.append(item)
    wb.save(filename + '.xlsx')
def main():
    content = GetContent()
    save_xlsx(content)

if __name__ == '__main__':
    main()
