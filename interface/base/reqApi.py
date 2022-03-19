import requests
import json


class reqMethodApi:
    def __init__(self,url,method,data=None):#构造函数
        self.res = self.Run(url,method,data)
    def Get(self,url,data):
        res = requests.get(url,data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def Post(self,url,data):
        res = requests.post(url,data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def Run(self,url,method,data=None):
        res = None
        if(method == 'GET'):
            res = self.Get(url,data)
        elif(method == 'POST'):
            res = self.Post(url,data)
        else:
            print('wrong requset way')
        return res
if __name__ == '__main__':
    # url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    # data = {
    #     'cart':'11'
    # }
    url = 'http://127.0.0.1:8000/test/getinfo?SSS=111'
    data = {
        'zengchaunyin': 'sss',
        'cid': '1111',
        'vailcode': '000',
        'kiam': 'iii'
    }
    api = reqMethodApi(url,'GET',data)
    # print(api.res)
    print (api.Run(url,'GET',data))



