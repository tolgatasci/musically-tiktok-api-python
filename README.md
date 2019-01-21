# musically tiktok api python
Musically ( Tiktok ) api python open source free... 

we can work together to develop.

## Create Register Device Method Private
service/2/device_register/
Contact me : 
- We Chat  : tolgatasci1
- Telegram : @tolgatasci


## Required
- Python 3.x
- Json
- requests

## Wiki Info
- [Change Device Info](https://github.com/tolgatasci/musically-tiktok-api-python/wiki/Device-Info-Change "Change Device Info")
- [Create Account](https://github.com/tolgatasci/musically-tiktok-api-python/wiki/Account-Create "Create Account")

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
### User Follower List ( Require Session )
	follower = api.follow_list(user_id=6594722549190574086,count=20,session=api.active_user['cookies'])
	print(follower)	
### User Following List ( Require Session )
	following = api.following_list(user_id=6594722549190574086,count=20,session=api.active_user['cookies'])
	print(following)		
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
### User Video List ( No Require Session )
	user_video_list = api.user_video_list(user_id=6594722549190574086)
	print(user_video_list)
### Search Tags  ( No Require Session )
	tags = api.search_hashtag(text="teamtolga")
	print(tags)
### Tag list Videos  ( No Require Session )
	tag_videos = api.list_hashtag(cid=cid)
	print(tag_videos)	
