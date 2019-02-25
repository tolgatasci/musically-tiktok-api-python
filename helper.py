#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
import urllib.parse
import re
from urllib import parse


class Helper():

    @staticmethod
    def request_get(url, costum_headers={}, session={}):

        cookies = ""
        for key, value in session.items():
            cookies += key + "=" + value + "; "
        if (session.__len__() < 1):
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

    @staticmethod
    def request_post(url, posts={}, costum_headers={}, session={}):
        cookies = ""
        for key, value in session.items():
            cookies += key + "=" + value + "; "
        if (session.__len__() < 1):
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

    @staticmethod
    def default_variable(data={}):
        items = {}
        items['app_language'] = "cs"
        items['language'] = "cs"
        items['region'] = "cs"
        items['app_type'] = "normal"
        items['sys_region'] = "CZ"
        items['carrier_region'] = "CZ"
        items['carrier_region_v2'] = "230"
        items['build_number'] = "9.9.0"
        items['timezone_offset'] = "10800"
        items['timezone_name'] = "Europe/Istanbul"
        items['mcc_mnc'] = "23001"
        items['is_my_cn'] = "0"
        items['fp'] = ""
        items['account_region'] = "CZ"
        items['iid'] = "6620659482206930694"
        items['ac'] = "wifi"
        items['channel'] = "googleplay"
        items['aid'] = "1233"
        items['app_name'] = "musical_ly"
        items['version_code'] = "990"
        items['version_name'] = "9.9.0"
        items['device_id'] = "6594726280552547846"
        items['device_platform'] = "android"
        items['ssmix'] = "a"
        items['device_type'] = "TA-1020"
        items['device_brand'] = "Nokia"
        items['os_api'] = "26"
        items['os_version'] = "8.0.0"
        items['openudid'] = "b307b864b574e818"
        items['manifest_version_code'] = "2019011531"
        items['resolution'] = "720*1280"
        items['dpi'] = "320"
        items['update_version_code'] = "2019011531"
        items['_rticket'] = int(round(time.time() * 1000))
        items['ts'] = int(round(time.time() * 1000))
        items['as'] = "a145cac75e153c5ef36066"
        items['cp'] = "ab5ac054ec3175e3e1Yaae"
        items['mas'] = "016d48633d67d491135bc9b025d80be9d56c6c0c6ccc66a6acc6cc"

        if (data.__len__() > 0):
            for x, y in data.items():
                items[x] = y
        return items

    @staticmethod
    def xor(string, key=5):
        # now it works also for extended utf-8 characters, and is much simpler
        return ''.join([hex(int(x ^ key))[2:] for x in string.encode('utf-8')])

    @staticmethod
    def query(data):
        return urllib.parse.urlencode(data)

    @staticmethod
    def user_data_export(data):
        data_export = {}
        data_export['user_id'] = data.get('user_id')
        data_export['session_key'] = data.get('session_key')
        data_export['screen_name'] = data.get('screen_name')
        return data_export

    @staticmethod
    def explode_cookie(data):
        return data
