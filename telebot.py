from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from GetInfoBot import GetInfo

TOKEN = 'API_KEY'
bot = Bot(TOKEN)
disp = Dispatcher(bot)

#kb = ReplyKeyboardMarkup(resize_keyboard=True)
#kb.add(KeyboardButton('Get user games'))

@disp.message_handler(content_types=['text'])
async def show_info_about_user(message: types.Message):
    await message.answer(text=GetInfo().user_games(message.text)) #, reply_markup=kb)

@disp.message_handler(commands=['start'])
async def show_answer_to_message(message: types.Message):
    await message.answer(text='Type steamid of any user') #, reply_markup=kb)

executor.start_polling(disp)
