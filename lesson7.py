import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


def render_progressbar(total, iteration, prefix='', suffix='',
                       length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id, text, bot):
    text = parse(text)
    message = 'Запускаю таймер...' + '\n' + render_progressbar(text, 0)
    message_id = bot.send_message(chat_id, message)
    bot.create_countdown(text, notify_progress, chat_id=chat_id,
                         message_id=message_id, text=text, bot=bot)
    bot.create_timer(text+0.01, the_end, chat_id=chat_id,
                     message_id=message_id, text=text, bot=bot)


def notify_progress(secs, chat_id, message_id, text, bot):
    message = "Осталось секунд: {}".format(secs) + '\n' \
              + render_progressbar(text, text-secs)
    bot.update_message(chat_id, message_id, message)


def the_end(chat_id, message_id, text, bot):
    message = 'Время вышло!' + '\n' + render_progressbar(text, text)
    bot.update_message(chat_id, message_id, message)


def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(reply, bot=bot)
    bot.run_bot()


if __name__ == '__main__':
    main()
