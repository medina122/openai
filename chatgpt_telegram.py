import telebot 
import logging
import openai 
from api import openai_token
from api import telegram_token
from datetime import datetime

openai.api_key = openai_token
bot = telebot.TeleBot(telegram_token)

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.1
    )

    message = completions.choices[0].text
    return message

def logger(firstname, username, content):
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    data = f'{time} - {firstname} @{username}: {content}'
    print(data)

@bot.message_handler(['start'])
def welcome(message):
    response = 'Welcome to ChatGPT Bot! \n\nSpanish not supported yet'
    bot.send_message(chat_id=message.chat.id, text=response)

@bot.message_handler(func=lambda message: True)
def process_message(message):

    response = generate_response(message.text)
    logger(message.from_user.first_name, message.from_user.username, message.text)
    
    bot.send_message(chat_id=message.chat.id, text=response)
    
    print(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Bot @Bot: {str(response).strip()}')

if __name__ == '__main__':

    print('RESPONSE: 200 - SERVER IS RUNNING')
    bot.polling(non_stop=True)
