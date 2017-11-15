import requests
from bs4 import BeautifulSoup
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'UserName': cfg['username'], 'Password': cfg['password']}
session = requests.Session()

r = session.post('https://account.tfl.gov.uk/Login', headers=headers, data=payload)
soup = BeautifulSoup(r.content, "html.parser")
cardlink = soup.find('a', {'data-pageobject': 'mycards-card-cardlink'})
print(type(cardlink))

# r = session.get('https://oyster.tfl.gov.uk/oyster/journeyHistory.do')
# print(r.content)
