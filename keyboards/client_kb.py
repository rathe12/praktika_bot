from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
mb1 = KeyboardButton('Товары 🍭')
mb2 = KeyboardButton('Мой профиль 👤')
mb3 = KeyboardButton('О магазине 📕')
mb4 = KeyboardButton('Соглашение 📜')
mb5 = KeyboardButton('Помощь 🆘')
main_kb.add(mb1).add(mb2).insert(mb3).add(
    mb4).insert(mb5)

product_kb = ReplyKeyboardMarkup(resize_keyboard=True)
pb1 = KeyboardButton('Discord Nitro 🤖')
pb2 = KeyboardButton('Discord токены 🛅')
pb3 = KeyboardButton('Proxy 📶')
pb4 = KeyboardButton('Vpn 🌐')
pb5 = KeyboardButton('Выход в меню 🔙')
product_kb.add(pb1).insert(pb2).add(pb3).insert(
    pb4).add(pb5)

profile_kb = InlineKeyboardMarkup()
pib1 = InlineKeyboardButton(text='История заказов', callback_data='profile_history_of_orders')
pib2 = InlineKeyboardButton(text='Пополнить баланс', callback_data='profile_replenish_the_balance')
profile_kb.add(pib1).insert(pib2)


vpn_kb = InlineKeyboardMarkup()
vib1 = InlineKeyboardButton(text='Nord VPN',
                            callback_data='nord_vpn')
vib2 = InlineKeyboardButton(text='Express VPN',
                            callback_data='express_vpn')
vib3 = InlineKeyboardButton(text='CyberGhost VPN',
                            callback_data='cyberghost_vpn')
vpn_kb.add(vib1).add(vib2).add(vib3)

nord_kb = InlineKeyboardMarkup()
nvib1 = InlineKeyboardButton(
    text='1 месяц | 300р', callback_data='nord_vpn_one_month')
nvib2 = InlineKeyboardButton(
    text='3 месяця | 800р', callback_data='nord_vpn_three_months')
nvib3 = InlineKeyboardButton(
    text='6 месяцев | 1500р', callback_data='nord_vpn_six_months')
nvib4 = InlineKeyboardButton(
    text='Назад', callback_data='exit_to_vpn_menu')
nord_kb.add(nvib1).add(nvib2).add(nvib3).add(nvib4)

express_kb = InlineKeyboardMarkup()
evib1 = InlineKeyboardButton(
    text='1 месяц | 300р', callback_data='express_vpn_one_month')
evib2 = InlineKeyboardButton(
    text='3 месяця | 800р', callback_data='express_vpn_three_months')
evib3 = InlineKeyboardButton(
    text='6 месяцев | 1500р', callback_data='express_vpn_six_months')
express_kb.add(evib1).add(evib2).add(evib3).add(nvib4)

cyberghost_kb = InlineKeyboardMarkup()
cgvib1 = InlineKeyboardButton(
    text='1 месяц | 300р', callback_data='cyberghost_vpn_one_month')
cgvib2 = InlineKeyboardButton(
    text='3 месяця | 800р', callback_data='cyberghost_vpn_three_months')
cgvib3 = InlineKeyboardButton(
    text='6 месяцев | 1500р', callback_data='cyberghost_vpn_six_months')
cyberghost_kb.add(cgvib1).add(cgvib2).add(cgvib3).add(nvib4)


nitro_kb = InlineKeyboardMarkup()
nib1 = InlineKeyboardButton(
    text='Nitro Full Monthly | 250р', callback_data='nitro_full_monthly')
nib2 = InlineKeyboardButton(
    text='Nitro Classic Monthly | 190р', callback_data='nitro_classic_monthly')
nib3 = InlineKeyboardButton(
    text='Nitro Full Yearly | 1250р', callback_data='nitro_full_yearly')
nib4 = InlineKeyboardButton(
    text='Nitro Classic Yearly | 700р', callback_data='nitro_classic_yearly')
nitro_kb.add(nib1).add(nib2).add(nib3).add(nib4)




tokens_kb = InlineKeyboardMarkup()
tib1 = InlineKeyboardButton(
    text='Discord токены | 2р', callback_data='token1')
