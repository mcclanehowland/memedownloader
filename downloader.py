import urllib.request
from bs4 import BeautifulSoup

url = "https://ifunny.co/"

response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html,'html.parser')

counter = 1
for link in soup.find_all("img", class_="media__image"):
    urllib.request.urlretrieve(link.get('src'),'./images/image'+str(counter)+'.jpeg')
    counter = counter+1
