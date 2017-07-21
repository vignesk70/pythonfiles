import urllib
import requests

posturl="https://maker.ifttt.com/trigger/{event}/with/key/b5ObZ2pevIZcbrJ9uKie3l"
payload = {}
r = requests.post(posturl, data={})
print(r.url)
print(r.text)

