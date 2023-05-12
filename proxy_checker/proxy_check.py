import aiohttp
import asyncio
import requests


async def check_proxy_type(session, proxy):
    url = "http://example.com"
    http_proxy = f"http://{proxy}"
    try:
        async with session.get(url, proxy=http_proxy, timeout=5) as response:
            if response.status == 200:
                return (proxy, "HTTP")
    except:
        pass
    socks5_proxy = f"socks5://{proxy}"
    try:
        async with session.get(url, proxy=socks5_proxy, timeout=5) as response:
            if response.status == 200:
                return (proxy, "SOCKS5")
    except:
        return None


async def check_proxies(proxies):
    async with aiohttp.ClientSession() as session:
        tasks = [check_proxy_type(session, proxy) for proxy in proxies]
        results = await asyncio.gather(*tasks)
    valid_proxies = [result for result in results if result]
    return valid_proxies


async def check_proxy(text):

    async def get_proxy_country(proxy):
        response = requests.get(f'http://ipwho.is/{proxy[0]}')
        data = response.json()
        try:
            return data['country_code'].lower()
        except:
            pass

    county_list = ['de', 'us', 'nl']
    proxy_list = text.split('\n')
    clear_proxy_list = []
    end_proxy_list = []
    for proxy in proxy_list:
        proxy = proxy.replace(' ', '')
        if len(proxy) != 0:
            clear_proxy_list.append(proxy)
    clear_proxy_list = list(set(clear_proxy_list))
    hz_kak_nazvat = []
    try:
        for i in clear_proxy_list:
            hz_kak_nazvat.append(i.split(':')[2]+':'+i.split(':')[3])
    except:
        return 'Некрокетно введенные данные'
    valid_proxies = await check_proxies(hz_kak_nazvat)
    for proxy in valid_proxies:
        proxy = list(proxy)
        country_code = await get_proxy_country(proxy[0].split(':'))
        if country_code != None:
            print(f'{country_code}:{proxy[1].lower()}@{proxy[0]}')
            if country_code in county_list:
                for prx in clear_proxy_list:
                    if proxy[0] in prx:
                        nagovnokodil = prx.split(':')
                        end_proxy_list.append(
                            f'{country_code}:{proxy[1].lower()}:{nagovnokodil[0]}:{nagovnokodil[1]}@{nagovnokodil[2]}:{nagovnokodil[3]}')

    return end_proxy_list

# if __name__ == '__main__':
#     asyncio.run(check_proxy("""
#      8.219.97.248:80
# 124.13.181.6:80
# 103.216.103.163:80
# 181.189.135.90:8080
# 13.95.173.197:80
# 158.160.56.149:8080
# 152.69.215.206:80
# 34.106.12.175:8585
# 95.183.140.94:80
# 95.183.140.89:80
# 182.72.203.246:80
# 117.102.81.3:53281
#        """))
