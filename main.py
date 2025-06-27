import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

TOKEN = "7940375943:AAEzNdhDYrHejyNN-mviRO0xw3koIsk_jnI"

# Links y datos
GRUPO_EROTICO = "https://t.me/+jXXhemKMzyo3NWQ5"
GRUPO_EXPLICITO = "https://t.me/+qyZP3sQ6iY04Mzdh"
GRUPO_COMUNIDAD = "https://t.me/fatics_13"
WHATSAPP_NUMERO = "+584125294977"

# Métodos de pago
PAGOS = {
    "PayPal": "@fati0202",
    "Binance": "281257425",
    "Zelle": "Solicítalo por privado: @Cuevas0202",
    "Pago Móvil": "04125294977 (CI: 31075801, BNC)",
    "Ko-fi": "https://ko-fi.com/fatics13",
    "PIX Brasil": "https://pay.belo.app/checkout?id=685cee090d4794d63e891e21",
    "USDT (TRC20)": "TLZaPT4b6Cm8mT2agNbS6MehE56dm5CpxZ",
    "Bitcoin": "1CxhH7mJhUbyMY53pEwSgiymMEuEmPDXJE"
}

# Logging básico
logging.basicConfig(level=logging.INFO)
