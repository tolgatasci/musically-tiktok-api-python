from api import api
import sys
if __name__ == "__main__":
    api = api()
    #api.global_veriable['as'] = "test" change Device Info
    #api.global_veriable['cp'] = "test" change Device Info
    (api.login("",""))

    # Cookie Active User
    #home_list = api.home_list(api.active_user)
    # No Cookie
    #home_list = api.home_list()
    #print(home_list)

    #search = api.search_user(text='teamtolga')
    #print(search)


    #like = api.like_post(aweme_id='6632541425961536773',type='1',session=api.active_user['cookies'])
    #print(like)
    #unlike = api.like_post(aweme_id='6632541425961536773',type='0',session=api.active_user['cookies'])
    #print(unlike)
