import os
from aiogram import Bot, Dispatcher

async def main() -> None:
    dp = Dispatcher()
    bot = Bot(os.getenv('token'))
