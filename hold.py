import requests
import os

cookies = {
    'cf_clearance': os.getenv("CF_CLEARANCE"),
    '__Secure-better-auth.session_token': os.getenv("SECURE_BETTER_AUTH"),
}

headers = {
    'User-Agent': os.getenv("USER_AGENT"),
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://rugplay.com/coin/HOLDCONST',
    'Content-Type': 'application/json',
    'Origin': f'https://rugplay.com/coin/HOLDCONST',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0',
}

def sell_coin(amt: float):
    data = requests.get("https://rugplay.com/api/coin/HOLDCONST/", cookies=cookies, headers=headers).json()

    json_data = {
        'type': 'SELL',
        'amount': float(amt/float(data["coin"]["currentPrice"])),
    }

    print(json_data)
    data = requests.post(f'https://rugplay.com/api/coin/HOLDCONST/trade', cookies=cookies, headers=headers, json=json_data)
    print(data.json())

def buy_coin(amt: float):
    json_data = {
        'type': 'BUY',
        'amount': float(amt),
    }

    print(json_data)
    data = requests.post(f'https://rugplay.com/api/coin/HOLDCONST/trade', cookies=cookies, headers=headers, json=json_data)
    print(data.json())

def get_sell_amt():
    data = requests.get("https://rugplay.com/api/coin/HOLDCONST/", cookies=cookies, headers=headers).json()
    current = float(data["coin"]["poolBaseCurrencyAmount"])

    return 5000000-current

if __name__ == '__main__':
    while True:
        amt = get_sell_amt()
        try:
            if amt == 0:
                continue
            elif amt < 0:
                sell_coin(amt.__abs__())
            else:
                buy_coin(amt.__abs__())
        except Exception as e:
            print(f"[ERROR] {e}")
            continue

        print(f"off by {amt}")