from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, time

url_list = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&sparkline=false'
names = []
per_page = 100


def get_names():
    for page in range(5):
        parameters = {
        'page':page + 1,
        'per_page':per_page
        }
        headers = {
        'Accepts': 'application/json',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url_list, params=parameters)
            data = json.loads(response.text)
            for x in range(per_page):
                names.append(data[x]['id'])
        except(ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        time.sleep(15)
        print('getting names... we are on page {}'.format(page))
    return names


def get_info(name):
    url_socials = 'https://api.coingecko.com/api/v3/coins/{}?localization=false&tickers=false&market_data=true&community_data=true&developer_data=false&sparkline=false'.format(name)
    headers = {
    'Accepts': 'application/json',
    }
    socials = []
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url_socials)
        data = json.loads(response.text)
        #print(data['community_data'])
        #print(data['market_data']['current_price']['usd'])
        socials.append(data['community_data'])
        socials.append(data['market_data']['current_price']['usd'])
        return socials
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)