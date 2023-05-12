from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext 
from aiogram.dispatcher.filters.state import StatesGroup, State
import aiofiles
from create_bot import bot
from data_base import create_profile, get_info, balance_update, edit_vpn_history, edit_nitro_history,  edit_tokens_history, edit_proxy_history,get_history
from keyboards import main_kb, product_kb, profile_kb, vpn_kb, nord_kb, express_kb, cyberghost_kb, nitro_kb, tokens_kb, token1_kb, token2_kb, token3_kb, proxy_kb, proxy_de_kb, proxy_de_socks5_kb, proxy_de_http_kb, proxy_us_kb, proxy_us_socks5_kb, proxy_us_http_kb, proxy_nl_kb, proxy_nl_socks5_kb, proxy_nl_http_kb


AGREEMENT = """Соглашение от 20.10.2021:
1: Покупая любую услугу, Вы автоматически подтверждаете тот факт, что полностью ознакомились с данным официальным соглашением.
2.1: Возрат денег сделать возможно, но до того, как продавец сделает заказ у поставщика.
2.2: Выдача товаров может длиться от 1 дня, до 10. Если прошло более 10-и дней и товара Вы не получили, Вы в праве получить возврат денег
2.3: Если покупатель ведет себя неподобающе во время проведения сделки (Оскорбление, неадекватное поведение), продавец в праве отказать в оказании услуги без возможности возврата средств.
3.1: В зависимости от платформы, подписка может длиться менее 30 дней, 6 или 12 месяцев.
3.2: Незнание соглашения не освобождает от ответственности!
3.3: Возможны откаты.
3.4: Активация сразу.
3.5: Комиссию с оплаты всегда на себя берёт покупатель.
4.1: Продавец оставляет за собой право изменить соглашение в одностороннем порядке, при этом уведомление покупателей не обязательно.
4.2: Если продавец дал Вам товар в долг, Вы обязуетесь его вернуть в течении назначенного времени.
4.3: Округление всегда берёт на себя покупатель. То есть, если общая сумма к оплате к примеру 37,51, то покупатель оплачивает 38 рублей.

(Пункты под номером 2 относятся к случаю, когда товара нет в боте, и он приобретается через продавца)"""

DESCRIPTION = """Вы ищете надежный и доступный способ обеспечить свою анонимность и безопасность в интернете? Тогда наш магазин аккаунтов vpn, proxy и дискорд токенов для вас! У нас вы найдете широкий выбор качественных и проверенных сервисов, которые позволят вам подключаться к любым сайтам и приложениям без ограничений и рисков. Наш магазин предлагает вам:

• Аккаунты vpn🌐 - виртуальные частные сети, которые шифруют ваш трафик и скрывают ваше местоположение от посторонних глаз. Вы можете выбрать любую страну для подключения и наслаждаться свободой интернета.

• Аккаунты proxy📶 - прокси-серверы, которые перенаправляют ваш запрос через другой компьютер, изменяя ваш IP-адрес и обходя блокировки. Вы можете использовать прокси для разных целей, например, для парсинга данных, сбора информации или рекламы.

• Аккаунты дискорд нитро🤖 - премиум-подписки, которые дают вам дополнительные функции и бонусы на платформе Discord, такие как анимированный аватар, кастомный тег, больше эмодзи, улучшенное качество звука и видео, бесплатные игры и многое другое.

• Дискорд токены🛅 - уникальные коды, которые дают вам доступ к платформе Discord, где вы можете общаться с другими пользователями по голосу, видео или тексту. Вы можете создавать или присоединяться к различным серверам по интересам, играм или работе.

Все наши аккаунты гарантированно работают и имеют низкую цену. Вы можете купить их одним кликом и получить их мгновенно. Наша поддержка всегда готова ответить на ваши вопросы и помочь вам с любыми проблемами. Не упустите свой шанс стать анонимным и безопасным в интернете с нашим магазином <b>Praktika shop!</b> """


class ClientStatesGroup(StatesGroup):

    token1t_anumber_of_tokens = State()
    token2t_anumber_of_tokens = State()
    token3t_anumber_of_tokens = State()


    proxy_de_socks5_amount_user = State()
    proxy_de_http_amount_user = State()

    proxy_us_socks5_amount_user = State()
    proxy_us_http_amount_user = State()

    proxy_nl_socks5_amount_user = State()
    proxy_nl_http_amount_user = State()


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, '<em>Вас приветствует бот магазина Praktika</em>', 'HTML',
                           reply_markup=main_kb)
    await message.delete()
    await create_profile(message.from_user.id, message.from_user.username)


