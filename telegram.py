import telebot
from time import gmtime, strftime
from private import teletoken
from instalooter.looters import PostLooter

bot = telebot.TeleBot(teletoken)


def log(time, message):
    log_print(time, message.from_user.username, message.chat.id, message.text)


def log_print(time, user, user_id, command):
    log_file = open('message_log.txt', 'a')
    log_file.write('{}:@{}({}) \"{}\"\n'.format(time, user, user_id, command))
    log_file.close()


@bot.message_handler(commands=['start'])
def start_message(message):
    log(strftime("%Y-%m-%d %H:%M:%S", gmtime()), message)
    bot.send_message(message.chat.id, 'Welcome to InstaSaveBot, {}'.format(message.from_user.first_name))
    bot.send_message(message.chat.id, 'Send me an instagram link or a user\'s username like @username.\n\nNeed more help?\nJust tap: /help')
    bot.send_message(509291958, 'added new user, @{}\nchatid: {}'.format(message.from_user.username, message.chat.id))


@bot.message_handler(commands=['help'])
def help_message(message):
    log(strftime("%Y-%m-%d %H:%M:%S", gmtime()), message)
    help_output = 'This bot is easiest and fastet way to download from instagram.\n\n'
    help_output += 'To download instagram posts, send the post \'s URL to the bot.\n\n'
    help_output += 'To download stories or HD profile photos, send the account\'s ID to the bot.\nExample:\n@google\n\n'
    help_output += 'I\'ve sent you a picture that shows how to copy post URLs 👇'
    bot.send_message(message.chat.id, help_output)
    bot.send_photo(message.chat.id, open('./service_images/help.jpeg', 'rb'))


@bot.message_handler(commands=['status'])
def status_message(message):
    log(strftime("%Y-%m-%d %H:%M:%S", gmtime()), message)
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
    log(strftime("%Y-%m-%d %H:%M:%S", gmtime()), message)
    bot.send_message(message.chat.id, 'Now this function unavailable❌\n\nSorry 😓😓😓\n\nBut you can download Instagram photos!\nJust tap: /help')


@bot.message_handler(commands=['fix'])
def fix_message(message):
    log(strftime("%Y-%m-%d %H:%M:%S", gmtime()), message)
    bot.send_message(message.chat.id, 'Report sent‼️\n\nThank You for helping to develop the project\n')


@bot.message_handler(content_types=['text'])
def send_text(message):
    log(strftime("%Y-%m-%d %H:%M:%S", gmtime()), message)
    bot.send_message(509291958, '@{} send(id{}):\n\'{}\''.format(message.from_user.username, message.chat.id, message.text))
    if 'instagram.com/p/' in message.text:
        path = message.text
        looter = PostLooter(path)
        if looter.info['__typename'] == 'GraphImage':
            picture_id = looter.info['id']
            looter.download('./pictures/')
            bot.send_photo(message.chat.id, open('./pictures/{}.jpg'.format(picture_id), 'rb'), caption='🤖 Downloaded with @instsave_bot')
        elif looter.info['__typename'] == 'GraphVideo':
            video_id = looter.info['id']
            looter.download_videos('./videos/')
            bot.send_video(message.chat.id, open('./videos/{}.mp4'.format(video_id), 'rb'), caption='🤖 Downloaded with @instsave_bot')
        elif looter.info['__typename'] == 'GraphSidecar':
            bot.send_message(message.chat.id, 'Sorry, I can\'t send you post with more than 1 photo\n\nPlease try again')
    elif 'private' in message.text:
        bot.send_message(436264579, message.text[7:])
    else:
        bot.send_message(message.chat.id, 'Please, send link or username\n\nNeed more help?\nJust tap: /help')


bot.polling()
