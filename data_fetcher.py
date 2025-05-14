import requests

def get_crypto_data(token):
    try:
        token = token.lower()

        # Получить список монет
        coin_list_url = "https://api.coingecko.com/api/v3/coins/list"
        coin_list = requests.get(coin_list_url).json()

        token_id = None
        for coin in coin_list:
            if token in [coin['id'], coin['symbol'], coin['name'].lower()]:
                token_id = coin['id']
                break

        if not token_id:
            return {"error": f"Token '{token}' not found"}

        # Получить рыночные данные
        market_data_url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
        market_data = requests.get(market_data_url).json()

        price = market_data['market_data']['current_price']['usd']
        market_cap = market_data['market_data']['market_cap']['usd']
        rank = market_data['market_cap_rank']
        name = market_data['name']

        news = f"Latest news about {name} is not available in this demo."

        return {
            "name": name,
            "price": price,
            "market_cap": market_cap,
            "rank": rank,
            "news": news
        }

    except Exception as e:
        return {"error": str(e)}
