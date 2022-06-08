#!/usr/bin/python
# This is a simple echo bot using the decorator mechanism.
import random
con1 = False

def ramdomqwish():
    l = list(range(0, 16))
    random.shuffle(l)
    return l[6:]

randomq = ramdomqwish()



from telebot import TeleBot

bot = TeleBot('5597396246:AAHSh0z3UdeF3qzxkIdahRuwNaQBQ02qt7A')

#from aiogram import types

from telebot import types


def qwestion(nq,messege):
    print('g')
    with open('answers.txt') as answer:
        with open('qwestions.txt') as qwestion:
            answers = answer.readlines()
            qwestions = qwestion.readlines()
            answerss = answers[nq].split('. ')
            
            
            markup = types.ReplyKeyboardMarkup()
            buttonA = types.KeyboardButton(answerss[0], callback_data='1')
            buttonC = types.KeyboardButton(answerss[2], callback_data='3')
            buttonD = types.KeyboardButton(answerss[3], callback_data='4')
            buttonB = types.KeyboardButton(answerss[1],callback_data='2')

            markup.row(buttonA, buttonB)
            markup.row(buttonC, buttonD)

    
    
            bot.edit_message_text(messege, text = qwestions[nq], reply_markup = markup)
            print('g')


@bot.message_handler(commands=['start'])
def start(message):
    pas = 0
    bot.send_message(message.chat.id, 'Привет!')
    markup = types.ReplyKeyboardMarkup()
    buttonA = types.KeyboardButton('Да')
    buttonB = types.KeyboardButton('Нет')


    markup.row(buttonA, buttonB)
    bot.send_message(message.chat.id, 'Сейчас идет игра. Ты в ней участвуешь?',reply_markup = markup)
    while con1 != True:
        pas += 0
    bot.send_message(message.chat.id, 'Для начала тебе надо ответить на несколько вопросов:')
    answers=[]         
    qwestions = []
    nq = randomq[0]
    with open('answers.txt') as answer:
        answers = answer.readlines()
    with open('qwestions.txt') as qwestion:
        qwestions = qwestion.readlines()
    answers[nq] = answers[nq].split('. ')
            
            
    markup = types.ReplyKeyboardMarkup()
    buttonA = types.KeyboardButton(answers[nq][0], callback_data='1')
    buttonC = types.KeyboardButton(answers[nq][2], callback_data='3')
    buttonD = types.KeyboardButton(answers[nq][3], callback_data='4')
    buttonB = types.KeyboardButton(answers[nq][1],callback_data='2')

    markup.row(buttonA, buttonB)
    markup.row(buttonC, buttonD)

    
    
    bot.send_message(message.chat.id, qwestions[nq], reply_markup = markup)
            
    print('f')
    for i in range(1,):
        qwestion(randomq[i],message.chat.id)
      

@bot.message_handler(content_types=["Нет"])
def no(message):
    bot.sendMessage(message.chat.id, 'Хорошо. Подожди, когда эта игра закончится.')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    #bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == 'нет':
        no()
    elif call.data == '4':
        answer = 'Вы хорошист!'
    elif call.data == '5':
        answer = 'Вы отличник!'

    bot.send_message(call.message.chat.id, answer)

bot.polling(none_stop=True, interval=1)  


 
