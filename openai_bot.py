import telebot 
import openai 
from api import openai_token, telegram_token

openai.api_key = openai_token
model_engine = 'text-davinci-003'
bot = telebot.TeleBot(telegram_token)

@bot.message_handler(func=lambda message: True)
def get_codex(message):
    response = openai.Completion.create(
        engine="code-davinci-001",
        prompt='"""\n{}\n"""'.format(message.text),
        n=1,
        temperature=0.5,
        max_tokens=1200,
        stop=None)
    
    bot.send_message(message.chat.id, response["choices"][0]["text"])

bot.infinity_polling()

