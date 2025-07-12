import telebot

# Bot token
BOT_TOKEN = '7706823290:AAF2_MmdNC1zuIby-9DcAI_GdxC6sBR7wM0'
OWNER_ID = 6318824492  # Replace with your Telegram ID

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    welcome_msg = """Hi! 👋

Please join both channels to access the full VARC 1000 content:

🔹 [Join VARC 1000 Channel](https://t.me/+Kiqzg-zQ-81hNThl)  
🔹 [Join Elites Grid Channel](https://t.me/+Znyae4N7PUkxMDY9)

Once joined, you can message me here for any help! 😊
"""
    bot.send_message(msg.chat.id, welcome_msg, parse_mode='Markdown')

@bot.message_handler(func=lambda m: True)
def forward_message(msg):
    bot.forward_message(OWNER_ID, msg.chat.id, msg.message_id)

bot.polling()
