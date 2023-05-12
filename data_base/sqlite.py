import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect('data/new.db')
    cur = db.cursor()

    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS profile
        (
            user_id TEXT PRIMARY KEY NOT NULL, 
            user_name TEXT, 
            balance INTEGER DEFAULT 0, 
            number_of_purchases INTEGER DEFAULT 0
            )''')

    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS history
        (
            user_id TEXT PRIMARY KEY NOT NULL, 
            orders_history TEXT 
            )''')
    db.commit()


async def create_profile(user_id, user_name):
    user = cur.execute(
        f"SELECT 1 FROM profile WHERE user_id == '{user_id}'").fetchone()
    if not user:
        cur.execute(
            f"INSERT INTO profile (user_id, user_name) VALUES(?, ?)", (user_id, user_name))
        cur.execute(
            f"INSERT INTO history (user_id, orders_history) VALUES(?, ?)", (user_id, ''))
        db.commit()


async def get_info(user_id, user_name):
    cur.execute(
        f"""
        UPDATE profile
        SET user_name == '{user_name}'
        WHERE user_id == '{user_id}'
        """)
    user = cur.execute(
        f"SELECT user_id, user_name, balance, number_of_purchases FROM profile WHERE user_id == '{user_id}'").fetchall()
    db.commit()
    return user[0]


async def balance_update(user_id, sum):
    balance = cur.execute(
        f"SELECT balance FROM profile WHERE user_id == '{user_id}'").fetchall()[0][0]
    if int(balance) >= sum:
        cur.execute(
            f"""
            UPDATE profile
            SET balance == balance - {sum}, number_of_purchases = number_of_purchases + 1
            WHERE user_id == '{user_id}'
            """)
        db.commit()
        return True
    else:
        return False


async def edit_vpn_history(user_id, historyy, data):
    history = historyy.split('_')
    user_history = cur.execute(
        f"SELECT orders_history FROM history WHERE user_id == '{user_id}'").fetchall()[0][0]
    if user_history == '':
        cur.execute(
            f"""
            UPDATE history
            SET orders_history == '{history[0].title()} {history[1].title()} {history[2]} {history[3]}:/./login: {data[2]}/./pass: {data[3]}``'
            WHERE user_id == '{user_id}'
            """)
        db.commit()
    else:
        cur.execute(
            f"""
            UPDATE history
            SET orders_history == '{f"{user_history}``{history[0].title()} {history[1].title()} {history[2]} {history[3]}:/./login: {data[2]}/./pass: {data[3]}``"}'
            WHERE user_id == '{user_id}'
            """)
        db.commit()


async def edit_nitro_history(user_id, historyy, data):
    history = historyy.split('_')
    user_history = cur.execute(
        f"SELECT orders_history FROM history WHERE user_id == '{user_id}'").fetchall()[0][0]
    if user_history == '':
        cur.execute(
            f"""
            UPDATE history
            SET orders_history == '{history[0].title()} {history[1].title()} {history[2].title()}:/./{data[1]}``'
            WHERE user_id == '{user_id}'
            """)
        db.commit()
    else:
        cur.execute(
            f"""
            UPDATE history
            SET orders_history == '{f"{user_history}``{history[0].title()} {history[1].title()} {history[2].title()}:/./{data[1]}``"}'
            WHERE user_id == '{user_id}'
            """)
        db.commit()


async def edit_tokens_history(user_id, historyy, data):
    user_history = cur.execute(
        f"SELECT orders_history FROM history WHERE user_id == '{user_id}'").fetchall()[0][0]
    history = historyy.split('t_a')
    if history[0] == 'token1':
        history = 'Токены самые дешевые:'
    elif history[0] == 'token2':
        history = 'Токены от 8 месяцев:'
    elif history[0] == 'token3':
        history = 'Токены 200+ дней:'
    token_str = ''
    for token_lst in data:
        token_str += (token_lst[1]+'/./')
    if user_history == '':
        cur.execute(
            f"""
            UPDATE history
            SET orders_history == '{history}:/./{token_str}``'
            WHERE user_id == '{user_id}'
            """)
        db.commit()
    else:
        cur.execute(
            f"""
            UPDATE history
            SET orders_history == '{f"{user_history}``{history}:/./{token_str}``"}'
            WHERE user_id == '{user_id}'
            """)
        db.commit()


async def edit_proxy_history(user_id, data):
    user_history = cur.execute(
        f"SELECT orders_history FROM history WHERE user_id == '{user_id}'").fetchall()[0][0]
    proxy_str = ''
    country = ''
    for proxy_lst in data:
        if proxy_lst[0] == 'de':
            country = 'Germany'
        elif proxy_lst[0] == 'us':
            country = 'Usa'
        elif proxy_lst[0] == 'nl':
            country = 'Netherlands'
        proxy_str += (f'{proxy_lst[2]}:{proxy_lst[3]}:{proxy_lst[4]}/./')
    if user_history == '':
        cur.execute(
            f"""
            UPDATE history
            SET orders_history == '{country} {proxy_lst[1].upper()}:/./{proxy_str}``'
            WHERE user_id == '{user_id}'
            """)
        db.commit()
    else:
        cur.execute(
            f"""
            UPDATE history
            SET orders_history == '{f"{user_history}``{country} {proxy_lst[1].upper()}:/./{proxy_str}``"}'
            WHERE user_id == '{user_id}'
            """)
        db.commit()


async def get_history(user_id):
    user_history = cur.execute(
        f"SELECT orders_history FROM history WHERE user_id == '{user_id}'").fetchall()[0]
    if user_history[0] == '':
        return 'У вас нет заказов'
    return user_history[0]


async def get_user_id(user_name):
    try:
        user_id = cur.execute(
            f"SELECT user_id FROM profile WHERE user_name == '{user_name}'").fetchone()[0]
        db.commit()
        return int(user_id)
    except:
        return None
