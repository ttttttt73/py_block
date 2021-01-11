import unittest
import requests
import json
'''
class UnitTest(unittest.TestCase):
    def setUp(self):
        self.host = 'http://loclahost:5000'
        self.right_parameter = {
                'parameter1' : 3,
                'parameter2' : 6
                }
        self.wrong_parameter = {
                'parameter1' : 3
                }
'''

host = 'http://localhost:5000'
path = '/encrypt'
url = host + path
data = (("msg","hello"),)

response = requests.get(url, params=data)
result = response.json()
print(result)

path = '/decrypt'
url = host + path
header = {"Content-Type":"application/json"}
# data = {f'{result}'}
data = result
print(data)
response = requests.post(url, headers=header, json=data)
print(response)
print(response.json())
