# -*-coding:utf-8 -*-
import requests
url = "http://127.0.0.1:8000/test/service/"
params = {"aaa":"wwww"}
# resp = requests.get(url=url,params=params)
# print(resp.text)
#
# p_resp = requests.post(url=url,data=params)
# print(p_resp.text)
# def send

# class Runmain:
def send_post(url,data=None):
    resp=requests.post(url=url,data=data)
    return resp.text
def send_get(url,data=None):
    resp=requests.get(url=url,data=data)
    return resp.text
def runserive(method,url,data=None):
    if method =='GET':
       resp=send_get(url,data)
    elif method =='POST':
        resp = send_post(url,data)
    else:
        return "ERROR METHOD"
    return resp

resp=runserive('GET',url,data=params)
print(resp)