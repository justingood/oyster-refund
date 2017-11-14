import requests

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'UserName': 'user here', 'Password': 'password here'}
session = requests.Session()

r = session.post('https://account.tfl.gov.uk/Login', headers=headers, data=payload)

# r = session.get('https://oyster.tfl.gov.uk/oyster/journeyHistory.do')
print(r.content)