tib2 = InlineKeyboardButton(
    text='Discord токены | 3р', callback_data='token2')
tib3 = InlineKeyboardButton(
    text='Discord токены | 5р', callback_data='token3')
tokens_kb.add(tib1).add(tib2).add(tib3)

token1_kb = InlineKeyboardMarkup()
t1ib1 = InlineKeyboardButton(
    text='1', callback_data='token1t_amount1')
t1ib2 = InlineKeyboardButton(
    text='5', callback_data='token1t_amount5')
t1ib3 = InlineKeyboardButton(
    text='10', callback_data='token1t_amount10')
t1ib4 = InlineKeyboardButton(
    text=' Другое количество', callback_data='token1t_amount_user')
t1ib5 = InlineKeyboardButton(
    text='Назад', callback_data='exit_to_tokens_menu')
token1_kb.insert(t1ib1).insert(t1ib2).insert(t1ib3).add(t1ib4).add(t1ib5)

token2_kb = InlineKeyboardMarkup()
t2ib1 = InlineKeyboardButton(
    text='1', callback_data='token2t_amount1')
t2ib2 = InlineKeyboardButton(
    text='5', callback_data='token2t_amount5')
t2ib3 = InlineKeyboardButton(
    text='10', callback_data='token2t_amount10')
t2ib4 = InlineKeyboardButton(
    text=' Другое количество', callback_data='token2t_amount_user')
token2_kb.insert(t2ib1).insert(t2ib2).insert(t2ib3).add(t2ib4).add(t1ib5)

token3_kb = InlineKeyboardMarkup()
t3ib1 = InlineKeyboardButton(
    text='1', callback_data='token3t_amount1')
t3ib2 = InlineKeyboardButton(
    text='5', callback_data='token3t_amount5')
t3ib3 = InlineKeyboardButton(
    text='10', callback_data='token3t_amount10')
t3ib4 = InlineKeyboardButton(
    text=' Другое количество', callback_data='token3t_amount_user')
token3_kb.insert(t3ib1).insert(t3ib2).insert(t3ib3).add(t3ib4).add(t1ib5)


proxy_kb = InlineKeyboardMarkup()
pib1 = InlineKeyboardButton(
    text = 'Германия', callback_data='proxy_de')
pib2 = InlineKeyboardButton(
    text = 'США', callback_data='proxy_us')
pib3 = InlineKeyboardButton(
    text = 'Нидерланды', callback_data='proxy_nl')
proxy_kb.add(pib1).add(pib2).add(pib3)

proxy_de_kb = InlineKeyboardMarkup()
pdeib1 = InlineKeyboardButton(
    text='SOCKS5 | 18р', callback_data='proxy_de_socks5')
pdeib2 = InlineKeyboardButton(
    text='HTTP | 18р', callback_data='proxy_de_http')
pdeib5 = InlineKeyboardButton(
    text='Назад', callback_data='exit_to_proxy_menu')
proxy_de_kb.insert(pdeib1).insert(pdeib2).add(pdeib5)

proxy_de_socks5_kb = InlineKeyboardMarkup()
pdesib1 = InlineKeyboardButton(
    text='1', callback_data='proxy_de_socks5_amount1')
pdesib2 = InlineKeyboardButton(
    text='5', callback_data='proxy_de_socks5_amount5')
pdesib3 = InlineKeyboardButton(
    text='10', callback_data='proxy_de_socks5_amount10')
pdesib4 = InlineKeyboardButton(
    text=' Другое количество', callback_data='proxy_de_socks5_amount_user')
pdesib5 = InlineKeyboardButton(
    text='Назад', callback_data='exit_to_proxy_de_menu')
proxy_de_socks5_kb.insert(pdesib1).insert(pdesib2).insert(pdesib3).add(pdesib4).add(pdesib5)

proxy_de_http_kb = InlineKeyboardMarkup()
pdehib1 = InlineKeyboardButton(
    text='1', callback_data='proxy_de_http_amount1')
pdehib2 = InlineKeyboardButton(
    text='5', callback_data='proxy_de_http_amount5')
