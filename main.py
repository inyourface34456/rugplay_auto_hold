import requests
import time
import os

cookies = {
    'cf_clearance': os.getenv("CF_CLEARANCE"),
    '__Secure-better-auth.session_token': os.getenv("SECURE_BETTER_AUTH"),
}

def get_portfolio_data():
    headers = {
        'User-Agent': os.getenv("USER_AGENT"),
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': "https://rugplay.com",
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=4',
    }

    return requests.get('https://rugplay.com/api/portfolio/total', cookies=cookies, headers=headers).json()

def sell_coin(symbol: str, amt: int):
    headers = {
        'User-Agent': os.getenv("USER_AGENT"),
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://rugplay.com/coin/6N2M2ZIXML',
        'Content-Type': 'application/json',
        'Origin': f'https://rugplay.com/coin/{symbol}',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
    }

    json_data = {
        'type': 'SELL',
        'amount': amt,
    }

    requests.post(f'https://rugplay.com/api/coin/{symbol}/trade', cookies=cookies, headers=headers, json=json_data)


if __name__ == '__main__':
    response = get_portfolio_data()
    coin_names = []
    for i in response["coinHoldings"]:
        # print(i["symbol"])
        if i["symbol"] == "IDEGAF" or i["symbol"] == "IDEGAF":
            print("skipped idegaf")
            continue
        sell_coin(i["symbol"], i["quantity"])
        print(f"sold ${i['symbol']} {i['quantity']}")
        time.sleep(.05)

