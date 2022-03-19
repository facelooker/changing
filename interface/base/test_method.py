#coding=utf-8
import unittest
from base import reqApi

class TestMethod(unittest.TestCase):
    def test_01(self):
        url = 'http://127.0.0.1:8000/test/getinfo?SSS=111'
        data = {
            'zengchaunyin':'sss',
            'cid':'1111',
            'vailcode':'000',
            'kiam':'iii'
        }
        run = reqApi.reqMethodApi(url,'GET',data)
        res = run.Run(url,'GET',data)
        self.assertFalse(res.find("000")==-1,"failtest")
        # print(type(res))

if __name__ == '__main__':
    unittest.main()
