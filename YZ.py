import json
import os
import time
from time import sleep

import requests
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
import urllib.request
from matplotlib import pyplot as plt
from helper import helper
class YZ:
    sayi  = 25
    start_date = 0
    helper_ = None
    self_ = None
    api_  = None

    def __init__(self,api,helper):
        self_ = self
        self.api_= api
        self.helper_ = helper
        return None
    def checkimage(self,buyuk,kucuk,id):
        urllib.request.urlretrieve(buyuk, "resimler/cop/buyuk/"+str(id)+".jpg")
        urllib.request.urlretrieve(kucuk, "resimler/cop/kucuk/"+str(id)+".jpg")
        boyutlar = {}
        img_rgb = cv2.imread("resimler/cop/buyuk/"+str(id)+".jpg")
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread("resimler/cop/kucuk/"+str(id)+".jpg",0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (5,5,255), 2)
            boyutlar['sol_x'] = pt[0]
            boyutlar['sol_y'] = pt[1]
            boyutlar['sag_x'] = pt[0] + w
            boyutlar['sag_y'] = pt[1] + h
        os.remove("resimler/cop/kucuk/"+str(id)+".jpg")
        os.remove("resimler/cop/buyuk/"+str(id)+".jpg")
        '''for i in range(1):
            plt.subplot(1,1,1),plt.imshow(img_rgb,'gray')
            plt.title("test")
            plt.xticks([]),plt.yticks([])
            plt.show()
        '''
        return boyutlar
    def puzzle_get(self):
        x = {}
        url = "https://verification-va.byteoversea.com/get?aid=1233&lang=tr&app_name=musical_ly&iid="+str(self.api_.global_veriable['iid'])+"&vc=2018111625&did="+str(self.api_.global_veriable['device_id'])+"&ch=googleplay&os=0&challenge_code=1105"
        data = self.helper_.request_get(self,url)
        data = data.json().get('data')
        x['id'] = data['id']
        x['url1'] = data['question']['url1']
        x['url2'] = data['question']['url2']
        url = data['question']['url1']
        width, height = self.get_image_size(url)
        x['width']  = width
        x['height'] = height
        x['tip_y'] = data['question']['tip_y']
        return x
    def get_image_size(self,url):
        data = requests.get(url).content
        im = Image.open(BytesIO(data))
        return im.size
    def request_puzzle(self,id,y,x,tim):
        start_date = int(round(time.time() * 1000))
        reply = []
        sleep(0.1)
        for c in range(int(x) // 7):
            c = c + 1
            relative_time = int(round(time.time() * 1000)) - start_date
            rp = {
                    "relative_time": relative_time,
                    "x": (int(c) * 7),
                    "y": y
                }
            reply.append(rp)
            sleep(0.1)

        url = "https://verification-va.byteoversea.com/verify?aid=1233&lang=tr&app_name=musical_ly&iid="+str(self.api_.global_veriable['iid'])+"&vc=2018111625&did="+str(self.api_.global_veriable['device_id'])+"&ch=googleplay&os=0&challenge_code=1105"
        header = {}
        jsonx = {"modified_img_width":335,"id":str(id),"mode":"slide","reply":reply}
        header['Content-Type'] = 'application/json'
        return self.helper_.request_post(self,url=url,posts=json.dumps(jsonx),costum_headers=header).json()
    def puzla_getter(self,get_puzzle,sol_x):


        p = self.request_puzzle(get_puzzle['id'],get_puzzle['tip_y'],sol_x,self.start_date)


        if(p.get('action') =="new"):
            sayi = self.sayi + 1
            self.resim_degistir()
        else:
            return "ok"
    def resim_degistir(self):

        try:
            get_puzzle = self.puzzle_get()
            self.start_date = int(round(time.time() * 1000))

            check = self.checkimage(buyuk=get_puzzle['url1'],kucuk=get_puzzle['url2'],id=get_puzzle['id'])
            sol_x = int(check['sol_x']) + self.sayi
            gelen = self.puzla_getter(get_puzzle,sol_x)
            if(gelen=="ok"):
                return 1
        except BaseException as e:
            print(e)
            self.resim_degistir()


