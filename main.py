import settings
from telegram_bot import TelegramBot

bot = TelegramBot(settings.BOT_TOKEN, bot_user_id=settings.BOT_USER_ID)


def main():
    try:
        bot.start()
    except Exception as err:
        print('error', err, flush=True)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
