import  requests
def myRequest(url,method, request_data):
    # 判断是个geet请求还是post请求
    # 调用requeest方法
    # 获取返回值
    if method=="get":
        res=requests.get(url,request_data)
    elif method=="post":
        res=requests.post(url,request_data)
    else:
        res=None
    return  res

