import  requests
from requests.cookies import RequestsCookieJar
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
s.get('https://www.baidu.com')
r = s.get('https://www.baidu.com/cookies')

#print(r.text.encode())

r = requests.get("https://en.wikipedia.org/wiki/Monty_Python")
print(r.headers)
r.text.encode()

cookiejar = RequestsCookieJar()
cookiejar.set()