from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN_API')
storage = MemoryStorage()
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
