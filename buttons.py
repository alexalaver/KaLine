from aiogram import types
import config as cfg

def begins_button(lang):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(cfg.BUY_eSIM_BUTTON(lang), cfg.CHECK_BALANCE_BUTTON(lang), cfg.HOW_TO_ACTIVATION_BUTTON(lang), cfg.LIST_COUNTRIES_BUTTON(lang), cfg.CONTACT_US_BUTTON(lang))
    return markup

def select_language_buttons():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="Հայերեն", callback_data="arm_lang")
    btn2 = types.InlineKeyboardButton(text="Русский", callback_data="rus_lang")
    btn3 = types.InlineKeyboardButton(text="English", callback_data="eng_lang")
    markup.add(btn1, btn2, btn3)
    return markup