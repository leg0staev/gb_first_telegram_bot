from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_token import TOKEN


welcome_speech = \
    """Привет, я тестовый бот!
Я могу выполнять пока всего две комманды:
здороваться по команде /hello и складывать два чиисла.
Чтобы сложить 2 числа пришли мне комманду /sum и два числа после пробела.
например /sum 2 3"""


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a, b = int(items[1]), int(items[2])
    await update.message.reply_text(f'{a} + {b} = {a + b}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_speech)

app = ApplicationBuilder().token(TOKEN).build()

# start_handler = CommandHandler('start', start)
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()
