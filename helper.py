#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
import urllib.parse
import re
from urllib import parse
class helper():

    def __init__(self):
        (int(round(time.time() * 1000)));
    @staticmethod
    def request_get(self,url,costum_headers= {}, session = {}):

        cookies = ""
        for key, value in session.items():
            cookies+=key+"="+value+"; "
        if(session.__len__()<1):
            cookies = "null = 1;"
        url_parse = parse.urlsplit(url)

        headers = {
            "Host": url_parse.netloc,
            'X-SS-TC': "0",
            'User-Agent': "com.zhiliaoapp.musically/2018090613 (Linux; U; Android 8.0.0; tr_TR; TA-1020; Build/O00623; Cronet/58.0.2991.0)",
            'Accept-Encoding': "gzip",
            'Connection': "keep-alive",
            'X-Tt-Token': "",
            'sdk-version': "1",
            'Cookie': cookies
        }
        for c_key, c_value in costum_headers.items():
            headers[c_key] = c_value
        return requests.get(url, headers=headers)
    def request_post(self,url,posts = {}, costum_headers= {}, session = {}):
        cookies = ""
        for key, value in session.items():
            cookies+=key+"="+value+"; "
        if(session.__len__()<1):
            cookies = "null = 1;"
        url_parse = parse.urlsplit(url)
        headers = {
            "Host": url_parse.netloc,
            'X-SS-TC': "0",
            'User-Agent': "com.zhiliaoapp.musically/2018090613 (Linux; U; Android 8.0.0; tr_TR; TA-1020; Build/O00623; Cronet/58.0.2991.0)",
            'Accept-Encoding': "gzip",
            'Connection': "keep-alive",
            'X-Tt-Token': "",
            'sdk-version': "1",
            'Cookie': cookies
        }
        for c_key, c_value in costum_headers.items():
            headers[c_key] = c_value
        return requests.post(url, headers=headers, data=posts)
    def default_veriable(self,data = {}):
        items = {}
        items['app_language']  = "tr"
        items['language']  = "tr"
        items['region']  = "tr"
        items['app_type']  = "normal"
        items['sys_region']  = "TR"
        items['carrier_region']  = "TR"
        items['carrier_region_v2']  = "286"
        items['build_number']  = "8.4.0"
        items['timezone_offset']  = "10800"
        items['timezone_name']  = "Europe/Istanbul"
        items['mcc_mnc']  = "28601"
        items['is_my_cn']  = "0"
        items['fp']  = ""
        items['account_region']  = "TR"
        items['iid']  = "6620659482206930694"
        items['ac']  = "wifi"
        items['channel']  = "googleplay"
        items['aid']  = "1233"
        items['app_name']  = "musical_ly"
        items['version_code']  = "840"
        items['version_name']  = "8.4.0"
        items['device_id']  = "6594726280552547846"
        items['device_platform']  = "android"
        items['ssmix']  = "a"
        items['device_type']  = "TA-1020"
        items['device_brand']  = "Nokia"
        items['os_api']  = "26"
        items['os_version']  = "8.0.0"
        items['openudid']  = "b307b864b574e818"
        items['manifest_version_code']  = "2018090613"
        items['resolution']  = "720*1280"
        items['dpi']  = "320"
        items['update_version_code']  = "2018090613"
        items['_rticket']  = int(round(time.time() * 1000))
        items['ts']  = int(round(time.time() * 1000))
        items['as']  = "a1qwert123"
        items['cp']  = "cbfhckdckkde1"

        if(data.__len__()>0):
            for x,y in data.items():
                items[x] = y
        return items
    def xor(self,str, key = 5):
        veriable = []
        donen = ""
        for x in range(len(str)):
            veriable.append(ord(str.__getitem__(x)) ^ key)
        for c in veriable:

            donen+= self.base_convert(number=c,fromBase=10,toBase=16)
        return donen
    def base_convert(self,number, fromBase, toBase):
        try:
            # Convert number to base 10
            base10 = number
        except ValueError:
            raise

        if toBase < 2 or toBase > 36:
            raise NotImplementedError

        output_value = ''
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        sign = ''

        if base10 == 0:
            return '0'
        elif base10 < 0:
            sign = '-'
            base10 = -base10

        # Convert to base toBase
        s = ''
        while base10 != 0:
            r = base10 % toBase
            r = int(r)
            s = digits[r] + s
            base10 //= toBase

        output_value = sign + s
        return output_value
    def query(self,data):
        return urllib.parse.urlencode(data)
    def user_data_export(self,data):
        data_export = {}
        data_export['user_id'] = data.get('user_id')
        data_export['session_key'] = data.get('session_key')
        data_export['screen_name'] = data.get('screen_name')
        return data_export
    def explode_cookie(self,data):

        return data
