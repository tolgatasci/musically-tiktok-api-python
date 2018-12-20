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
### Like and Unlike Video ( Require Session )
	like = api.like_post(aweme_id='6632541425961536773',type='1',session=api.active_user['cookies'])
    print(like)
    unlike = api.like_post(aweme_id='6632541425961536773',type='0',session=api.active_user['cookies'])
    print(unlike)
### increase monitoring ( Require Session )
	for x in range(255):
        	view = api.view_post(aweme_id=6632541425961536773,session=api.active_user['cookies'])
        	print(view)
### Follow and Unfollow ( Require Session )
	follow = api.follow(user_id='6594722549190574086',type=1,session=api.active_user['cookies'])
	print(follow)
	unfollow = api.follow(user_id='6594722549190574086',type=0,session=api.active_user['cookies'])
	print(unfollow)
### Get User İnfo ( No Require Session )
	user_info = api.user_info(user_id=6594722549190574086,session=api.active_user['cookies'])
	print(user_info)
### MIT License

	Copyright (c) 2018 Tolga

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.
