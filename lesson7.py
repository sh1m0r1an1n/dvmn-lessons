import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse
load_dotenv()


TG_TOKEN = os.getenv('TG_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID')
BOT = ptbot.Bot(TG_TOKEN)


def render_progressbar(total, iteration, prefix='', suffix='',
                       length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id, text):
    text = parse(text)
    message = 'Запускаю таймер...' + '\n' + render_progressbar(text, 0)
    message_id = BOT.send_message(chat_id, message)
    BOT.create_countdown(text, notify_progress, chat_id=chat_id,
                         message_id=message_id, text=text)
    BOT.create_timer(text+0.01, the_end, chat_id=chat_id,
                     message_id=message_id, text=text)


def notify_progress(secs, chat_id, message_id, text):
    message = "Осталось секунд: {}".format(secs) + '\n' \
              + render_progressbar(text, text-secs)
    BOT.update_message(chat_id, message_id, message)


def the_end(chat_id, message_id, text):
    message = 'Время вышло!' + '\n' + render_progressbar(text, text)
    BOT.update_message(chat_id, message_id, message)


def main():
    BOT.reply_on_message(reply)
    BOT.run_bot()


if __name__ == '__main__':
    main()
