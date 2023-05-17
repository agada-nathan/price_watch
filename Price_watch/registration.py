import telebot
import requests.exceptions
import time

# Replace YOUR_TOKEN with your own Telegram bot token
bot = telebot.TeleBot("6128011521:AAEo95b8qUQF4r3NKoDqOPTG_C5jtN07IRE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! What is the name of your business?")
    bot.register_next_step_handler(message, ask_business_name)

def ask_business_name(message):
    chat_id = message.chat.id
    business_name = message.text.strip()
    bot.reply_to(message, "Please share your location.")
    bot.register_next_step_handler(message, save_business_info, chat_id, business_name)

def save_business_info(message, chat_id, business_name):
    location = message.text.strip()
    with open("business_info.txt", "a") as info_file, open("chat_ids.txt", "a") as chat_file:
        info_file.write(f"{chat_id}:{business_name}:{location}\n")
        chat_file.write(f"{chat_id}\n")
    bot.reply_to(message, f"Thanks, {business_name} and your location have been saved to our systems.")

while True:
    try:
        bot.polling()
    except requests.exceptions.ReadTimeout as e:
        print(f"Request timed out: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)



#bot = telebot.TeleBot("6128011521:AAEo95b8qUQF4r3NKoDqOPTG_C5jtN07IRE")