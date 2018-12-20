from api import api
import sys
if __name__ == "__main__":
    api = api()
    #api.global_veriable['costum_query_field'] = "value"
    print (api.login("username","password"))
