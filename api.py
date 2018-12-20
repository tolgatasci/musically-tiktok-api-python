import requests
import json
import os.path
from helper import helper

class api():
    api_url = "https://api2.musical.ly/"
    global_veriable = {}
    active_user = {}
    helper = helper()
    def __init__(self):
        var = 1
    def login(self,username,password):
        username = self.helper.xor(str=username)
        if os.path.exists(username+'.json'):
            with open(username+'.json', encoding='utf-8') as json_file:
                load = json.load(json_file)
                self.active_user = load
                return load
        password = self.helper.xor(password)
        url = self.api_url+"passport/user/login/?"+self.helper.query(self.helper.default_veriable(self.global_veriable))

        posts = {
            'mix_mode':1,
            'username':username,
            'password':password,
            'email': None,
            'mobile': None,
            'account': None,
            'captcha': None
        }
        login = self.helper.request_post(url,posts)

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
                success['data'] = self.helper.user_data_export(data.get('data'))
                success['cookies'] = headers
                with open(username +'.json', 'w') as outfile:
                    json.dump(success, outfile)
                return success
            else:
                return login.json()

    def home_list(self,user_data = {}):
        url = self.api_url + "aweme/v1/feed/?count=20&offset=0&max_cursor=0&type=0&is_cold_start=1&pull_type=1&"+self.helper.query(self.helper.default_veriable())
        if(user_data.__len__()>0):
            data = self.helper.request_get(self,url,session=self.active_user['cookies'])
        else:
            data = self.helper.request_get(self,url)
        return data.json()
    def search_user(self,text = 'teamtolga'):
        url = self.api_url + "aweme/v1/discover/search/?cursor=0&keyword="+text+"&count=10&type=1&hot_search=0&"+self.helper.query(self.helper.default_veriable())
        data = self.helper.request_get(self,url)
        return data.json()
    def like_post(self,aweme_id = 1, type='1', session = {}):
        url = self.api_url + "aweme/v1/commit/item/digg/?aweme_id="+ aweme_id +"&type="+ type +"&retry_type=no_retry&from=3&"+self.helper.query(self.helper.default_veriable())
        data = self.helper.request_get(self,url,session=session)
        return data.json()
    def view_post(self,aweme_id = 1,session = {}):
        data = self.helper.default_veriable()
        data['aweme_type'] = 0
        data['play_delta'] = 1
        data['item_id'] = aweme_id
        url = self.api_url + "aweme/v1/aweme/stats/?"+self.helper.query(self.helper.default_veriable())

        data = self.helper.request_post(url,posts=data,session=session)
        return data.json()
    def follow(self,user_id = '6594722549190574086', type='1', session = {}):
        url = self.api_url + "aweme/v1/commit/follow/user/?user_id="+str(user_id)+"&type="+str(type)+"&retry_type=no_retry&from=3&"+self.helper.query(self.helper.default_veriable())
        data = self.helper.request_get(self,url,session=session)
        return data.json()
    def user_info(self,user_id = '6594722549190574086', session = {}):
        url = self.api_url + "aweme/v1/user/?user_id=" + str(user_id)+"&"+self.helper.query(self.helper.default_veriable())
        data = self.helper.request_get(self,url,session=session)
        return data.json()
