from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7940375943:AAEzNdhDYrHejyNN-mviRO0xw3koIsk_jnI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🍑 Grupo Erótico", callback_data="erotico")],
        [InlineKeyboardButton("🔥 Grupo Explícito", callback_data="explicito")],
        [InlineKeyboardButton("💬 WhatsApp", callback_data="whatsapp")],
        [InlineKeyboardButton("💖 Contenido personalizado", callback_data="personalizado")],
        [InlineKeyboardButton("🌐 Mis páginas hot", callback_data="paginas")],
        [InlineKeyboardButton("👥 Comunidad", url="https://t.me/fatics_13")],
        [InlineKeyboardButton("❓¿Problemas?", url="https://t.me/Cuevas0202")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("¡Hola! 💕 Elige una opción:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "erotico":
        await query.edit_message_text(
            text="""👀 *Grupo Erótico*
Contenido erótico, picante y excitante. A veces incluye giveaways atrevidos.

Elige un método de pago:""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("PayPal", url="https://paypal.me/fati0202")],
                [InlineKeyboardButton("Ko-fi", url="https://ko-fi.com/fatics")],
                [InlineKeyboardButton("Pago Móvil Venezuela", callback_data="venezolano")],
                [InlineKeyboardButton("Criptomonedas", callback_data="cripto")],
                [InlineKeyboardButton("Zelle", callback_data="zelle")],
            ]),
            parse_mode="Markdown"
        )

    elif query.data == "explicito":
        await query.edit_message_text(
            text="""🍑 *Grupo Explícito*
Todos mis videos íntimos, sin censura y contenido futuro 🔥

Elige un método de pago:""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("PayPal", url="https://paypal.me/fati0202")],
                [InlineKeyboardButton("Ko-fi", url="https://ko-fi.com/fatics")],
                [InlineKeyboardButton("Pago Móvil Venezuela", callback_data="venezolano")],
                [InlineKeyboardButton("Criptomonedas", callback_data="cripto")],
                [InlineKeyboardButton("Zelle", callback_data="zelle")],
            ]),
            parse_mode="Markdown"
        )

    elif query.data == "whatsapp":
        await query.edit_message_text(
            text="""💬 *Acceso a mi WhatsApp privado*
Precio: $70 (pago único)

Elige cómo deseas pagar:""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("PayPal", url="https://paypal.me/fati0202")],
                [InlineKeyboardButton("Ko-fi", url="https://ko-fi.com/fatics")],
                [InlineKeyboardButton("Pago Móvil Venezuela", callback_data="venezolano")],
                [InlineKeyboardButton("Criptomonedas", callback_data="cripto")],
                [InlineKeyboardButton("Zelle", callback_data="zelle")],
            ]),
            parse_mode="Markdown"
        )

    elif query.data == "personalizado":
        await query.edit_message_text(
            text="💖 Para contenido personalizado, escríbeme directo a mi Telegram: @Cuevas0202",
            parse_mode="Markdown"
        )

    elif query.data == "paginas":
        await query.edit_message_text(
            text="""👄 *Mis páginas hot:*

- [Fansly](https://fans.ly/Fatics_) (contenido porno)
- [OnlyFans](https://onlyfans.com/cuevas0202)
- [MiPriv](https://mipriv.com/fatics)""",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )

    elif query.data == "venezolano":
        await query.edit_message_text(
            text="""🇻🇪 *Pago Móvil Venezuela*

Banco: BNC  
Teléfono: 04125294977  
Cédula: 31075801

Después de pagar, envía el comprobante por Telegram a @Cuevas0202""",
            parse_mode="Markdown"
        )

    elif query.data == "cripto":
        await query.edit_message_text(
            text="""🪙 *Criptomonedas*

USDT (TRC20): `TLZaPT4b6Cm8mT2agNbS6MehE56dm5CpxZ`  
BTC: `1CxhH7mJhUbyMY53pEwSgiymMEuEmPDXJE`

Envíame el comprobante por Telegram a @Cuevas0202""",
            parse_mode="Markdown"
        )

    elif query.data == "zelle":
        await query.edit_message_text(
            text="""Zelle disponible 💵  
Solicítame los datos por privado: @Cuevas0202""",
            parse_mode="Markdown"
        )

if __name__ == "__main__":
    import asyncio

    async def main():
        application = Application.builder().token(TOKEN).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(button))

        await application.initialize()
        await application.start()
        await application.updater.start_polling()
        await application.updater.idle()

    asyncio.run(main())
