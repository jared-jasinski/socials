from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, time

url_list = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&sparkline=false'
names = []
per_page = 100
wait = 1
wait_socials = 4

def get_names():
    print('getting top 500...')
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
                print('#{} got {}'.format(((page * 100) + x) + 1, data[x]['id']))
                time.sleep(0.02)
        except(ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        time.sleep(wait)
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
        socials.append(data['community_data'])
        socials.append(data['market_data']['current_price']['usd'])
        socials.append(data['market_data']['market_cap']['usd'])
        socials.append(data['market_data']['total_volume']['usd'])
        time.sleep(wait_socials)
        return socials
    except (ConnectionError, Timeout, TooManyRedirects,json.JSONDecodeError, TypeError) as e:
        print(e)