# @dp.message_handler(state = ClientStatesGroup.token1t_anumber_of_tokens)
# @dp.message_handler(state = ClientStatesGroup.token2t_anumber_of_tokens)
# @dp.message_handler(state = ClientStatesGroup.token3t_anumber_of_tokens)
async def number_of_tokens(message: types.Message, state: FSMContext):
    async def buy_token(type, count):
        async with aiofiles.open('data/tokens.txt', 'r') as file:
            lines = await file.readlines()
            lines_list = []
            necessary_list = []
            data = []
            for line in lines:
                if type.split('t_a')[0] in line:
                    necessary_list.append(line)
                else:
                    lines_list.append(line)
            if necessary_list == []:
                await bot.send_message(message.from_user.id,'Товар закончился')
                await message.delete()   
                return
            try:
                for i in range(0,count):
                    data.append(necessary_list.pop(0).split(':'))
            except:
                await bot.send_message(message.from_user.id,'Товара осталось меньше заданного')
                return
            async with aiofiles.open('data/tokens.txt', 'w') as file:
                necessary_list.append('\n')
                await file.writelines(necessary_list + lines_list)
            token_str = ''
            for token_lst in data:
                token_str += token_lst[1] + '\n'
            await bot.send_message(message.from_user.id,f'Ваш товар:\n{token_str}')
            await edit_tokens_history(message.from_user.id, type, data) 
            await message.delete()
    
    async def not_enough_money():
        await bot.send_message(message.from_user.id,'Не хватает денег на балансе')

    try:
        current_state = await state.get_state()  
        count = int(message.text) 

        if current_state == 'ClientStatesGroup:token1t_anumber_of_tokens':
            examination = await balance_update(message.from_user.id, 2*count)
            if examination:
                await buy_token('token1t_amount_user',count)
            else:
                await not_enough_money()
        elif current_state == 'ClientStatesGroup:token2t_anumber_of_tokens':
            examination = await balance_update(message.from_user.id, 3*count)
            if examination:
                await buy_token('token2t_amount_user',count)
            else:
                await not_enough_money()
        elif current_state == 'ClientStatesGroup:token3t_anumber_of_tokens':
            examination = await balance_update(message.from_user.id, 5*count)
            if examination:
                await buy_token('token3t_amount_user',count)
            else:
                await not_enough_money()
    except:
        await bot.send_message(message.from_user.id,'Вы ввели не число')
    await state.finish()


async def number_of_proxy(message: types.Message, state: FSMContext):
    async def buy_proxy(type, count):
        type = type.split('_')
        async with aiofiles.open('data/proxy.txt', 'r') as file:
            lines = await file.readlines()
            lines_list = []
            necessary_list = []
            data = []
            for line in lines:
                if f'{type[1]}:' in line and type[2] in line:
                    necessary_list.append(line)
                else:
                    lines_list.append(line)
            if necessary_list == []:
                await bot.send_message(message.from_user.id,'Товар закончился')
                await message.delete()   
                return
            try:
                for i in range(0,count):
                    data.append(necessary_list.pop(0).split(':'))
            except:
                await bot.send_message(message.from_user.id,'Товара осталось меньше заданного')
                return
            async with aiofiles.open('data/proxy.txt', 'w') as file:
                necessary_list.append('\n')
                await file.writelines(necessary_list + lines_list)
            proxy_str = ''
            for proxy_lst in data:
                proxy_str += f'{proxy_lst[2]}:{proxy_lst[3]}:{proxy_lst[4]} \n'
            await bot.send_message(message.from_user.id,f'Ваш товар:\n{proxy_str}')
            await edit_proxy_history(message.from_user.id, data) 
            await message.delete()

    async def not_enough_money():
        await bot.send_message(message.from_user.id,'Не хватает денег на балансе')

    try:
        current_state = await state.get_state()  
        count = int(message.text) 

        if current_state == 'ClientStatesGroup:proxy_de_socks5_amount_user':
            examination = await balance_update(message.from_user.id, 18*count)
            if examination:
                await buy_proxy('proxy_de_socks5_amount_user',count)
            else:
                await not_enough_money()
        elif current_state == 'ClientStatesGroup:proxy_de_http_amount_user':
            examination = await balance_update(message.from_user.id, 18*count)
            if examination:
                await buy_proxy('proxy_de_http_amount_user',count)
            else:
                await not_enough_money()
        elif current_state == 'ClientStatesGroup:proxy_us_socks5_amount_user':
            examination = await balance_update(message.from_user.id, 25*count)
            if examination:
                await buy_proxy('proxy_us_socks5_amount_user',count)
            else:
                await not_enough_money()
        elif current_state == 'ClientStatesGroup:proxy_us_http_amount_user':
            examination = await balance_update(message.from_user.id, 25*count)
            if examination:
                await buy_proxy('proxy_us_http_amount_user',count)
            else:
                await not_enough_money()
        elif current_state == 'ClientStatesGroup:proxy_nl_socks5_amount_user':
            examination = await balance_update(message.from_user.id, 17*count)
            if examination:
                await buy_proxy('proxy_nl_socks5_amount_user',count)
            else:
                await not_enough_money()
        elif current_state == 'ClientStatesGroup:proxy_nl_http_amount_user':
            examination = await balance_update(message.from_user.id, 17*count)
            if examination:
                await buy_proxy('proxy_nl_http_amount_user',count)
            else:
                await not_enough_money()
    except:
        await bot.send_message(message.from_user.id,'Вы ввели не число')
    await state.finish()


