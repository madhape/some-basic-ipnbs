import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

def start_command(bot, update):
    text = 'Привет! Я бот с курса IT-Recruiter'
    print(text)
    update.message.reply_text(text)


def parrot_function(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
#@quokka666_bot:
    mybot = Updater("736859883:AAGKDq6uMuVxo6WcixnfKNH5_mrCwjMQ2y8")
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, parrot_function))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()