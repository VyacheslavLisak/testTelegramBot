import botToken
import telebot

'''Token from @BotFather'''
bot = telebot.TeleBot(botToken.BOT_TOKEN)

'''Creating keybord with only 1 key'''
keyboardMain = telebot.types.ReplyKeyboardMarkup(True)
keyboardMain.row('У меня возникла проблема')

'''Creating keybord with problems. Max keys = 12'''
keyboardProblems = telebot.types.ReplyKeyboardMarkup(True, True)
keyboardProblems.row('Ничего не работает', 'Совсем ничего не работает')

'''Starting chat and creating keyboardMain'''
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'У вас возникли проблемы?', reply_markup=keyboardMain)

'''Replying on commands'''
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'у меня возникла проблема':
        bot.send_message(message.chat.id, 'Какая проблема у вас возникла?', reply_markup=keyboardProblems)

    elif message.text.lower() == 'ничего не работает':
        bot.send_message(message.chat.id, 'Очень жаль')

    elif message.text.lower() == 'совсем ничего не работает':
        bot.send_message(message.chat.id, 'Прям совсем грустно')

'''Keep running'''
bot.polling()
