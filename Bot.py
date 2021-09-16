import requests
import time

#global
api_key = 'f94ab33c-05e3-455d-9f86-669d6eb7a898'
bot_token = '1976352054:AAEXeOSBoNg7E7Mn4Bp1-Hj5CjrexrgG1C0'
chat_id = '1131629301'
coin_limit = 59000
time_interval = 5

def get_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'1',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url , headers=headers , params = parameters).json()
    bitcoin_price = response['data'][0]['quote']['USD']['price']
    return bitcoin_price



def send_msg(chat_id , msg):
    url= f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}'
    requests.get(url)

def main():
    while True:
        price = get_price()
        print(price)
        if price < coin_limit:
            send_msg(chat_id,f"سعر البيتكوين: {price}")
        time.sleep(time_interval)

main()
