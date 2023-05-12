import requests


async def check_tokens(text, type):
    tokens_list = text.split('\n')
    valid_tokens = []
    for token in tokens_list:
        token = token.replace(' ', '')
        if len(token) != 0:
            headers = {'Authorization': token}
            responce = requests.get(
                'https://discordapp.com/api/v9/users/@me/library', headers=headers)
            if responce.status_code == 200:
                valid_tokens.append(type+':'+token)

    return list(set(valid_tokens))
