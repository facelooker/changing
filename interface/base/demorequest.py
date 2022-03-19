#coding = utf-8
import requests
import json

url = 'http://127.0.0.1:8000/test/getinfo?aa=11'
data = {
            'zengchaunyin':'sss',
            'cid':'1111',
            'vailcode':'000',
            'kiam':'iii'
        }
res = requests.get(url,data).json()

tiketA = "d8cfa99b89834db09c568a35fbc30d19"
tiketB = "eba6f3c3-b4e0-4194-bf59-207ab8ff2c45"

print(len(tiketA))
print("--------")
print(len(tiketB))



print(res)