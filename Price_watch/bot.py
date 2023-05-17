import os
import telebot
import sys

bot = telebot.TeleBot('6022694210:AAG0HXT_cxYjk0Vrtu-K-uPsr8h5YEAJgyY')
vendor_ids = []
vendor_index = []
vendor_name = []
vendor_location = []
vendor_user = []
# Populate vendor IDs from the file
with open('business_info.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line != '':
            vendor = line.split(':')
            vendor_ids.append(vendor[0])
            vendor_index.append(vendor[0])
            vendor_name.append(vendor[1])
            vendor_location.append(vendor[2])
@bot.message_handler(content_types=['photo'])
def send_to_vendors(message):
    # Get the photo and user information
    photo = message.photo[-1].file_id
    user_id = message.from_user.id
    vendor_user.append(user_id)
    # Forward the photo and user information to each vendor
    for vendor_id in vendor_ids:
        bot.forward_message(chat_id=vendor_id, from_chat_id=user_id, message_id=message.message_id)
        bot.send_message(chat_id=vendor_id, text="Please provide the price")

    # Reply to the user
    for vendor_id in vendor_ids:
        bot.send_message(chat_id=user_id, text=f"Your request has been forwarded to the vendors")
    

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_reply(message):
    use = vendor_user[0]
    
    for vendor_id in vendor_ids:
        bot.send_message(chat_id=use, text=f"Name: {vendor_name[vendor_index.index(vendor_id)]}, Location:{vendor_location[vendor_index.index(vendor_id)]}")
        bot.send_message(chat_id=use, text=f" {message.text}")
    bot.stop_polling()

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            # restart the bot if an error occurs
            os.execv(sys.executable, ['python'] + [__file__])