# @dp.message_handler(state='*')
async def main(message: types.Message):
    if message.text == 'Мой профиль 👤':
        user = await get_info(message.from_user.id,message.from_user.username)
        await bot.send_message(message.from_user.id,f'❤️ Пользователь:  @{user[1]}\n💸 Количество покупок: {user[3]}\n🔑 ID: {user[0]}\n💰 Ваш баланс: {user[2]} ₽',reply_markup=profile_kb)
    elif message.text == 'Соглашение 📜':
        await bot.send_message(message.from_user.id,AGREEMENT)
    elif message.text == 'Помощь 🆘':
        await bot.send_message(message.from_user.id,'<a href="http://discord.gg/">Наш Discord сервер</a> 🤖\n<a href="http://t.me/PraktikaSupport_bot">Тех. Поддержка</a> 🛠️', 'HTML')
    elif message.text == 'О магазине 📕':
        await bot.send_message(message.from_user.id,DESCRIPTION, 'HTML')
    elif message.text == 'Товары 🍭':
        await bot.send_message(message.from_user.id,'Товары', reply_markup=product_kb)
        await message.delete()
    elif message.text == 'Выход в меню 🔙':
        await bot.send_message(message.from_user.id,'Выход в меню', reply_markup=main_kb)
        await message.delete()

    elif message.text == 'Vpn 🌐':
        await bot.send_photo(message.from_user.id, types.InputFile('img/vpn.png'), 'VPN-сервис - это онлайн-сервис, который шифрует ваш интернет-трафик и скрывает ваш IP-адрес и физическое местоположение.', reply_markup=vpn_kb)
    elif message.text == 'Discord Nitro 🤖':
        await bot.send_photo(message.from_user.id, types.InputFile('img/discord_nitro.png'), 'Discord Nitro - это платная подписка, которая разблокирует различные функции и преимущества на Discord, позволяя вам больше веселиться и выражать себя.', reply_markup=nitro_kb)
    elif message.text == 'Discord токены 🛅':
        await bot.send_photo(message.from_user.id, types.InputFile('img/tokens.png'), 'Дискорд токены - это уникальные идентификаторы, которые позволяют взаимодействовать с серверами Discord.', reply_markup=tokens_kb)
    elif message.text == 'Proxy 📶':
        await bot.send_photo(message.from_user.id, types.InputFile('img/proxy.png'), 'Прокси - это сервис, который позволяет подключаться к интернет-ресурсам через посредника, скрывая ваш реальный IP-адрес и обеспечивая анонимность и безопасность.', reply_markup=proxy_kb)


# @dp.callback_query_handler(lambda callback: 'profile' in callback.data)
async def profile_callback(callback: types.CallbackQuery):
    if callback.data == 'profile_history_of_orders':
        history = await get_history(callback.from_user.id)
        if history == 'У вас нет заказов':
            await bot.send_message(callback.from_user.id,'У вас нет покупок')
            await callback.message.delete()
            return
        purchase_str = ''
        for purchase in history.split('``'):
            if len(purchase) != 0:
                for i in purchase.split('/./'):
                    purchase_str += '\n' + i
                purchase_str += '_'*40+'\n'
        await callback.message.delete()
        await bot.send_message(callback.from_user.id,f'Ваши покупки:\n\n{purchase_str}')


