import asyncio
import sys

import aiohttp
from datetime import datetime, timedelta

async def get_exchange_rates(date):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            rates = {}
            for currency in data['exchangeRate']:
                if currency['currency'] in ['USD', 'EUR']:
                    rates[currency['currency']] = {'buy': float(currency['purchaseRate']),
                                                   'sell': float(currency['saleRateNB'])}
            return rates

async def main(num_it=None):
    if not num_it:
        num_it = int(input('Введите за сколько дней Вы бы хотели узнать курс валют: '))
    else:
        num_it = int(num_it)
    while True:
        if num_it <= 10:
            today = datetime.today()
            for i in range(num_it):
                date = (today - timedelta(days=i)).strftime('%d.%m.%Y')
                rates = await get_exchange_rates(date)
                print(f"Курсы валют на {date}:")
                for currency, values in rates.items():
                    print(f"{currency}: Покупка - {values['buy']}, Продажа - {values['sell']}")
            break
        else:
            print('Вы можете узнать курс не более чем на 10 дне от текущей даты.')
            num_it = int(input('Введите за сколько дней Вы бы хотели узнать курс валют: '))
            continue

if __name__ == '__main__':
    try:
        num_it = sys.argv[1]
    except:
        num_it=None
    asyncio.run(main(num_it))
