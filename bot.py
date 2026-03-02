from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# ضع التوكن هنا
TOKEN = "8259519039:AAGeE-8bLRprIKiRi6qvZM0kd4apEgCyDJo"

# قاعدة بيانات بسيطة لتجربة النقاط
users_points = {}

# القائمة الرئيسية
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎓 تقني رياضي", callback_data="branch")],
        [InlineKeyboardButton("💰 نقاطي", callback_data="points")],
        [InlineKeyboardButton("🔄 استبدال النقاط", callback_data="exchange")],
        [InlineKeyboardButton("❓ الأسئلة", callback_data="faq")]
    ]
    return InlineKeyboardMarkup(keyboard)

# أزرار التخصصات داخل تقني رياضي
def tech_branch_keyboard():
    keyboard = [
        [InlineKeyboardButton("هندسة ميكانيكية", callback_data="mechanical")],
        [InlineKeyboardButton("هندسة كهربائية", callback_data="electrical")],
        [InlineKeyboardButton("هندسة طرائق", callback_data="process")],
        [InlineKeyboardButton("هندسة مدنية", callback_data="civil")],
        [InlineKeyboardButton("⬅️ رجوع", callback_data="back")]
    ]
    return InlineKeyboardMarkup(keyboard)

# دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in users_points:
        users_points[user_id] = 0
    await update.message.reply_text("اختر من القائمة:", reply_markup=main_menu_keyboard())

# معالجة الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    if user_id not in users_points:
        users_points[user_id] = 0

    data = query.data

    if data == "branch":
        await query.edit_message_text("اختر فرعك:", reply_markup=tech_branch_keyboard())
    elif data == "points":
        await query.edit_message_text(f"لديك {users_points[user_id]} نقطة/نقاط.", reply_markup=main_menu_keyboard())
    elif data == "exchange":
        await query.edit_message_text("هنا يمكن شراء الملخصات باستخدام النقاط (لم تطبق بعد).", reply_markup=main_menu_keyboard())
    elif data == "faq":
        await query.edit_message_text("يمكنك السؤال عن البوت أو الملخصات هنا (لم تطبق بعد).", reply_markup=main_menu_keyboard())
    elif data == "back":
        await query.edit_message_text("اختر من القائمة:", reply_markup=main_menu_keyboard())
    elif data in ["mechanical", "electrical", "process", "civil"]:
        await query.edit_message_text(f"لقد اخترت {data}. هنا ستظهر الملخصات والتمارين الخاصة بالفرع.", reply_markup=tech_branch_keyboard())
        # لاحقًا يمكن إضافة خصم النقاط عند شراء ملخص:
        # users_points[user_id] -= 3

# تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("البوت يعمل الآن...")
app.run_polling()
