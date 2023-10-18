from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client

#Стара версія
async def command_start(message : types.Message):
  await bot.send_message(message.from_user.id, 'Доброго дня!', reply_markup=kb_client)
  await message.delete()

#Нова версія
async def command_price(message : types.Message):
    await message.answer( 'Наш прайс')
    await message.delete()

async def command_buy(message : types.Message):
    await bot.send_message(message.from_user.id, 'Оберіть товари')



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start,  commands=['start'])
    dp.register_message_handler(command_price, commands=['Подивитися_прайс'])
    dp.register_message_handler(command_buy, commands=['Оформити_замовлення'])
    