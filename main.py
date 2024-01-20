from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import buttons
from datab import Data
import buttons as btn
import logging
import config as cfg

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Data("localhost", "5432", "kaline", "alexman", "alexman123")

class SELECTLANGUAGE(StatesGroup):
    select_language_1 = State()

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
            await message.answer(cfg.START_BEGIN_TEXT, reply_markup=markup)

#################################### START COMMAND

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
@dp.message_handler()
async def all_functions(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        if message.text == "/start":
            await start_command(message)
#################################### ALL COMMANDS AND TEXTS

if __name__ == "__main__":
    executor.start_polling(dp)