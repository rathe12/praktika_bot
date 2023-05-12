from create_bot import bot
from data_base import get_user_id, get_history
from aiogram import types, Dispatcher
from keyboards import admin_kb, main_kb, add_products_kb, add_tokens_kb, add_vpn_kb, nord_kb, express_kb, cyberghost_kb
from aiogram.dispatcher import FSMContext
from proxy_checker import check_proxy
from aiogram.dispatcher.filters.state import StatesGroup, State
from token_checker import check_tokens
import random
import string
import aiofiles


class AdminStatesGroup(StatesGroup):

    admin = State()
    view_user_purchase_history = State()
    random_log_pass = State()
    add_proxy = State()
    add_tokens = State()
    add_token1 = State()
    add_token2 = State()
    add_token3 = State()
    add_vpn = State()
    nord_vpn_one_month = State()
    nord_vpn_three_months = State()
    nord_vpn_six_months = State()
    express_vpn_one_month = State()
    express_vpn_three_months = State()
    express_vpn_six_months = State()
    cyberghost_vpn_one_month = State()
    cyberghost_vpn_three_months = State()
    cyberghost_vpn_six_months = State()


async def admin_command(message: types.Message):
    await bot.send_message(message.from_user.id, '<em>Переход в режим администрирования</em>', 'HTML', reply_markup=admin_kb)
    await AdminStatesGroup.admin.set()


async def random_command(message: types.Message):
    await bot.send_message(message.from_user.id, '<em>Переход в режим рандомного заполнения прокси</em>', 'HTML')
    await AdminStatesGroup.random_log_pass.set()


async def admin(message: types.Message, state: FSMContext):
    if message.text == 'Выход':
        await bot.send_message(
            message.from_user.id, '<em>Выход из режима администрирования</em>', 'HTML', reply_markup=main_kb)
        await state.finish()
    if message.text == 'Назад':
        await bot.send_message(
            message.from_user.id, '<em>Выход из режима добавления товара</em>', 'HTML', reply_markup=admin_kb)
    elif message.text == 'Посмотреть иcторию покупок':
        await bot.send_message(message.from_user.id, 'Введите ник пользователя')
        await AdminStatesGroup.view_user_purchase_history.set()
    elif message.text == 'Добавить товар':
        await bot.send_message(message.from_user.id, '<em>Переход в режим добавления товара</em>', 'HTML', reply_markup=add_products_kb)
    elif message.text == 'Добавить прокси':
        await AdminStatesGroup.add_proxy.set()
        await bot.send_message(message.from_user.id, '<em>Отправьте прокси(по одной в строке)</em>', 'HTML')
    elif message.text == 'Добавить токены':
        await AdminStatesGroup.add_tokens.set()
        await bot.send_message(message.from_user.id, '<em>Выберите тип токенов</em>', 'HTML', reply_markup=add_tokens_kb)
    elif message.text == 'Добавить впн':
        await AdminStatesGroup.add_vpn.set()
        await bot.send_message(message.from_user.id, '<em>Выберите тип впн</em>', 'HTML', reply_markup=add_vpn_kb)


