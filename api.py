from _overlapped import NULL

import requests
from helper import *
class api():
    api_url = "https://api2.musical.ly/"

    def __init__(self):
        var = 1
    def login(self,username,password):
        username = helper.xor(username)
        password = helper.xor(password)
        url = self.api_url+"passport/user/login/?"+helper.query(helper.default_veriable())
        posts = {
            'mix_mode':1,
            'username':username,
            'password':password,
            'email': None,
            'mobile': None,
            'account': None,
            'captcha': None
        }
        login = helper.request_post(url,posts)
        if(login.status_code != 200):
            return login.status_code
        else:
            data = login.json()
            if data.get('data'):
                return helper.user_data_export(data.get('data'))
            else:
                return login.json()
api = api()
print(api.login("username","password"))
