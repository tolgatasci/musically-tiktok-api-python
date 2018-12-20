# musically tiktok api python
Musically ( Tiktok ) api python open source free... 

we can work together to develop.



### Login Username, Password
    print(api.login("username","password"))
### Home Video List ( No Require Session )
    # Cookie Active User
    # home_list = api.home_list(api.active_user)
    # No Cookie
    home_list = api.home_list()
    print(home_list)
### Search User ( No Require Session )
	search = api.search_user(text='teamtolga')
    print(search)
### Like Video ( Require Session )
	like = api.like_post(aweme_id='6632541425961536773',type='1',session=api.active_user['cookies'])
    print(like)
    unlike = api.like_post(aweme_id='6632541425961536773',type='0',session=api.active_user['cookies'])
    print(unlike)
