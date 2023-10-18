from aiogram import types, Dispatcher
from create_bot import dp, bot


async def command_help(message : types.Message):
    await bot.send_message(message.from_user.id, 'nope')


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(command_help)