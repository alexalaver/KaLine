from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import buttons
import other_functions as fnc
from datab import Data
import buttons as btn
import logging
import config as cfg
import aiohttp
import re

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Data("192.168.1.22", "5432", "kaline", "kaline_user", "kaline1230")


class SELECTLANGUAGE(StatesGroup):
    select_language_1 = State()

class ACTIVATEORDERS(StatesGroup):
    activate_orders_1 = State()

class CHECKBALANCEORDERS(StatesGroup):
    check_balance_orders_1 = State()

class SUPPORTSENDMESSAGE(StatesGroup):
    support_send_message_1 = State()

#################################### START COMMAND
async def start_command(message):
    if message.chat.type == types.ChatType.PRIVATE:
        user_id = message.from_user.id
        if(not db.check_user(user_id)):
            await SELECTLANGUAGE.select_language_1.set()
            markup = btn.select_language_buttons()
            await message.answer(cfg.SELECT_LANGUAGE_TEXT, reply_markup=markup)
        else:
            lang = db.select_language(user_id)
            markup = buttons.begins_button(lang)
            await message.answer(cfg.START_BEGIN_TEXT(lang), reply_markup=markup)

#################################### START COMMAND

#################################### BUY eSIM COMMAND

async def buy_eSIM_command(message):
    if message.chat.type == types.ChatType.PRIVATE:
        user_id = message.from_user.id
        lang = db.select_language(user_id)
        await message.answer(cfg.BUY_eSIM_TEXT(lang))

#################################### BUY eSIM COMMAND

#################################### SEND PHOTO PROOF

async def send_photo_proof_func(message):
    if message.chat.type == types.ChatType.PRIVATE:
        proof_channel = cfg.PROOF_CHANNEL_TG
        user_id = message.from_user.id
        photo_file_id = message.photo[0].file_id
        markup = buttons.confirm_order_buttons(user_id)
        await bot.send_photo(proof_channel, caption=cfg.USER_SEND_PHOTO_TEXT(fnc.nick_with_link("Օգտագործողն", user_id)), photo=photo_file_id, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)
        # await bot.send_message(proof_channel, cfg.USER_SEND_PHOTO_TEXT, reply_markup=markup)

#################################### SEND PHOTO PROOF

#################################### ACTIVATE FOR ORDERS ID FUNC

async def activate_for_orders_id_func(message):
    if message.chat.type == types.ChatType.PRIVATE:
        user_id = message.from_user.id
        lang = db.select_language(user_id)
        markup = buttons.back_button(lang)
        await message.answer(cfg.ACTIVATE_TEXT_USER(lang), reply_markup=markup)
        await ACTIVATEORDERS.activate_orders_1.set()

