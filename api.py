import requests
import json
import os.path
from helper import *

class api():
    api_url = "https://api2.musical.ly/"
    global_veriable = {}
    def __init__(self):
        var = 1
    def login(self,username,password):
        username = helper.xor(username)
        if os.path.exists(username+'.json'):
            with open(username+'.json') as json_file:
                return json.load(json_file)
        password = helper.xor(password)
        url = self.api_url+"passport/user/login/?"+helper.query(helper.default_veriable(self.global_veriable))

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

        try:
            headers = {}
            for c in login.cookies:
                headers[c.name]= c.value

        except KeyError:
            headers = None
        success = {}
        if(login.status_code != 200):
            return login.status_code
        else:
            data = login.json()
            if (data.get('data') and (data.get('error_code') == None)):
                success['data'] = helper.user_data_export(data.get('data'))
                success['cookies'] = headers
                with open(username +'.json', 'w') as outfile:
                    json.dump(success, outfile)
                return success
            else:
                return login.json()