# @dp.callback_query_handler(lambda callback: '_vpn_' in callback.data)
async def buy_vpn_callback(callback: types.CallbackQuery):

    async def buy_vpn(type):
        async with aiofiles.open('data/vpn.txt', 'r') as file:
            lines = await file.readlines()
            lines_list = []
            necessary_list = []
            for line in lines:
                if type in line:
                    necessary_list.append(line)
                else:
                    lines_list.append(line)
            if necessary_list == []:
                 await bot.send_message(callback.from_user.id,'Товар закончился')
                 await callback.message.delete()   
                 return
            data = necessary_list.pop(0).split(':')
            async with aiofiles.open('data/vpn.txt', 'w') as file:
                await file.writelines(necessary_list + lines_list)
            await bot.send_message(callback.from_user.id,f'Ваш аккаунт:\nEmail: {data[2]}\nPassword: {data[3]}')
            await edit_vpn_history(callback.from_user.id, callback.data, data) 
            await callback.message.delete()

    async def not_enough_money():
        await bot.send_message(callback.from_user.id,'Не хватает денег на балансе')   


    if callback.data == 'nord_vpn_one_month':    
        examination = await balance_update(callback.from_user.id, 300)
        if examination:
            await buy_vpn('nord:1m:')
        else: 
            await not_enough_money()
    elif callback.data == 'nord_vpn_three_months':    
        examination = await balance_update(callback.from_user.id, 800)
        if examination:
            await buy_vpn('nord:3m:')
        else: 
            await not_enough_money()
    elif callback.data == 'nord_vpn_six_months':    
        examination = await balance_update(callback.from_user.id, 1500)
        if examination:
            await buy_vpn('nord:6m:')
        else: 
            await not_enough_money()
    
    elif callback.data == 'express_vpn_one_month':    
        examination = await balance_update(callback.from_user.id, 300)
        if examination:
            await buy_vpn('express:1m:')
        else: 
            await not_enough_money()
    elif callback.data == 'express_vpn_three_months':    
        examination = await balance_update(callback.from_user.id, 800)
        if examination:
            await buy_vpn('express:3m:')
        else: 
            await not_enough_money()
    elif callback.data == 'express_vpn_six_months':    
        examination = await balance_update(callback.from_user.id, 1500)
        if examination:
            await buy_vpn('express:6m:')
        else: 
            await not_enough_money()

    elif callback.data == 'cyberghost_vpn_one_month':    
        examination = await balance_update(callback.from_user.id, 300)
        if examination:
            await buy_vpn('cyberghost:1m:')
        else: 
            await not_enough_money()
    elif callback.data == 'cyberghost_vpn_three_months':    
        examination = await balance_update(callback.from_user.id, 800)
        if examination:
            await buy_vpn('cyberghost:3m:')
        else: 
            await not_enough_money()
    elif callback.data == 'cyberghost_vpn_six_months':    
        examination = await balance_update(callback.from_user.id, 1500)
        if examination:
            await buy_vpn('cyberghost:6m:')
        else: 
            await not_enough_money()

    elif callback.data == 'exit_to_vpn_menu':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/vpn.png'), type='photo', caption='VPN-сервис - это онлайн-сервис, который шифрует ваш интернет-трафик и скрывает ваш IP-адрес и физическое местоположение.'), reply_markup=vpn_kb)


# @dp.callback_query_handler(lambda callback: 'vpn' in callback.data)
async def vpn_callback(callback: types.CallbackQuery):
    if callback.data == 'nord_vpn':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/nord_vpn.png'), type='photo', caption='Nord VPN — уникальные функции защиты, в том числе собственная разработка сервиса, протокол Nordlynx, который обеспечивает первоклассную скорость передачи данных.'), reply_markup=nord_kb)
        # await callback.message.delete()
        # await callback.message.answer_photo(photo =  types.InputFile('img/nord_vpn.png'), caption='Nord VPN — уникальные функции защиты, в том числе собственная разработка сервиса, протокол Nordlynx, который обеспечивает первоклассную скорость передачи данных.', reply_markup=nord_kb)
    elif callback.data == 'express_vpn':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/express_vpn.png'), type='photo', caption='Express VPN — лучший VPN-сервис в плане скорости, защиты и надежности.'), reply_markup=express_kb)
    elif callback.data == 'cyberghost_vpn':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/cyberghost_vpn.png'), type='photo', caption='Сyber Ghost VPN — специализированные серверы и отличная защита приватности.'), reply_markup=cyberghost_kb)


