from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7940375943:AAEzNdhDYrHejyNN-mviRO0xw3koIsk_jnI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔞 Grupo Erótico", callback_data="erotico")],
        [InlineKeyboardButton("🔥 Grupo Explícito", callback_data="explicito")],
        [InlineKeyboardButton("💬 WhatsApp", callback_data="whatsapp")],
        [InlineKeyboardButton("💖 Contenido Personalizado", url="https://t.me/Cuevas0202")],
        [InlineKeyboardButton("🌐 Mis páginas hot", callback_data="paginas")],
        [InlineKeyboardButton("👥 Comunidad FATICS", url="https://t.me/fatics_13")],
        [InlineKeyboardButton("❓¿Problemas?", url="https://t.me/Cuevas0202")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bienvenido a *FATICS BOT*. Elige una opción:", reply_markup=reply_markup, parse_mode="Markdown")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "erotico":
        await query.edit_message_text(
            text="👀 *Grupo Erótico*
Contenido erótico, picante y excitante.

Elige un método de pago:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("PayPal", url="https://paypal.me/fati0202")],
                [InlineKeyboardButton("Ko-fi", url="https://ko-fi.com/fatics")],
                [InlineKeyboardButton("PIX (Brasil)", url="https://pay.belo.app/checkout?id=685cee090d4794d63e891e21")],
                [InlineKeyboardButton("Pago móvil 🇻🇪", callback_data="venezolano")],
                [InlineKeyboardButton("Cripto (USDT / BTC)", callback_data="cripto")],
                [InlineKeyboardButton("Zelle (pedir)", url="https://t.me/Cuevas0202")]
            ]),
            parse_mode="Markdown"
        )

    elif query.data == "explicito":
        await query.edit_message_text(
            text="🍑 *Grupo Explícito*
Todos mis videos íntimos, sin censura y contenido futuro 🔥

Métodos de pago:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("PayPal", url="https://paypal.me/fati0202")],
                [InlineKeyboardButton("Ko-fi", url="https://ko-fi.com/fatics")],
                [InlineKeyboardButton("PIX (Brasil)", url="https://pay.belo.app/checkout?id=685cee090d4794d63e891e21")],
                [InlineKeyboardButton("Pago móvil 🇻🇪", callback_data="venezolano")],
                [InlineKeyboardButton("Cripto (USDT / BTC)", callback_data="cripto")],
                [InlineKeyboardButton("Zelle (pedir)", url="https://t.me/Cuevas0202")]
            ]),
            parse_mode="Markdown"
        )

    elif query.data == "whatsapp":
        await query.edit_message_text(
            text="💬 *Acceso a mi WhatsApp privado*
Precio: $70 (pago único)

Elige cómo deseas pagar:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("PayPal", url="https://paypal.me/fati0202")],
                [InlineKeyboardButton("Ko-fi", url="https://ko-fi.com/fatics")],
                [InlineKeyboardButton("PIX (Brasil)", url="https://pay.belo.app/checkout?id=685cee090d4794d63e891e21")],
                [InlineKeyboardButton("Pago móvil 🇻🇪", callback_data="venezolano")],
                [InlineKeyboardButton("Cripto (USDT / BTC)", callback_data="cripto")],
                [InlineKeyboardButton("Zelle (pedir)", url="https://t.me/Cuevas0202")]
            ]),
            parse_mode="Markdown"
        )

    elif query.data == "paginas":
        await query.edit_message_text(
            text="👄 *Mis páginas hot:*

- [Fansly](https://fans.ly/Fatics_) (con videos secretos 👀)
- [OnlyFans](https://onlyfans.com/cuevas0202)
- [MiPriv](https://mipriv.com/fatics)",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )

    elif query.data == "venezolano":
        await query.edit_message_text(
            text="🇻🇪 *Pago Móvil Venezuela*

Banco: BNC
Teléfono: 04125294977
Cédula: 31075801

Después de pagar, envía el comprobante a @Cuevas0202 para validar.",
            parse_mode="Markdown"
        )

    elif query.data == "cripto":
        await query.edit_message_text(
            text="💰 *Criptomonedas*

USDT (TRC20): `TLZaPT4b6Cm8mT2agNbS6MehE56dm5CpxZ`
BTC: `1CxhH7mJhUbyMY53pEwSgiymMEuEmPDXJE`

Envíame el comprobante por Telegram a @Cuevas0202",
            parse_mode="Markdown"
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
