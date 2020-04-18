import telebot
from time import gmtime, strftime
from private import teletoken

bot = telebot.TeleBot(teletoken)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome to InstaSaveBot, {}'.format(message.from_user.first_name))
    bot.send_message(message.chat.id, 'Send me an instagram link or a user\'s username like @username.\n\nNeed more help?\nJust tap: /help')
    bot.send_message(509291958, 'added new user, @{}\nchatid: {}'.format(message.from_user.username, message.chat.id))


@bot.message_handler(commands=['help'])
def help_message(message):
    help_output = 'This bot is easiest and fastet way to download from instagram.\n\n'
    help_output += 'To download instagram posts, send the post \'s URL to the bot.\n\n'
    help_output += 'To download stories or HD profile photos, send the account\'s ID to the bot.\nExample:\n@google\n\n'
    help_output += 'I\'ve sent you a picture that shows how to copy post URLs 👇'
    bot.send_message(message.chat.id, help_output)
    bot.send_photo(message.chat.id, open('help.jpeg', 'rb'))


@bot.message_handler(commands=['status'])
def status_message(message):
    status_output = 'STATUS:\n🟢Online\n'
    status_output += 'Server datatime: '
    status_output += strftime("%Y-%m-%d %H:%M:%S", gmtime())
    status_output += '\nActive tasks: 0/10 (0%)✅'
    status_output += '\nYour chatId: '
    status_output += str(message.chat.id)
    status_output += '\nBot version: v1.0.0'
    bot.send_message(message.chat.id, status_output)


@bot.message_handler(commands=['youtube'])
def youtube_message(message):
    bot.send_message(message.chat.id, 'Now this function unavailable❌\n\nSorry 😓😓😓\n\nBut you can download Instagram photos!\nJust tap: /help')


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_photo(message.chat.id, open('Sorry.png', 'rb'))
    bot.send_message(message.chat.id, 'Please, contact administrator or tap: /help')


bot.polling()
