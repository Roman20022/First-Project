# import urllib.request
# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/post")
# print(response.read())
import requests
response= requests.post("https://httpbin.org/post", data="Test Data", headers={"h1":"test Title"})

print(response.text)
