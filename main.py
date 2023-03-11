from art import tprint
import requests
import json
import time

def start():
    save_one_select()

    print('[!] Please wait while the data is being downloaded....')
    tprint('Surveillance', font='standard')
    question = input('[+] Monitoring\nWhere do we start ?: ')


    if question == 'Monitoring':
        Select_Ethereum().select_Ethereum()

        
def save_one_select():

    url = 'https://api.coinmarketcap.com/dexer/v3/dexer/pair-list?base-address=0x2170ed0880ac9a755fd29b2688956bd959f933f8&start=1&limit=10&platform-id=14'
    response = requests.get(url)

    price_ETH_USDT = json.loads(response.text)
    price_ETH_USDT_TO_DICT = dict(price_ETH_USDT)

    with open('two.json', 'w') as file:
        json.dump(price_ETH_USDT_TO_DICT, file, indent=4, ensure_ascii=False)


class Select_Ethereum():

    def select_Ethereum(self):

        url = 'https://api.coinmarketcap.com/dexer/v3/dexer/pair-list?base-address=0x2170ed0880ac9a755fd29b2688956bd959f933f8&start=1&limit=10&platform-id=14'
        response = requests.get(url)

        price_ETH_USDT = json.loads(response.text)
        price_ETH_USDT_TO_DICT = dict(price_ETH_USDT)

        item_Ethereum_Token = price_ETH_USDT_TO_DICT['data'][1]['baseToken']['name']
        item_Tether_USD_Token = price_ETH_USDT_TO_DICT['data'][3]['quoteToken']['name']
        item_priceUsd_to_priceETH = price_ETH_USDT_TO_DICT['data'][3]['priceUsd']
        item_priceUsd_to_priceETH_volume = price_ETH_USDT_TO_DICT['data'][3]['volume24h']
        item_priceUsd_to_priceETH_liquidity = price_ETH_USDT_TO_DICT['data'][3]['liquidity']
        item_priceUsd_to_priceETH_priceChange24h = price_ETH_USDT_TO_DICT['data'][3]['priceChange24h']
        item_priceUsd_to_priceETH_liquidityScore = price_ETH_USDT_TO_DICT['data'][3]['liquidityScore']

        tprint('Monitoring',font='standard')

        print(f'{item_Ethereum_Token}>>TO>>{item_Tether_USD_Token}')
        print(f'[+] Price: {item_priceUsd_to_priceETH}')
        print(f'[+] One percent: {float(item_priceUsd_to_priceETH) / 100}')
        print(f'[+] Volume 24h: {item_priceUsd_to_priceETH_volume}')
        print(f'[+] Liquidity: {item_priceUsd_to_priceETH_liquidity}')
        print(f'[+] Price Change 24h: {item_priceUsd_to_priceETH_priceChange24h}')
        print(f'[+] Liquidity Score: {item_priceUsd_to_priceETH_liquidityScore}')

        with open('two.json', 'r') as file:
            last = json.load(file)

        if float(item_priceUsd_to_priceETH) / 100 > float(last['data'][3]['priceUsd'])/100:
            tprint('Warning', font='larry3d')
            print('[!] The exchange rate has increased by 1% in the last hour')
            print(f"[!] Price an hour ago: {float(last['data'][3]['priceUsd'])}")
            print(f"[!] price in relation to one percent: {float(last['data'][3]['priceUsd'])/100}")
            save_one_select()

        elif float(item_priceUsd_to_priceETH) / 100 < float(last['data'][3]['priceUsd'])/100:
            tprint('Warning', font='larry3d')
            print('[!] The exchange rate has fallen by 1% in the last hour')
            print(f"[!] Price an hour ago: {float(last['data'][3]['priceUsd'])}")
            print(f"[!] price in relation to one percent: {float(last['data'][3]['priceUsd'])/100}")
            save_one_select()

        time.sleep(120)

        if __name__ == '__main__':
            Select_Ethereum().select_Ethereum()


def main():
    start()


if __name__ == '__main__':
    main()
