import requests
import json
from django.http.response import HttpResponse
data={
    'username':'sadada',
    'password':'ssssss'
}
headers={
    'content-type':'application/json'
}
data = json.dumps(data)
url  = 'http://127.0.0.1:8000/test/postinfo/'
url2 = 'http://127.0.0.1:8000/test/getinfo?ssss=qsdada&fssadas=uuuu'
# headers =json.dumps(headers)
# print(data)
class Main:
    def send_post(self,url,data,headers):
       self.responsemsg = self.requests.post(url=url,data=data,headers=headers)
       return self.responsemsg.text
    def send_get(url,data):
        resmsg = requests.get(url=url,data=data)
        # return json.dumps(resmsg,sort_keys=True,indent=2)
        return resmsg.text
    def main(method,url,data=None):
        res = ''
        if method == 'GET':
            res = send_get(url=url,data=data)
        elif method == 'POST':
            res = send_post(url=url,data=data)
        else:
            return HttpResponse('请求方法错误')
        return res

# res2 = send_get(url2,data)
# print('res2:'+res2)
# res = send_post(url=url,data=data,headers=headers)
# print('res:'+res)
res = main('GET',url2)
print(res)