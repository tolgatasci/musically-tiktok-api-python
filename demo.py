from api import Api
from time import sleep
import sys
import os


def login_(login):
    if (login.get('code')):
        from capthca import capthca
        cc = capthca(login.get('code'))
        if (cc.backdata):
            if (len(cc.backdata) > 0):
                login = Api.login(username, password, cc.backdata)
                del cc
                login_(login)
        else:
            print('empty form again')
            login = Api.login(username, password, cc.backdata)
            del cc
            login_(login)

if __name__ == "__main__":
    api = Api()

    api.global_variable['device_id'] = "6648944787888948741"
    api.global_variable['iid'] = "6648944787888948741"
    api.global_variable['openudid'] = "6vchx2vx3ubd051q"
    username = ""
    password = ""
    login = api.login(username,password)
    login_(login)

