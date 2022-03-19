# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response #返回页面用
from django.http import HttpResponse
import json
import re
from urllib import parse
# Create your views here.

#POST请求接口，返回表单指定字段数据
def Login(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       return HttpResponse(username)
    else:
        return  render_to_response('login.html')

def post_infov2(request):
    if request.method == 'POST' and request.META.get('CONTENT_TYPE')=='application/json':
        params =""
        params = json.loads(request.body)
        params = json.dumps(params)
        return HttpResponse(params)
    else:
        return HttpResponse("请求异常")
#GET请求接口
def Info(request):
    resultData = {}
    if request.method == 'GET':
        userName = request.GET.get('username')
        cId = request.GET.get('cid')
        vailCode = request.GET.get('vailcode')
        resultData['username'] = userName
        resultData['cid'] = cId
        resultData['vailcode'] = vailCode
        resultdata = json.dumps(resultData)
        # print(resultData)
        return HttpResponse(resultdata)
    else:
        return render_to_response('login.html')
#GET接口，返回全部URL参数
def requestUrl(request):
    if request.method == 'GET':
        reqMsg = request.get_full_path()
        reqMsgPam = re.findall(r"\?(.*)",reqMsg)#列表类型['']
        reqMsgPamS = ''.join(reqMsgPam)
        print(type(reqMsgPamS))
        # reqMsgPam = str(reqMsgPam)
        # reqMsgPamS = ''
        if (reqMsgPamS.find('&') != -1):
            reqMsgPamS=reqMsgPamS.replace('&',';')
            # print ("信息"+reqMsgPamS)
            # print(type(reqMsgPamS))
            reqMsgPamS = json.dumps(reqMsgPamS)
            return  HttpResponse(reqMsgPamS)
        else:
            pass
    else:
        return render_to_response('login.html')
#GET接口，返回全部URL参数二
def get_Info(request):
    result = {}
    if request.method == 'GET':
        for k, v in request.GET.items():
            result[k]= v
        result = json.dumps(result)
        return HttpResponse(result)
    else:
        return render_to_response('login.html')

#POST接口，根据header返回表单或body参数
def post_Info(request):
    if request.method == 'POST' and request.META.get('CONTENT_TYPE') == "application/x-www-form-urlencoded":
        params = ""
        username = request.POST.get('username')
        card_id = request.POST.get('card_id')
        password = request.POST.get('password')
        params = "用户名:"+username + "密码:" + password + "身份证:" + card_id
        # params = json.dumps(params)
        return HttpResponse(params)
    elif request.method == 'POST' and request.META.get('CONTENT_TYPE') == "application/json":
        params = ""
        params = json.loads(request.body)
        params = json.dumps(params)
        return HttpResponse(params)
    elif request.method == 'POST' and request.META.get('CONTENT_TYPE') == "application/json" and request.COOKIES['test_Cookie']!=None:
       return excu_Cookie(request.COOKIES['test_Cookie'])
    else:
        return render_to_response('login.html')

def excu_Cookie(cookies):
    message = "提交订单--Cookies是"
    return HttpResponse(message + cookies)


def service(request):
    params={}
    requestheader = request.META.get('CONTENT_TYPE')
    if request.method=='GET':
        for k,v in request.GET.items():
            params[k]=v
    elif request.method=='POST':
        if requestheader == "application/x-www-form-urlencoded" or requestheader == None:
            params = request.POST
        elif requestheader == "application/json":
            params = json.loads(request.body)
        else:
            return HttpResponse("ERROR HEADERS")
    else:
        return HttpResponse("ERROR METHODS")
    return HttpResponse(json.dumps(params))


