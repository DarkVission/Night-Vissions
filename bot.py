from aiogram import Bot, Dispatcher, executor, types
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import logging

bot = Bot(token='5511462464:AAF3LK7y8vTO_lIcuyiQKDpCgxWSZxGMmGw')
dp = Dispatcher(bot)

# welcome_Message
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply_photo("https://telegra.ph/file/68d324ddb2dfaad231b57.jpg",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Help", callback_data="help_menu"),
    InlineKeyboardButton(text="Night Vission", url="https://t.me/NightVission"),    InlineKeyboardButton(text="Creator", url="https://t.me/NA_VA_N_JA_NA1")]])),
    
# welcome_Message
@dp.message_handler(commands=['help'])
async def welcome(message: types.Message):
    await message.reply_sticker("CAACAgUAAxkBAAEFCTZiqEE-iFdO5DYBmDXMNAueQNndfwACXwUAArQLQVViIVZXSkmIDyQE", reply_markup=keyboard1)
    await message.answer(
        f"🌷 Hello Dear, {message.chat.full_name}😊\n\n✨ Im Night Vission Test Bot 😎")

# Button_Keybord
button1 = KeyboardButton("🤟Night Vission Devs")
button2 = KeyboardButton("⚡️Owner ")
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '🤟Night Vission Devs':
        await message.answer("@NightVission")

    elif message.text == '⚡️Owner ':
        await message.answer_photo('https://telegra.ph/file/68d324ddb2dfaad231b57.jpg')
        await message.answer("""️He He😁""")

executor.start_polling(dp)