import unittest
from django.test import TestCase
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(chrome_options=option)
# Create your tests here.
#
# from itertools import combinations
#
# s = ['2','7','8','11','13','19','27','28']
#
#
# comlist = list(combinations(s,6))
# for i in comlist:
#     print(i)


