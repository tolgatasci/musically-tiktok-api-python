from api import api
from time import sleep
import sys
import os


def login_(login):
    if (login.get('code')):
        from capthca import capthca
        cc = capthca(login.get('code'))
        if (cc.backdata):
            if (len(cc.backdata) > 0):
                login = api.login(username, password, cc.backdata)
                del cc
                login_(login)
        else:
            print('empty form again')
            login = api.login(username, password, cc.backdata)
            del cc
            login_(login)

if __name__ == "__main__":
    api = api()

    api.global_veriable['device_id'] = "6648944787888948741"
    api.global_veriable['iid'] = "6648944787888948741"
    api.global_veriable['openudid'] = "6vchx2vx3ubd051q"
    username = ""
    password = ""
    login = api.login(username,password)
    login_(login)

