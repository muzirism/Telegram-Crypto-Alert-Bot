import requests
from bs4 import BeautifulSoup
import re
import time
api_key="61a79b1c-4be3-4f51-9517-60438cc6881c"


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
#########################################################################################
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#parameters = {
 # 'start':'1',
  #'limit':'5000',
  #'convert':'USD'
#}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

session = Session()
session.headers.update(headers)
###########################################################################################
symbol = 'DOGE'
price = 0.1800

while 1 :
    time.sleep(10)
    try:
        response = session.get(url)
        data = json.loads(response.text)
        items = data['data']
        for item in items:
          if item['symbol']== symbol:
              print('Price at this time is' ,item["quote"]['USD']['price'])
              if item["quote"]['USD']['price'] > price :
                  print('Haji befroosh')
                  break


      #print (item)
  #print(data['data'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