async def rando(message: types.Message):
    async def generate_random_string(length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    proxy_list = message.text.split('\n')
    clear_proxy_str = ''
    for proxy in proxy_list:
        proxy = proxy.replace(' ', '')
        if len(proxy) != 0:
            clear_proxy_str += f'{await generate_random_string(5)}:{await generate_random_string(5)}:{proxy}\n'
    await bot.send_message(message.from_user.id, clear_proxy_str)
    await AdminStatesGroup.admin.set()


async def add_proxy(message: types.Message):
    proxy_list = await check_proxy(message.text)
    if proxy_list == 'Некрокетно введенные данные':
        await bot.send_message(message.from_user.id, f'<em>{proxy_list}</em>', 'HTML')
    else:
        async with aiofiles.open('data/proxy.txt', 'r') as file:
            lines = await file.readlines()
        for line in lines:
            for proxy in proxy_list:
                if proxy.split(':')[3] in line:
                    proxy_list.remove(proxy)
        async with aiofiles.open('data/proxy.txt', 'a') as file:
            await file.writelines('\n')
            for proxy in proxy_list:
                await file.writelines(proxy+'\n')
        await bot.send_message(message.from_user.id, f'<em>Добавлено {len(proxy_list)} прокси</em>', 'HTML')
    await AdminStatesGroup.admin.set()


async def view_user_history(message: types.Message):
    user_name = str(message.text.lower())
    user_id = await get_user_id(user_name)
    if user_id == None:
        await bot.send_message(message.from_user.id, f'Пользователь @{user_name} не пользовался ботом')
        await AdminStatesGroup.admin.set()
        return
    history = await get_history(user_id)
    if history == 'У вас нет заказов':
        await bot.send_message(message.from_user.id, f'У пользователя @{user_name} нет покупок')
        await AdminStatesGroup.admin.set()
        return
    purchase_str = ''
    for purchase in history.split('``'):
        if len(purchase) != 0:
            for i in purchase.split('/./'):
                purchase_str += '\n' + i
            purchase_str += '_'*40+'\n'
    await bot.send_message(message.from_user.id, f'Покупки пользователя @{user_name}:\n\n{purchase_str}')
    await AdminStatesGroup.admin.set()


async def add_tokens_callback(callback: types.CallbackQuery):
    if callback.data == 'add_end':
        await callback.message.delete()
        await AdminStatesGroup.admin.set()
    elif callback.data == 'add_token1':
        await bot.send_message(callback.from_user.id, '<em>Отправьте токены(по одной в строке)</em>', 'HTML')
        await AdminStatesGroup.add_token1.set()
    elif callback.data == 'add_token2':
        await bot.send_message(callback.from_user.id, '<em>Отправьте токены(по одной в строке)</em>', 'HTML')
        await AdminStatesGroup.add_token2.set()
    elif callback.data == 'add_token3':
        await bot.send_message(callback.from_user.id, '<em>Отправьте токены(по одной в строке)</em>', 'HTML')
        await AdminStatesGroup.add_token3.set()


async def add_tokens(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    try:
        if current_state == 'AdminStatesGroup:add_token1':
            token_list = await check_tokens(message.text, 'token1')
        elif current_state == 'AdminStatesGroup:add_token2':
            token_list = await check_tokens(message.text, 'token2')
        elif current_state == 'AdminStatesGroup:add_token3':
            token_list = await check_tokens(message.text, 'token3')
        async with aiofiles.open('data/tokens.txt', 'r') as file:
            lines = await file.readlines()
        for line in lines:
            for token in token_list:
                if token.split(':')[1] in line:
                    token_list.remove(token)
        async with aiofiles.open('data/tokens.txt', 'a') as file:
            await file.writelines('\n')
            for token in token_list:
                await file.writelines(token+'\n')
        await bot.send_message(message.from_user.id, f'<em>Добавлено {len(token_list)} токенов</em>', 'HTML')
    except:
        await bot.send_message(message.from_user.id, 'Произошла ошибка', 'HTML')
    await AdminStatesGroup.admin.set()


async def add_vpn_callback(callback: types.CallbackQuery):
    if callback.data == 'add_end':
        await callback.message.delete()
        await AdminStatesGroup.admin.set()
    if callback.data == 'exit_to_vpn_menu':
        await callback.message.edit_reply_markup(reply_markup=add_vpn_kb)
    elif callback.data == 'add_vpn_nord':
        await callback.message.edit_reply_markup(reply_markup=nord_kb)
    elif callback.data == 'add_vpn_express':
        await callback.message.edit_reply_markup(reply_markup=express_kb)
    elif callback.data == 'add_vpn_cyberghost':
        await callback.message.edit_reply_markup(reply_markup=cyberghost_kb)

    elif callback.data == 'nord_vpn_one_month':
        await bot.send_message(callback.from_user.id, '<em>Отправьте аккаунты впн(по одному в строке)</em>', 'HTML')
        await AdminStatesGroup.nord_vpn_one_month.set()
    elif callback.data == 'nord_vpn_three_months':
        await bot.send_message(callback.from_user.id, '<em>Отправьте аккаунты впн(по одному в строке)</em>', 'HTML')
        await AdminStatesGroup.nord_vpn_three_months.set()
    elif callback.data == 'nord_vpn_six_months':
        await bot.send_message(callback.from_user.id, '<em>Отправьте аккаунты впн(по одному в строке)</em>', 'HTML')
        await AdminStatesGroup.nord_vpn_six_months.set()

    elif callback.data == 'express_vpn_one_month':
        await bot.send_message(callback.from_user.id, '<em>Отправьте аккаунты впн(по одному в строке)</em>', 'HTML')
        await AdminStatesGroup.express_vpn_one_month.set()
    elif callback.data == 'express_vpn_three_months':
        await bot.send_message(callback.from_user.id, '<em>Отправьте аккаунты впн(по одному в строке)</em>', 'HTML')
        await AdminStatesGroup.express_vpn_three_months.set()
    elif callback.data == 'express_vpn_six_months':
        await bot.send_message(callback.from_user.id, '<em>Отправьте аккаунты впн(по одному в строке)</em>', 'HTML')
        await AdminStatesGroup.express_vpn_six_months.set()

    elif callback.data == 'cyberghost_vpn_one_month':
        await bot.send_message(callback.from_user.id, '<em>Отправьте аккаунты впн(по одному в строке)</em>', 'HTML')
        await AdminStatesGroup.cyberghost_vpn_one_month.set()
    elif callback.data == 'cyberghost_vpn_three_months':
        await bot.send_message(callback.from_user.id, '<em>Отправьте аккаунты впн(по одному в строке)</em>', 'HTML')
        await AdminStatesGroup.cyberghost_vpn_three_months.set()
    elif callback.data == 'cyberghost_vpn_six_months':
        await bot.send_message(callback.from_user.id, '<em>Отправьте аккаунты впн(по одному в строке)</em>', 'HTML')
        await AdminStatesGroup.cyberghost_vpn_six_months.set()


async def add_vpn(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    async def add_vpn_in_file(text, type, time):
        vpn_list = text.split('\n')
        clear_vpn_list = []
        for vpn in vpn_list:
            vpn = vpn.replace(' ', '')
            if len(vpn) != 0:
                clear_vpn_list.append(f'{type}:{time}:{vpn}')
        return list(set(clear_vpn_list))

    try:
        if current_state == 'AdminStatesGroup:nord_vpn_one_month':
            vpn_list = await add_vpn_in_file(message.text, 'nord', '1m')
        elif current_state == 'AdminStatesGroup:nord_vpn_three_months':
            vpn_list = await add_vpn_in_file(message.text, 'nord', '3m')
        elif current_state == 'AdminStatesGroup:nord_vpn_six_months':
            vpn_list = await add_vpn_in_file(message.text, 'nord', '6m')

        elif current_state == 'AdminStatesGroup:express_vpn_one_month':
            vpn_list = await add_vpn_in_file(message.text, 'express', '1m')
        elif current_state == 'AdminStatesGroup:express_vpn_three_months':
            vpn_list = await add_vpn_in_file(message.text, 'express', '3m')
        elif current_state == 'AdminStatesGroup:express_vpn_six_months':
            vpn_list = await add_vpn_in_file(message.text, 'express', '6m')

        elif current_state == 'AdminStatesGroup:cyberghost_vpn_one_month':
            vpn_list = await add_vpn_in_file(message.text, 'cyberghost', '1m')
        elif current_state == 'AdminStatesGroup:cyberghost_vpn_three_months':
            vpn_list = await add_vpn_in_file(message.text, 'cyberghost', '3m')
        elif current_state == 'AdminStatesGroup:cyberghost_vpn_six_months':
            vpn_list = await add_vpn_in_file(message.text, 'cyberghost', '6m')

        async with aiofiles.open('data/vpn.txt', 'r') as file:
            lines = await file.readlines()
        for line in lines:
            for vpn in vpn_list:
                if vpn.split(':')[2] in line:
                    print
                    vpn_list.remove(vpn)
        async with aiofiles.open('data/vpn.txt', 'a') as file:
            await file.writelines('\n')
            for vpn in vpn_list:
                await file.writelines(vpn+'\n')
        await bot.send_message(message.from_user.id, f'<em>Добавлено {len(vpn_list)} аккаунтов впн</em>', 'HTML')
    except Exception as e:
        print(e)
        await bot.send_message(message.from_user.id, 'Произошла ошибка', 'HTML')
    await AdminStatesGroup.admin.set()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_command, lambda message:
                                message.from_user.id == 546706778, commands=['admin'])
    dp.register_message_handler(random_command, lambda message:
                                message.from_user.id == 546706778, commands=['random'], state='*')
    dp.register_message_handler(admin, state=AdminStatesGroup.admin)
    dp.register_message_handler(rando, state=AdminStatesGroup.random_log_pass)
    dp.register_message_handler(
        add_proxy, state=AdminStatesGroup.add_proxy)
    dp.register_message_handler(
        view_user_history, state=AdminStatesGroup.view_user_purchase_history)
    dp.register_callback_query_handler(
        add_tokens_callback, state=AdminStatesGroup.add_tokens)
    dp.register_message_handler(
        add_tokens, state=AdminStatesGroup.add_token1)
    dp.register_message_handler(
        add_tokens, state=AdminStatesGroup.add_token2)
    dp.register_message_handler(
        add_tokens, state=AdminStatesGroup.add_token3)
    dp.register_callback_query_handler(
        add_vpn_callback, state=AdminStatesGroup.add_vpn)

    dp.register_message_handler(
        add_vpn, state=AdminStatesGroup.nord_vpn_one_month)
    dp.register_message_handler(
        add_vpn, state=AdminStatesGroup.nord_vpn_three_months)
    dp.register_message_handler(
        add_vpn, state=AdminStatesGroup.nord_vpn_six_months)

    dp.register_message_handler(
        add_vpn, state=AdminStatesGroup.express_vpn_one_month)
    dp.register_message_handler(
        add_vpn, state=AdminStatesGroup.express_vpn_three_months)
    dp.register_message_handler(
        add_vpn, state=AdminStatesGroup.express_vpn_six_months)

    dp.register_message_handler(
        add_vpn, state=AdminStatesGroup.cyberghost_vpn_one_month)
    dp.register_message_handler(
        add_vpn, state=AdminStatesGroup.cyberghost_vpn_three_months)
    dp.register_message_handler(
        add_vpn, state=AdminStatesGroup.cyberghost_vpn_six_months)
