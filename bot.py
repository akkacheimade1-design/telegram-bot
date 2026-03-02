from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8259519039:AAGeE-8bLRprIKiRi6qvZM0kd4apEgCyDJo"

# القائمة الرئيسية
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎓 تقني رياضي", callback_data="tech")],
        [InlineKeyboardButton("💰 نقاطي", callback_data="points")],
        [InlineKeyboardButton("🔄 استبدال النقاط", callback_data="exchange")],
        [InlineKeyboardButton("❓ الأسئلة", callback_data="questions")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text("اختر من القائمة:", reply_markup=reply_markup)
    else:
        await update.callback_query.edit_message_text("اختر من القائمة:", reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await main_menu(update, context)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "tech":
        keyboard = [
            [InlineKeyboardButton("⚙️ هندسة ميكانيكية", callback_data="mech")],
            [InlineKeyboardButton("⚡ هندسة كهربائية", callback_data="elec")],
            [InlineKeyboardButton("🏗️ هندسة مدنية", callback_data="civil")],
            [InlineKeyboardButton("🧪 هندسة طرائق", callback_data="process")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="back")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("اختر الفرع:", reply_markup=reply_markup)

    elif query.data == "points":
        await query.edit_message_text("رصيدك الحالي: 0 نقطة")

    elif query.data == "exchange":
        await query.edit_message_text("قريبًا يمكنك استبدال النقاط بالنجوم ⭐")

    elif query.data == "questions":
        await query.edit_message_text("هذا البوت يوفر ملخصات وتمارين خاصة بشعبة تقني رياضي.")

    elif query.data in ["mech", "elec", "civil", "process"]:
        await query.edit_message_text("قريبًا سيتم إضافة ملخصات وتمارين لهذا الفرع 📚")

    elif query.data == "back":
        await main_menu(update, context)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
