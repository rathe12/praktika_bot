from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
ab1 = KeyboardButton('Посмотреть иcторию покупок')
ab2 = KeyboardButton('Добавить товар')
ab3 = KeyboardButton('Выход')
admin_kb.add(ab1).insert(ab2).add(ab3)

add_products_kb = ReplyKeyboardMarkup(resize_keyboard=True)
pb1 = KeyboardButton('Добавить прокси')
pb2 = KeyboardButton('Добавить нитро')
pb3 = KeyboardButton('Добавить токены')
pb4 = KeyboardButton('Добавить впн')
pb5 = KeyboardButton('Назад')
add_products_kb.add(pb1).insert(pb2).add(pb3).insert(pb4).add(pb5)

add_tokens_kb = InlineKeyboardMarkup()
tib1 = InlineKeyboardButton(text='Тип 1',
                            callback_data='add_token1')
tib2 = InlineKeyboardButton(text='Тип 2',
                            callback_data='add_token2')
tib3 = InlineKeyboardButton(text='Тип 3',
                            callback_data='add_token3')
tib4 = InlineKeyboardButton(text='Закрыть',
                            callback_data='add_end')
add_tokens_kb.add(tib1).add(tib2).add(tib3).add(tib4)


add_vpn_kb = InlineKeyboardMarkup()
vib1 = InlineKeyboardButton(text='nord',
                            callback_data='add_vpn_nord')
vib2 = InlineKeyboardButton(text='express',
                            callback_data='add_vpn_express')
vib3 = InlineKeyboardButton(text='cyberghost',
                            callback_data='add_vpn_cyberghost')
add_vpn_kb.add(vib1).add(vib2).add(vib3).add(tib4)

nord_kb = InlineKeyboardMarkup()
nvib1 = InlineKeyboardButton(
    text='1 месяц | nord_vpn', callback_data='nord_vpn_one_month')
nvib2 = InlineKeyboardButton(
    text='3 месяця | nord_vpn', callback_data='nord_vpn_three_months')
nvib3 = InlineKeyboardButton(
    text='6 месяцев | nord_vpn', callback_data='nord_vpn_six_months')
nvib4 = InlineKeyboardButton(
    text='Назад', callback_data='exit_to_vpn_menu')
nord_kb.add(nvib1).add(nvib2).add(nvib3).add(nvib4)

express_kb = InlineKeyboardMarkup()
evib1 = InlineKeyboardButton(
    text='1 месяц | express', callback_data='express_vpn_one_month')
evib2 = InlineKeyboardButton(
    text='3 месяця | express', callback_data='express_vpn_three_months')
evib3 = InlineKeyboardButton(
    text='6 месяцев | express', callback_data='express_vpn_six_months')
express_kb.add(evib1).add(evib2).add(evib3).add(nvib4)

cyberghost_kb = InlineKeyboardMarkup()
cgvib1 = InlineKeyboardButton(
    text='1 месяц | cyberghost', callback_data='cyberghost_vpn_one_month')
cgvib2 = InlineKeyboardButton(
    text='3 месяця | cyberghost', callback_data='cyberghost_vpn_three_months')
cgvib3 = InlineKeyboardButton(
    text='6 месяцев | cyberghost', callback_data='cyberghost_vpn_six_months')
cyberghost_kb.add(cgvib1).add(cgvib2).add(cgvib3).add(nvib4)
