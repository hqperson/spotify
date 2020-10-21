import random,string,time,requests
from colorama import Fore, init
init()


class spotify:
    def __init__(self):
        self.session= requests.Session()
      
     
    def email(self):
        ran = ('').join(random.choices(string.ascii_letters + string.digits, k=8))
        email = ran+"@gmail.com"
        return email

    def passwordd(self):
        pas = ('').join(random.choices(string.ascii_letters + string.digits, k=8))
        return pas


    def user_ran(self):
        user = ('').join(random.choices(string.ascii_letters + string.digits, k=6))
        return user
        

    def create(self):
        data = {
            "creation_point":"client_mobile",
            "birth_day":"29",
            "password_repeat":self.passwordd(),
            "email":self.email(),
            "password":self.passwordd(),
            "iagree":"1",
            "birth_month":"6",
            "birth_year":"1992",
            "displayname":self.user_ran(),
            "creation_flow":"mobile_email",
            "gender":"male",
            "key":"bff58e9698f40080ec4f9ad97a2f21e0",
            "platform":"iOS-ARM"
        }
        headers = {
            "User-Agent":"Spotify/8.5.60 iOS/12.4.4 (iPhone7,2)",
            "App-Platform":"iOS",
            "Accept-Encoding":"br, gzip, deflate",
            "Content-Type":"application/x-www-form-urlencoded",
            "Spotify-App-Version":"8.5.60",
            "X-Client-Id":"58bd3c95768941ea9eb4350aaa033eb3"
        }
        send = self.session.post("https://spclient.wg.spotify.com/signup/public/v1/account",data=data,headers=headers)
        if "username" in send.text:
            print(Fore.GREEN+"[Created] account created username: {} | password: {} ".format(e,p))
        else:
            print(Fore.RED+"[Error] could not create account...")   

 
spotify().create()