async def activate_esim(orders_id):
    url = "https://herobot.me/api/globalink/redeem"
    headers = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjQ4Mjc2NjE2NDYsImlhdCI6MTcwNTU5NzY0NiwiZGlzY29yZFVzZXIiOiJrYXJvNzcyMiIsImRpc2NvcmRJRCI6Nzk0NTQ1NTk0MzcwMDk3MjAyfQ.mmvayO87Ft7I7RCcx_KEWIrjcAEWhvhuwiuDq-dR6Qk",
        "Host": "herobot.me",
        "Content-Type": "application/json"
    }
    json_data = {
        "orderID": orders_id
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

async def fetch_qr_code(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.read()
            return None

#################################### ACTIVATE FOR ORDERS ID FUNC

#################################### CHECK BANALCE ORDERS ID FUNC

async def check_balance_for_orders_id_func(message):
    if message.chat.type == types.ChatType.PRIVATE:
        user_id = message.from_user.id
        lang = db.select_language(user_id)
        markup = buttons.back_button(lang)
        await message.answer(cfg.CHECK_BALANCE_TEXT_USER(lang), reply_markup=markup)
        await CHECKBALANCEORDERS.check_balance_orders_1.set()

async def check_esim_usage(orders_id):
    url = "https://herobot.me/api/globalink/usage"
    headers = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjQ4Mjc2NjE2NDYsImlhdCI6MTcwNTU5NzY0NiwiZGlzY29yZFVzZXIiOiJrYXJvNzcyMiIsImRpc2NvcmRJRCI6Nzk0NTQ1NTk0MzcwMDk3MjAyfQ.mmvayO87Ft7I7RCcx_KEWIrjcAEWhvhuwiuDq-dR6Qk",
        "Host": "herobot.me",
        "Content-Type": "application/json"
    }
    json_data = {
        "orderID": orders_id
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

#################################### CHECK BANALCE ORDERS ID FUNC

#################################### BUTTONS LOGIC ACCEPT AND CANCEL

async def buttons_accept_and_cancel_func(callback_query: types.CallbackQuery):
    buttons_select = callback_query.data.split(":")
    user_order_id = int(buttons_select[1])
    accept_or_cancel = buttons_select[0]
    message_id = callback_query.message.message_id
    lang = db.select_language(user_order_id)
    if accept_or_cancel == "cancel":
        await bot.edit_message_caption(chat_id=cfg.PROOF_CHANNEL_TG, message_id=message_id, caption=cfg.CANCEL_USER_ORDER(fnc.nick_with_link("օգտագործողի", user_order_id)), reply_markup=None, parse_mode=types.ParseMode.MARKDOWN)
        await bot.send_message(chat_id=user_order_id, text=cfg.CANCEL_USER_ORDER_TEXt(lang))
    elif accept_or_cancel == "confirm":
        orders_all_new = db.select_orders_all_new()
        orders_id_for_user = orders_all_new[0]
        orders_all_used = db.select_orders_all_used()
        orders_user = db.select_orders_user(user_order_id)
        orders_user.append(orders_id_for_user)
        orders_all_used.append(orders_id_for_user)
        orders_all_new.remove(orders_id_for_user)
        db.update_orders_all_new(orders_all_new)
        db.update_orders_all_used(orders_all_used)
        db.update_orders_user(user_order_id, orders_user)
        await bot.edit_message_caption(chat_id=cfg.PROOF_CHANNEL_TG, message_id=message_id, caption=cfg.CONFIRM_USER_ORDER(fnc.nick_with_link("օգտվողին", user_order_id)), reply_markup=None, parse_mode=types.ParseMode.MARKDOWN)
        await bot.send_message(chat_id=user_order_id, text=cfg.CONFIRM_ORDERS_USER_TEXT(lang))
        await bot.send_message(chat_id=user_order_id, text=orders_id_for_user)

#################################### BUTTONS LOGIC ACCEPT AND CANCEL

#################################### SEND COUNTRIES FUNC

async def send_countries_func(message):
    user_id = message.from_user.id
    lang = db.select_language(user_id)
    media = [
        types.InputMediaPhoto(open('img/country1.jpg', 'rb'), caption=cfg.SEND_PHOTO_TEXT(lang)),
        types.InputMediaPhoto(open('img/country2.jpg', 'rb')),
        types.InputMediaPhoto(open('img/country3.jpg', 'rb')),
        types.InputMediaPhoto(open('img/country4.jpg', 'rb')),
        types.InputMediaPhoto(open('img/country5.jpg', 'rb')),
        types.InputMediaPhoto(open('img/country6.jpg', 'rb')),
        types.InputMediaPhoto(open('img/country7.jpg', 'rb'))
    ]
    await bot.send_media_group(message.from_user.id, media)

#################################### SEND COUNTRIES FUNC

#################################### SUPPORT SEND MESSAGE FUNC

async def support_send_message_func(message):
    user_id = message.from_user.id
    lang = db.select_language(user_id)
    markup = buttons.back_button(lang)
    await message.answer(cfg.SEND_TEXT_FOR_SUPPORT(lang), reply_markup=markup)
    await SUPPORTSENDMESSAGE.support_send_message_1.set()

#################################### SUPPORT SEND MESSAGE FUNC

#################################### SELECT LANGUAGE BUTTONS
@dp.callback_query_handler(state=SELECTLANGUAGE.select_language_1)
async def select_language_1_func(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    first_name = callback_query.from_user.first_name
    username = callback_query.from_user.username
    id = db.check_numbers_id() + 1
    lang = None
    if callback_query.data == "arm_lang":
        lang = "arm"
    elif callback_query.data == "rus_lang":
        #lang = "rus"
        pass
    elif callback_query.data == "eng_lang":
        #lang = "eng
        pass
    if lang is not None:
        db.add_user(id, user_id, first_name, username, lang)
        await callback_query.message.delete()
        markup = buttons.begins_button(lang)
        await callback_query.message.answer(text=cfg.RIGHT_SELECT_ARM_LANG(lang), reply_markup=markup)
        await state.finish()

@dp.message_handler(state=SELECTLANGUAGE.select_language_1)
async def select_language_1_text(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        if message.text == "/reg":
            markup = btn.select_language_buttons()
            await message.answer(cfg.SELECT_LANGUAGE_TEXT, reply_markup=markup)
        else:
            await message.answer(cfg.WRITE_TEXT_SELECT_LANGUAGE)
#################################### SELECT LANGUAGE BUTTONS

#################################### ALL COMMANDS AND TEXTS
@dp.message_handler(content_types=['text', 'photo'])
async def all_functions(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        user_id = message.from_user.id
        if (not db.check_user(user_id)):
            await SELECTLANGUAGE.select_language_1.set()
            markup = btn.select_language_buttons()
            await message.answer(cfg.SELECT_LANGUAGE_TEXT, reply_markup=markup)
        else:
            lang = db.select_language(user_id)
            if message.text == "/start":
                await start_command(message)
            elif message.text == cfg.BUY_eSIM_BUTTON(lang):
                await buy_eSIM_command(message)
            elif message.text == cfg.ACTIVATE_BUTTON(lang):
                await activate_for_orders_id_func(message)
            elif message.text == cfg.CHECK_BALANCE_BUTTON(lang):
                await check_balance_for_orders_id_func(message)
            elif message.text == cfg.LIST_COUNTRIES_BUTTON(lang):
                await send_countries_func(message)
            elif message.text == cfg.CONTACT_US_BUTTON(lang):
                await support_send_message_func(message)
            else:
                await message.answer(cfg.ERROR_COMMAND_TEXT(lang))
            if message.photo:
                await send_photo_proof_func(message)
    elif message.chat.username == cfg.SUPPORT_GROUP[1:]:
        match = re.search(r'\((.*?)\)', message.reply_to_message.text)
        if match:
            user_first_id = match.group(1)
        else:
            user_first_id = None
        lang = db.select_language(user_first_id)
        await bot.send_message(user_first_id, cfg.SUPPORT_RIGHT_TEXT(lang, message.text))

#################################### ALL COMMANDS AND TEXTS

#################################### ALL BUTTONS

@dp.callback_query_handler()
async def all_buttons(callback_query: types.CallbackQuery):
    accept_or_cancel = callback_query.data.split(":")
    if len(accept_or_cancel) == 2:
        await buttons_accept_and_cancel_func(callback_query)

#################################### ALL BUTTONS

#################################### ACTIVATE FOR ORDERS ID PROCESS

@dp.message_handler(state=ACTIVATEORDERS.activate_orders_1)
async def activate_for_orders_id_state(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    lang = db.select_language(user_id)
    markup = buttons.begins_button(lang)
    if message.text == cfg.BACK_BUTTON(lang):
        await message.answer(text=cfg.BACK_TEXT(lang), reply_markup=markup)
        await state.finish()
    else:
        orders_id = message.text
        esim_data = await activate_esim(orders_id)
        if esim_data and esim_data.get("success"):
            qr_code = esim_data["eSIM"]["qrCode"]
            activation_code = esim_data["eSIM"]["activationCode"]
            smdp_address = esim_data["eSIM"]["smdpAddress"]
            qr_code_image = await fetch_qr_code(qr_code)
            if qr_code_image:
                await message.answer(cfg.ACTIVATION_RIGHT_TEXT(lang, activation_code, smdp_address), reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)
                await message.answer_photo(qr_code_image)
                await state.finish()
            else:
                await message.answer(f"QR Code: {qr_code}\nActivation Code: {activation_code}\nSM-DP+ Address: {smdp_address}")
                await state.finish()
        else:
            await message.answer(cfg.ERROR_ACTIVATE_CODE_USER_TEXT(lang))

#################################### ACTIVATE FOR ORDERS ID PROCESS

#################################### CHECK BANALCE ORDERS ID PROCESS

@dp.message_handler(state=CHECKBALANCEORDERS.check_balance_orders_1)
async def check_balance_orders_1_state(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    lang = db.select_language(user_id)
    markup = buttons.begins_button(lang)
    if message.text == cfg.BACK_BUTTON(lang):
        await message.answer(text=cfg.BACK_TEXT(lang), reply_markup=markup)
        await state.finish()
    else:
        orders_id = message.text
        usage_data = await check_esim_usage(orders_id)
        if usage_data and usage_data.get("success"):
            remaining_data = usage_data["plan"]["remainingData"]
            expiry_date = usage_data["plan"]["expiryDate"]
            response_text = cfg.CHECK_BALANCE_RIGHT_TEXT(lang, remaining_data, expiry_date)
            await message.answer(response_text, reply_markup=markup)
            await state.finish()
        else:
            await message.answer(cfg.CHECK_BALANCE_TEXT_ERROR(lang))

#################################### CHECK BANALCE ORDERS ID PROCESS

#################################### SEND SUPPORT TEXT PROCESS

@dp.message_handler(state=SUPPORTSENDMESSAGE.support_send_message_1)
async def support_send_message_1_func(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    lang = db.select_language(user_id)
    markup = buttons.begins_button(lang)
    if message.text == cfg.BACK_BUTTON(lang):
        await message.answer(text=cfg.BACK_TEXT(lang), reply_markup=markup)
        await state.finish()
    else:
        await bot.send_message(cfg.SUPPORT_GROUP, f"{cfg.USER_SEND_TASK_TEXT(fnc.nick_with_link('Օգտատերը', user_id), user_id)}\n\n{message.text}", parse_mode=types.ParseMode.MARKDOWN)
        await message.answer(cfg.TAKE_TEXT_SUPPORT(lang), reply_markup=markup)
        await state.finish()

#################################### SEND SUPPORT TEXT PROCESS


if __name__ == "__main__":
    executor.start_polling(dp)