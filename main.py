import requests
from fake_useragent import UserAgent

#fake useragent alıyoruz
ua=UserAgent()

s=requests.Session()
s.get("https://instagram.com")
#csftoken alıyoruz
cookie=s.cookies.get('csrftoken')

#headerimiz, belirliyoruz
header = {
    'x-csrftoken': cookie,
    'user-agent':ua.chrome  #"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

#kullanıcı adı şifre
username="xxxxxx"
password="xxxxxx"

#data belirliyoruz
data={
    "username":f"{username}",
    "enc_password":f"#PWD_INSTAGRAM_BROWSER:0:0:"+password,
    "queryParams": {}
}

#giriş isteği gonderiyoruz
r=s.post("https://www.instagram.com/accounts/login/ajax/",data=data, headers=header)

if r.json()['authenticated']:
     print(r.text)
     print("Giriş Başarılı")
else:
    print("Giriş Başarısız")
