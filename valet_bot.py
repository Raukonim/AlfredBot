import sys
import time
import random
import datetime
import pprint
import telepot
import emoji



def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print 'Chat Message:', content_type, chat_type, chat_id

    if content_type == 'text':
        command = msg['text']

        print 'Got command: %s' % command

        if command == '/roll':
            bot.sendMessage(chat_id, random.randint(1,6))
        elif command == '/time':
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
        elif command == '/roll20':
            bot.sendMessage(chat_id, random.randint(1,20))
        elif command == '/coffee':
            bot.sendMessage(chat_id, emoji.emojize(':coffee:', use_aliases=True))


def on_inline_query(msg):
    # Just dump inline query to answerer
    answerer.answer(msg)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print 'Chosen Inline Result:', result_id, from_id, query_string

def compute_answer(inline_query):
    articles = [{'type': 'article',
                     'id': 'abc', 'title': 'ABC', 'message_text': 'Mi nombre es Alfred y soy tu bot mayordomo'}]

    return articles

TOKEN = sys.argv[1] # get token from command-line

bot = telepot.Bot(TOKEN)

# Create the Answere, give it the compute function.
answerer = telepot.helper.Answerer(bot, compute_answer)

bot.notifyOnMessage({'normal': on_chat_message,
                     'inline_query': on_inline_query,
                     'chosen_inline_result': on_chosen_inline_result})
print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
