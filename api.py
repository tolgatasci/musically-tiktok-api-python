import requests
import json
import os.path
from helper import *

class api():
    api_url = "https://api2.musical.ly/"
    global_veriable = {}
    active_user = {}
    def __init__(self):
        var = 1
    def login(self,username,password):
        username = helper.xor(username)
        if os.path.exists(username+'.json'):
            with open(username+'.json', encoding='utf-8') as json_file:
                load = json.load(json_file)
                self.active_user = load
                return load
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

    def home_list(self,user_data = {}):
        url = self.api_url + "aweme/v1/feed/?count=20&offset=0&max_cursor=0&type=0&is_cold_start=1&pull_type=1&"+helper.query(helper.default_veriable())
        if(user_data.__len__()>0):
            data = helper.request_get(self,url,session=self.active_user['cookies'])
        else:
            data = helper.request_get(self,url)
        return data.json()