# @dp.callback_query_handler(lambda callback: 'nitro' in callback.data)
async def buy_nitro_callback(callback: types.CallbackQuery):
    async def buy_nitro(type):
        async with aiofiles.open('data/nitro.txt', 'r') as file:
            lines = await file.readlines()
            lines_list = []
            necessary_list = []
            for line in lines:
                if type in line:
                    necessary_list.append(line)
                else:
                    lines_list.append(line)
            if necessary_list == []:
                await bot.send_message(callback.from_user.id,'Товар закончился')
                await callback.message.delete()   
                return
            data = necessary_list.pop(0).split('|')
            async with aiofiles.open('data/nitro.txt', 'w') as file:
                necessary_list.append('\n')
                await file.writelines(necessary_list + lines_list)
            await bot.send_message(callback.from_user.id,f'Ваш товар:\n{data[1]}')
            await edit_nitro_history(callback.from_user.id, callback.data, data) 
            await callback.message.delete()

    async def not_enough_money():
        await bot.send_message(callback.from_user.id,'Не хватает денег на балансе')   
        
    if callback.data == 'nitro_full_monthly':
        examination = await balance_update(callback.from_user.id, 250)
        if examination:
            await buy_nitro('nfm')
        else: 
            await not_enough_money()
    elif callback.data == 'nitro_classic_monthly':
        examination = await balance_update(callback.from_user.id, 190)
        if examination:
            await buy_nitro('ncm')
        else: 
            await not_enough_money()
    elif callback.data == 'nitro_full_yearly':
        examination = await balance_update(callback.from_user.id, 1250)
        if examination:
            await buy_nitro('nfy')
        else: 
            await not_enough_money()
    elif callback.data == 'nitro_classic_yearly':
        examination = await balance_update(callback.from_user.id, 700)
        if examination:
            await buy_nitro('ncy')
        else: 
            await not_enough_money()


# @dp.callback_query_handler(lambda callback: 't_a' in callback.data)
async def buy_token_callback(callback: types.CallbackQuery):
    async def buy_token(type, count):
        async with aiofiles.open('data/tokens.txt', 'r') as file:
            lines = await file.readlines()
            lines_list = []
            necessary_list = []
            data = []
            for line in lines:
                if type[0] in line:
                    necessary_list.append(line)
                else:
                    lines_list.append(line)
            if necessary_list == []:
                await bot.send_message(callback.from_user.id,'Товар закончился')
                await callback.message.delete()   
                return
            try:
                for i in range(0,count):
                    data.append(necessary_list.pop(0).split(':'))
            except:
                await bot.send_message(callback.from_user.id,'Товара осталось меньше заданного')
                return
            async with aiofiles.open('data/tokens.txt', 'w') as file:
                necessary_list.append('\n')
                await file.writelines(necessary_list + lines_list)
            token_str = ''
            for token_lst in data:
                token_str += token_lst[1] + '\n'
            await bot.send_message(callback.from_user.id,f'Ваш товар:\n{token_str}')
            await edit_tokens_history(callback.from_user.id, callback.data, data) 
            await callback.message.delete()

    async def not_enough_money():
        await bot.send_message(callback.from_user.id,'Не хватает денег на балансе')
    
    if callback.data == 'token1t_amount1':
        examination = await balance_update(callback.from_user.id, 2)
        if examination:
            await buy_token(callback.data.split('t_a'),1)
        else: 
            await not_enough_money()
    elif callback.data == 'token1t_amount5':
        examination = await balance_update(callback.from_user.id, 2*5)
        if examination:
            await buy_token(callback.data.split('t_a'),5)
        else: 
            await not_enough_money()
    elif callback.data == 'token1t_amount10':
        examination = await balance_update(callback.from_user.id, 2*10)
        if examination:
            await buy_token(callback.data.split('t_a'),10)
        else: 
            await not_enough_money()
    elif callback.data == 'token2t_amount1':
        examination = await balance_update(callback.from_user.id, 2)
        if examination:
            await buy_token(callback.data.split('t_a'),1)
        else: 
            await not_enough_money()
    elif callback.data == 'token2t_amount5':
        examination = await balance_update(callback.from_user.id, 2*5)
        if examination:
            await buy_token(callback.data.split('t_a'),5)
        else: 
            await not_enough_money()
    elif callback.data == 'token2t_amount10':
        examination = await balance_update(callback.from_user.id, 2*10)
        if examination:
            await buy_token(callback.data.split('t_a'),10)
        else: 
            await not_enough_money()
    elif callback.data == 'token3t_amount1':
        examination = await balance_update(callback.from_user.id, 2)
        if examination:
            await buy_token(callback.data.split('t_a'),1)
        else: 
            await not_enough_money()
    elif callback.data == 'token3t_amount5':
        examination = await balance_update(callback.from_user.id, 2*5)
        if examination:
            await buy_token(callback.data.split('t_a'),5)
        else: 
            await not_enough_money()
    elif callback.data == 'token3t_amount10':
        examination = await balance_update(callback.from_user.id, 2*10)
        if examination:
            await buy_token(callback.data.split('t_a'),10)
        else: 
            await not_enough_money()

    elif callback.data == 'token1t_amount_user':
        await bot.send_message(callback.from_user.id, 'Отправьте количество')
        await ClientStatesGroup.token1t_anumber_of_tokens.set()
    elif callback.data == 'token2t_amount_user':
        await bot.send_message(callback.from_user.id, 'Отправьте количество')
        await ClientStatesGroup.token2t_anumber_of_tokens.set()
    elif callback.data == 'token3t_amount_user':
        await bot.send_message(callback.from_user.id, 'Отправьте количество')
        await ClientStatesGroup.token3t_anumber_of_tokens.set()

