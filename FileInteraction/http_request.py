import requests

r =requests.get('https://imgs.xkcd.com/comics/making_progress.png')
print(r.status_code)
print(r.headers)
# print(r.text) #this is the raw text
# print(r.content)
with open("samples/downloaded_image.png", "wb") as f:
    f.write(r.content)

#here's how you add a payload to a get request
ploads = {'things':2,'total':25}
r = requests.get('https://httpbin.org/get',params=ploads)
print(r.text)
# print(r.url)

#here's an example of a post request
pload = {'username':'Olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)
# print(r.text)
print(r.json()) #turns into a dictionary