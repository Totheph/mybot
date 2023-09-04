import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO) #записывает информацию о работе бота в специальный файл, чтобы отслеживать ошибки

def greet_user(update, context): #update - то, что пришло с сервера тг (сообщение пользователя, информация о нем и т.д.)
  #context - благодаря ней мы можем отдавать команды боту, вызвавшему функцию (например, если хотим отправить сообщение другому пользователю)
  print("Вызван /start")  
  update.message.reply_text("Здравствуй, пользователь! Ты ввел команду /start")
  
def talk_to_me(update, context):
  text = update.message.text
  print(text)
  update.message.reply_text(text)

def main():
  mybot = Updater(settings.API_KEY, use_context=True)
  
  dp = mybot.dispatcher
  
  dp.add_handler(CommandHandler("start", greet_user))
  dp.add_handler(MessageHandler(Filters.text, talk_to_me))
  
  logging.info("Бот стартовал")
  
  
  mybot.start_polling() #чтобы он постоянно обращался к серверам тг за входящей информацией
  
  mybot.idle() #чтобы он работал всегда до остановки
  
  
if __name__ == "__main__":
  main()