# @dp.callback_query_handler(lambda callback: 'token' in callback.data)
async def token_callback(callback: types.CallbackQuery):
    if callback.data == 'token1':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/token1.png'), type='photo', caption='Токенные собранные с логов, самые дешевые.\nВыберите количество для покупки:'), reply_markup=token1_kb) 
    elif callback.data == 'token2':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/token2.png'), type='photo', caption='Токены (подтвержденные по эмейл) в отлежке не умирают, возраст ОТ 8МЕС. + КАЧЕСТВО ПРЕМИУМ.\nВыберите количество для покупки:'), reply_markup=token2_kb)
    elif callback.data == 'token3':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/token3.png'), type='photo', caption='Токены 200+ дней отлеги. Не умирают, MIX IP, Ultra High Quality & Best PRICE.\nВыберите количество для покупки:'), reply_markup=token3_kb)    
    elif callback.data == 'exit_to_tokens_menu':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/tokens.png'), type='photo', caption='Дискорд токены - это уникальные идентификаторы, которые позволяют взаимодействовать с серверами Discord.'), reply_markup=tokens_kb)


# @dp.callback_query_handler(lambda callback: 'proxy' in callback.data)
async def proxy_callback(callback: types.CallbackQuery):
    async def buy_proxy(type, count):
        async with aiofiles.open('data/proxy.txt', 'r') as file:
            lines = await file.readlines()
            lines_list = []
            necessary_list = []
            data = []
            for line in lines:
                if f'{type[1]}:' in line and type[2] in line:
                    necessary_list.append(line)
                else:
                    lines_list.append(line)
            if necessary_list == []:
                await bot.send_message(callback.from_user.id,'Товар закончился')
                await callback.message.delete()   
                return
            try:
                for i in range(0,count):
                    data.append(necessary_list.pop(0).split(':'))
            except:
                await bot.send_message(callback.from_user.id,'Товара осталось меньше заданного')
                return
            async with aiofiles.open('data/proxy.txt', 'w') as file:
                necessary_list.append('\n')
                await file.writelines(necessary_list + lines_list)
            proxy_str = ''
            for proxy_lst in data:
                proxy_str += f'{proxy_lst[2]}:{proxy_lst[3]}:{proxy_lst[4]} \n'
            await bot.send_message(callback.from_user.id,f'Ваш товар:\n{proxy_str}')
            await edit_proxy_history(callback.from_user.id, data) 
            await callback.message.delete()

    async def not_enough_money():
        await bot.send_message(callback.from_user.id,'Не хватает денег на балансе')
  
    if callback.data == 'proxy_de':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_de.png'), type='photo', caption='Выберите тип прокси.'), reply_markup=proxy_de_kb)
    elif callback.data == 'proxy_de_socks5':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_de.png'), type='photo', caption='Прокси Германия SOKC5.'), reply_markup=proxy_de_socks5_kb)
    elif callback.data == 'proxy_de_http':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_de.png'), type='photo', caption='Прокси Германия http.'), reply_markup=proxy_de_http_kb)
    elif callback.data == 'exit_to_proxy_de_menu':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_de.png'), type='photo', caption='Выберите тип прокси.'), reply_markup=proxy_de_kb)
    elif callback.data == 'proxy_us':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_us.png'), type='photo', caption='Прокси США.'), reply_markup=proxy_us_kb)
    elif callback.data == 'proxy_us_socks5':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_us.png'), type='photo', caption='Прокси США SOKC5.'), reply_markup=proxy_us_socks5_kb)
    elif callback.data == 'proxy_us_http':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_us.png'), type='photo', caption='Прокси США http.'), reply_markup=proxy_us_http_kb)
    elif callback.data == 'exit_to_proxy_us_menu':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_us.png'), type='photo', caption='Выберите тип прокси.'), reply_markup=proxy_us_kb)
    elif callback.data == 'proxy_nl':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_nl.png'), type='photo', caption='Выберите тип прокси.'), reply_markup=proxy_nl_kb)
    elif callback.data == 'proxy_nl_socks5':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_nl.png'), type='photo', caption='Прокси Нидерланды SOKC5.'), reply_markup=proxy_nl_socks5_kb)
    elif callback.data == 'proxy_nl_http':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_nl.png'), type='photo', caption='Прокси Нидерланды http.'), reply_markup=proxy_nl_http_kb)
    elif callback.data == 'exit_to_proxy_nl_menu':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy_nl.png'), type='photo', caption='Выберите тип прокси.'), reply_markup=proxy_nl_kb)
    
    elif callback.data == 'proxy_de_socks5_amount1':
        examination = await balance_update(callback.from_user.id, 18)
        if examination:
            await buy_proxy(callback.data.split('_'),1)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_de_socks5_amount5':
        examination = await balance_update(callback.from_user.id, 5*18)
        if examination:
            await buy_proxy(callback.data.split('_'),5)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_de_socks5_amount10':
        examination = await balance_update(callback.from_user.id, 10*18)
        if examination:
            await buy_proxy(callback.data.split('_'),10)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_de_http_amount1':
        examination = await balance_update(callback.from_user.id, 18)
        if examination:
            await buy_proxy(callback.data.split('_'),1)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_de_http_amount5':
        examination = await balance_update(callback.from_user.id, 5*18)
        if examination:
            await buy_proxy(callback.data.split('_'),5)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_de_http_amount10':
        examination = await balance_update(callback.from_user.id, 10*18)
        if examination:
            await buy_proxy(callback.data.split('_'),10)
        else: 
            await not_enough_money()

    elif callback.data == 'proxy_us_socks5_amount1':
        examination = await balance_update(callback.from_user.id, 25)
        if examination:
            await buy_proxy(callback.data.split('_'),1)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_us_socks5_amount5':
        examination = await balance_update(callback.from_user.id, 5*25)
        if examination:
            await buy_proxy(callback.data.split('_'),5)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_us_socks5_amount10':
        examination = await balance_update(callback.from_user.id, 10*25)
        if examination:
            await buy_proxy(callback.data.split('_'),10)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_us_http_amount1':
        examination = await balance_update(callback.from_user.id, 25)
        if examination:
            await buy_proxy(callback.data.split('_'),1)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_us_http_amount5':
        examination = await balance_update(callback.from_user.id, 5*25)
        if examination:
            await buy_proxy(callback.data.split('_'),5)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_us_http_amount10':
        examination = await balance_update(callback.from_user.id, 10*25)
        if examination:
            await buy_proxy(callback.data.split('_'),10)
        else: 
            await not_enough_money()

    elif callback.data == 'proxy_nl_socks5_amount1':
        examination = await balance_update(callback.from_user.id, 17)
        if examination:
            await buy_proxy(callback.data.split('_'),1)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_nl_socks5_amount5':
        examination = await balance_update(callback.from_user.id, 5*17)
        if examination:
            await buy_proxy(callback.data.split('_'),5)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_nl_socks5_amount10':
        examination = await balance_update(callback.from_user.id, 10*17)
        if examination:
            await buy_proxy(callback.data.split('_'),10)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_nl_http_amount1':
        examination = await balance_update(callback.from_user.id, 17)
        if examination:
            await buy_proxy(callback.data.split('_'),1)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_nl_http_amount5':
        examination = await balance_update(callback.from_user.id, 5*17)
        if examination:
            await buy_proxy(callback.data.split('_'),5)
        else: 
            await not_enough_money()
    elif callback.data == 'proxy_nl_http_amount10':
        examination = await balance_update(callback.from_user.id, 10*17)
        if examination:
            await buy_proxy(callback.data.split('_'),10)
        else: 
            await not_enough_money()

    elif callback.data == 'proxy_de_socks5_amount_user':
        await bot.send_message(callback.from_user.id, 'Отправьте количество')
        await ClientStatesGroup.proxy_de_socks5_amount_user.set()
    elif callback.data == 'proxy_de_http_amount_user':
        await bot.send_message(callback.from_user.id, 'Отправьте количество')
        await ClientStatesGroup.proxy_de_http_amount_user.set()
    elif callback.data == 'proxy_us_socks5_amount_user':
        await bot.send_message(callback.from_user.id, 'Отправьте количество1')
        await ClientStatesGroup.proxy_us_socks5_amount_user.set()
    elif callback.data == 'proxy_us_http_amount_user':
        await bot.send_message(callback.from_user.id, 'Отправьте количество')
        await ClientStatesGroup.proxy_us_http_amount_user.set()
    elif callback.data == 'proxy_nl_socks5_amount_user':
        await bot.send_message(callback.from_user.id, 'Отправьте количество')
        await ClientStatesGroup.proxy_nl_socks5_amount_user.set()
    elif callback.data == 'proxy_nl_http_amount_user':
        await bot.send_message(callback.from_user.id, 'Отправьте количество')
        await ClientStatesGroup.proxy_nl_http_amount_user.set()

    elif callback.data == 'exit_to_proxy_menu':
        await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/proxy.png'), type='photo', caption='Прокси - это сервис, который позволяет подключаться к интернет-ресурсам через посредника, скрывая ваш реальный IP-адрес и обеспечивая анонимность и безопасность.'), reply_markup=proxy_kb)
    # elif callback.data == 'exit_to_nitro_menu':
    #     await callback.message.edit_media(types.InputMedia(media=types.InputFile('img/discord_nitro.png'), type='photo', caption='Discord Nitro - это платная подписка, которая разблокирует различные функции и преимущества на Discord, позволяя вам больше веселиться и выражать себя.'), reply_markup=nitro_kb)
    #     await callback.answer()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(number_of_tokens ,state=ClientStatesGroup.token1t_anumber_of_tokens)
    dp.register_message_handler(number_of_tokens, state=ClientStatesGroup.token2t_anumber_of_tokens)
    dp.register_message_handler(number_of_tokens, state=ClientStatesGroup.token3t_anumber_of_tokens)
    dp.register_message_handler(number_of_proxy ,state=ClientStatesGroup.proxy_de_socks5_amount_user)
    dp.register_message_handler(number_of_proxy ,state=ClientStatesGroup.proxy_de_http_amount_user)
    dp.register_message_handler(number_of_proxy ,state=ClientStatesGroup.proxy_us_socks5_amount_user)
    dp.register_message_handler(number_of_proxy ,state=ClientStatesGroup.proxy_us_http_amount_user)
    dp.register_message_handler(number_of_proxy ,state=ClientStatesGroup.proxy_nl_socks5_amount_user)
    dp.register_message_handler(number_of_proxy ,state=ClientStatesGroup.proxy_nl_http_amount_user)
    dp.register_message_handler(main, state='*')
    dp.register_callback_query_handler(profile_callback, lambda callback: 'profile' in callback.data)
    dp.register_callback_query_handler(buy_vpn_callback, lambda callback: '_vpn_' in callback.data)
    dp.register_callback_query_handler(vpn_callback, lambda callback: 'vpn' in callback.data)
    dp.register_callback_query_handler(buy_nitro_callback, lambda callback: 'nitro' in callback.data)
    dp.register_callback_query_handler(buy_token_callback, lambda callback: 't_a' in callback.data)
    dp.register_callback_query_handler(token_callback, lambda callback: 'token' in callback.data)
    dp.register_callback_query_handler(proxy_callback, lambda callback: 'proxy' in callback.data)
    # dp.register_message_handler()
    # dp.register_callback_query_handler()