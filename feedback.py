import telebot

TOKEN = '7177189959:AAFGBlxc71EtvA6YEyFGZSSGBzTkZ3jLIqQ'

bot = telebot.TeleBot(TOKEN)


def send_feedback(email, msg):
    bot.send_message(931534758, f"Email: {email} \n Message: {msg}", parse_mode="HTML")