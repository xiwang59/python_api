from conmon.doExcel import DoExcel
from conmon import requestApi
import os
# 获取所有的数据,不要写绝对路径，这样灵活性就很高
de=DoExcel(os.getcwd().replace("testCase","testDatas")+"/apitest.xlsx")
all_case=de.get_caseData()
print("所有的请求数据",all_case)
# 使用for循环读取每行的测试数据
for case_data in all_case:
    print(case_data)
    res=requestApi.myRequest(case_data["url"],case_data["method"],eval(case_data["request_data"]))
    print(res)
    print()
    assert res.text == case_data["expected_data"]
# 比对响应结果与期望结果

