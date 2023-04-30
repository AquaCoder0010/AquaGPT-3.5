import sys
import time
import telepot
import openai
from telepot.loop import MessageLoop



TOKEN = "BOT:TOKEN";
openai.api_key = "OPENAI:TOKEN";

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        bot.sendMessage(chat_id, "Thinking....");


        response = openai.ChatCompletion.create(model='gpt-3.5-turbo-0301',
                messages=[{'role': 'user', 'content': msg['text']}])
        

        bot.sendMessage(chat_id, response['choices'][0]['message']['content']);


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread();
# Keep the program running.

while 1:
    time.sleep(10)
