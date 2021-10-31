from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)
# from telegram import ()

import random
import datetime
import sys

from admin import API_KEY

LOGGING = False

updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher

def start_command(update,context):
    """Initializes the bot"""
    text =  'Hello '+(update.message.from_user.first_name or '@'+update.message.from_user.username )+', this is the divine pikachu.\n'
    text+= 'I will answer any questions you have to the best of my ability...'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text)
start_handler = CommandHandler('start', start_command)
dispatcher.add_handler(start_handler)

def pika_command(update,context):
    """Sends a pikachu sticker"""
    try:
        if random.random() < 0.01:
            return context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Pika... boo? 🙂"
            )
        pika_list = [
            'pikachu',
            'pikachu2',
            'PikachuDetective',
            'pikachu6',
            'pikach',
            'pikach_memes'
            ]
        pikas = []
        for pika in pika_list:
            pikas.extend(context.bot.get_sticker_set(pika).stickers)
        pikas.extend(context.bot.get_sticker_set('uwumon').stickers[:20])
        pika = random.choice(pikas)
        context.bot.send_sticker(
            chat_id=update.effective_chat.id,
            sticker=pika
        )
        print(update.effective_chat.title, update.effective_chat.id, update.message.from_user.username, update.message.from_user.first_name)
    except Exception as e:
        with open('error.txt','a') as f:
            print(f"Pika error at {(datetime.datetime.now()+datetime.timedelta(hours=8)).strftime('%m/%d/%Y, %H:%M:%S')}\nError is:\n{e}\n", file=f)

pika_handler = CommandHandler('pika', pika_command)
dispatcher.add_handler(pika_handler)

def question_message(update,context):
    try:
        query = update.message.text
        if query[-1]=='?':
            pika_command(update,context)
    except Exception as e:
        with open('error.txt','a') as f:
            print(f"Question error at {datetime.datetime.utcnow().strftime('%m/%d/%Y, %H:%M:%S')}\nError is:\n{e}\n", file=f)


question_handler = MessageHandler(Filters.text & (~Filters.command), question_message)
dispatcher.add_handler(question_handler)


def ohno_command(update,context):
    """Sends a version of "Oh no"..."""
    text = random.choice([
        "OH NO!",
        "Oh no indeed...",
        "Oh no",
        "Ah, that is not ideal",
        "This is a pleasant surprise without the pleasant",
        "Goodness gracious me!",
        "Oh noes",
        "Das not good",
        "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaah",
        "How could this happen?!",
        "This calls for an 'Oh no'.",
        "F in the chat",
        "What did you do!?",
        "Seriously...",
        "ono",
        "FSKSJFLKSDJFH",
        "My condolences",
        "Rest in peace good sir",
        "ohhh myyy gawwwd",
        "OMG!",
        "oh no",
        "oh no...?",
        "Bless you",
        "Are you sure you didn't mean 'Oh yes'?",
        "This is truly a disaster",
        "...",
        ])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text)

ohno_handler = CommandHandler('ohno', ohno_command)
dispatcher.add_handler(ohno_handler)

def stfu_command(update,context):
    """Sends a version of "stfu"..."""
    text = random.choice([
        "Please stfu",
        "Your mouth very big ah",
        "Can shut up anot",
        "Keep quiet la",
        "shhhhhhh",
        "Don't understand how to shut up isit",
        "Shut your trap",
        "Stop letting the cat out of the bag",
        "Be silent",
        "Silence, fool!",
        "woof woof stop barking bitch",
        "stfu thanks",
        "can shut your face",
        "Pretty please SHUT UP",
        "keep quiet or i threaten you with scissors",
        "OI cb i said keep quiet right",
        "Uno reverse, YOU stfu",
        "Your mouth got problem is it that's why cannot shut up",
        "very noisy leh u",
        "stop making noise plz",
        "zip it",
        "Diam la",
        "Which part of STFU do you not understand",
        "nvm just keep talking only, I got the whole day",
        "U then shut up",
        "You looked smart. That\'s until you opened your mouth",
        "Was wondering what\'s that smell but realised it\'s the bullshit coming from your mouth",
        "A moment of silence for the time wasted listening to your shit",
        "hocus pocus gag a cockus",
        "If silence is gold then you're definitely broke",
        "Do you need a pacifier or will my dick suffice",
        "stfu",
        "bitch stfu",
        "shut your bazoo",
        "you might at least have the courtesy to keep your cakehole closed",
        "the amazon rainforest can't replenish your oxygen",
        "mumbo jumbo stfu dumbo",
        "why u breathing my oxygen",
        "You should plant a tree to make up for the oxygen you waste",

        ])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text)

stfu_handler = CommandHandler('stfu', stfu_command)
dispatcher.add_handler(stfu_handler)


def alive(context):
    with open('log.txt','a') as f:
        print(f"Bot last alive at {(datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime('%m/%d/%Y, %H:%M:%S')}", file=f)

if __name__ == "__main__":
    try:
        if LOGGING:
            with open('log.txt','a') as f:
                print(f"\nSTARTED at {(datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime('%m/%d/%Y, %H:%M:%S')}", file=f)
            for hour in range(24):
                for minute in range(0,60,10):
                    updater.job_queue.run_daily(alive, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=hour, minute=minute, second=1))
        updater.start_polling()
        print(f"Bot started at {datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}")
        updater.idle()
    except Exception as e:
        print(e)
