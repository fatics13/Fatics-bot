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
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "7940375943:AAEzNdhDYrHejyNN-mviRO0xw3koIsk_jnI"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("💗 Grupo Erótico (Mensual)", callback_data="grupo_erotico"),
        InlineKeyboardButton("🔥 Grupo Explícito (Pago Único)", callback_data="grupo_explicito"),
        InlineKeyboardButton("💬 WhatsApp Directo", callback_data="whatsapp"),
        InlineKeyboardButton("🎁 Contenido Personalizado", url="https://t.me/fatics_13")
    )

    bienvenida = f"Hola, {message.from_user.first_name} 💖\n\n"
    bienvenida += "Bienvenida a FATICS Bot. ¿Qué deseas hoy?"
    bot.send_message(message.chat.id, bienvenida, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "grupo_erotico":
        texto = "👀 Grupo erótico picante y con sorteos atrevidos. Puedes pagar así:\n\n"
        texto += "💳 **Ko-fi (PayPal o tarjeta):** [Pagar $15](https://ko-fi.com/s/4bfe9de9f5)\n"
        texto += "🇧🇷 **PIX:** [Pagar con PIX](https://pay.belo.app/checkout?id=685cee090d4794d63e891e21)\n"
        texto += "💸 **Cripto:** USDT (TRC20) `TLZaPT4b6Cm8mT2agNbS6MehE56dm5CpxZ`\n"
        texto += "\nLuego de pagar, envía el comprobante aquí 🧾 y espera la verificación 💌"

        bot.send_message(call.message.chat.id, texto, parse_mode="Markdown")

    elif call.data == "grupo_explicito":
        texto = "🔞 Grupo con TODOS mis videos más fuertes + lo nuevo que viene 🔥\n\n"
        texto += "💳 **Ko-fi (PayPal o tarjeta):** [Pagar $300](https://ko-fi.com/s/c5ef62fca7)\n"
        texto += "💸 **Cripto:** USDT (TRC20) `TLZaPT4b6Cm8mT2agNbS6MehE56dm5CpxZ`\n"
        texto += "\nDespués de pagar, mándame el comprobante y te doy acceso 🔐"

        bot.send_message(call.message.chat.id, texto, parse_mode="Markdown")

    elif call.data == "whatsapp":
        bot.send_message(call.message.chat.id, "✨ Mi WhatsApp directo: +58 412 5294977 💕")

bot.infinity_polling()