pdehib3 = InlineKeyboardButton(
    text='10', callback_data='proxy_de_http_amount10')
pdehib4 = InlineKeyboardButton(
    text=' Другое количество', callback_data='proxy_de_http_amount_user')
proxy_de_http_kb.insert(pdehib1).insert(pdehib2).insert(pdehib3).add(pdehib4).add(pdesib5)

proxy_us_kb = InlineKeyboardMarkup()
pueib1 = InlineKeyboardButton(
    text='SOCKS5 | 25р', callback_data='proxy_us_socks5')
pueib2 = InlineKeyboardButton(
    text='HTTP | 25р', callback_data='proxy_us_http')
pueib5 = InlineKeyboardButton(
    text='Назад', callback_data='exit_to_proxy_menu')
proxy_us_kb.insert(pueib1).insert(pueib2).add(pueib5)

proxy_us_socks5_kb = InlineKeyboardMarkup()
puesib1 = InlineKeyboardButton(
    text='1', callback_data='proxy_us_socks5_amount1')
puesib2 = InlineKeyboardButton(
    text='5', callback_data='proxy_us_socks5_amount5')
puesib3 = InlineKeyboardButton(
    text='10', callback_data='proxy_us_socks5_amount10')
puesib4 = InlineKeyboardButton(
    text=' Другое количество', callback_data='proxy_us_socks5_amount_user')
puesib5 = InlineKeyboardButton(
    text='Назад', callback_data='exit_to_proxy_us_menu')
proxy_us_socks5_kb.insert(puesib1).insert(puesib2).insert(puesib3).add(puesib4).add(puesib5)

proxy_us_http_kb = InlineKeyboardMarkup()
puehib1 = InlineKeyboardButton(
    text='1', callback_data='proxy_us_http_amount1')
puehib2 = InlineKeyboardButton(
    text='5', callback_data='proxy_us_http_amount5')
puehib3 = InlineKeyboardButton(
    text='10', callback_data='proxy_us_http_amount10')
puehib4 = InlineKeyboardButton(
    text=' Другое количество', callback_data='proxy_us_http_amount_user')
proxy_us_http_kb.insert(puehib1).insert(puehib2).insert(puehib3).add(puehib4).add(puesib5)

proxy_nl_kb = InlineKeyboardMarkup()
pueib1 = InlineKeyboardButton(
    text='SOCKS5 | 17р', callback_data='proxy_nl_socks5')
pueib2 = InlineKeyboardButton(
    text='HTTP | 17р', callback_data='proxy_nl_http')
pueib5 = InlineKeyboardButton(
    text='Назад', callback_data='exit_to_proxy_menu')
proxy_nl_kb.insert(pueib1).insert(pueib2).add(pueib5)

proxy_nl_socks5_kb = InlineKeyboardMarkup()
puesib1 = InlineKeyboardButton(
    text='1', callback_data='proxy_nl_socks5_amount1')
puesib2 = InlineKeyboardButton(
    text='5', callback_data='proxy_nl_socks5_amount5')
puesib3 = InlineKeyboardButton(
    text='10', callback_data='proxy_nl_socks5_amount10')
puesib4 = InlineKeyboardButton(
    text=' Другое количество', callback_data='proxy_nl_socks5_amount_user')
puesib5 = InlineKeyboardButton(
    text='Назад', callback_data='exit_to_proxy_nl_menu')
proxy_nl_socks5_kb.insert(puesib1).insert(
    puesib2).insert(puesib3).add(puesib4).add(puesib5)

proxy_nl_http_kb = InlineKeyboardMarkup()
puehib1 = InlineKeyboardButton(
    text='1', callback_data='proxy_nl_http_amount1')
puehib2 = InlineKeyboardButton(
    text='5', callback_data='proxy_nl_http_amount5')
puehib3 = InlineKeyboardButton(
    text='10', callback_data='proxy_nl_http_amount10')
puehib4 = InlineKeyboardButton(
    text=' Другое количество', callback_data='proxy_nl_http_amount_user')
proxy_nl_http_kb.insert(puehib1).insert(
    puehib2).insert(puehib3).add(puehib4).add(puesib5)
