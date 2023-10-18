from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#Функція для відсіювання НЕ модераторів
async def lovec_moder(message: types.Message):
    global ID
    ID =message.from_user.id
    await message.answer('а самому слабо???')#Доробити адмінські кнопки
    await message.delete()

#Початок діалогу нового пункту
#@dp.message_handler(commands='Завантажити', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
       await FSMAdmin.photo.set()
       await message.reply('Відправте фото')

#Вихід зі стану
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
      current_state = await state.get_state()
      if current_state is None:
          return
      await state.finish()
      await message.reply('OK')

# Ловимо першу відповідь та записуємо у словник
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
      async with state.proxy() as data:
          data['photo'] = message.photo[0].file_id
      await FSMAdmin.next()
      await message.reply('Введіть назву')

#Ловимо  наступну відповідь
#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
      async with state.proxy() as data:
          data['name'] = message.text
      await FSMAdmin.next()
      await message.reply('Введіть опис')

      async with state.proxy() as data:
          await message.reply(str(data))
      await state.finish()



def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start,  commands=['Завантажити'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='відміна', ignore_case=True), state='*')
    dp.register_message_handler(lovec_moder, commands=['Модератор'], is_chat_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(cancel_handler, state='*', commands='відміна')
    