import requests
import datetime
import time
from bs4 import BeautifulSoup

website_url = "http://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Poland"
head = requests.utils.default_headers()
request = requests.get(website_url, head)
soup = BeautifulSoup(request.content,'html.parser')
#print(soup.prettify())

clas = soup.find(id='mw-content-text')
#print(clas)
info = clas.find_all(class_='sortbottom')
#print(info)
inf = info[0]
#print(inf)
sorttd= inf.find_all('td')
#print(sorttd)
przypadki = [t.text.strip() for t in sorttd]

confirmed=przypadki[6]
suspected=przypadki[1]
deaths=przypadki[8]

przypadki = [t.text.strip() for t in sorttd]

print ('Stan na dzień: ',time.strftime("%Y-%m-%d ", time.localtime()))
print ('Potwierdzone przypadki:', confirmed)
print ('Podejrzani:', suspected)
print ('Zgony:', deaths)
