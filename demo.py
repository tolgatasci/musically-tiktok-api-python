from api import api
import sys
if __name__ == "__main__":
    api = api()
    api.global_veriable['as'] = "test"
    api.global_veriable['cp'] = "test"
    (api.login("",""))

    # Cookie Active User
    #home_list = api.home_list(api.active_user)
    # No Cookie
    home_list = api.home_list()
    print(home_list)

