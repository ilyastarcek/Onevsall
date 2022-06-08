#!/usr/bin/python
# This is a simple echo bot using the decorator mechanism.
import random
con1 = False
players = []
def ramdomqwish():
    l = list(range(0, 16))
    random.shuffle(l)
    return l[6:]

randomq = ramdomqwish()

def pre():
    with open('q.txt', 'w') as q:
        q.write('0')
    q.close()
    with open('game.txt', 'w') as q:
        q.write('\n\n\n\n\n\n')

def tn():
    t = 0
    with open('q.txt') as q:
        t = int(q.readline())
    with open('q.txt', 'w') as q:
        q.write(str(t+1))
    with open('q.txt') as q:
        t = int(q.readline())
    q.close()
    return t

from telebot import TeleBot

bot = TeleBot('5597396246:AAHSh0z3UdeF3qzxkIdahRuwNaQBQ02qt7A')

#from aiogram import types

from telebot import types

t = 0
id = 0
def qwestionsss(messege,id,nq):
    print('g')
    with open('answers.txt') as answer:
        with open('qwestions.txt') as qwestion:
            answers = answer.readlines()
            qwestions = qwestion.readlines()
            answerss = answers[nq].split('. ')
            
            
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton(answerss[0], callback_data='1')
            buttonC = types.InlineKeyboardButton(answerss[2], callback_data='3')
            buttonD = types.InlineKeyboardButton(answerss[3], callback_data='4')
            buttonB = types.InlineKeyboardButton(answerss[1],callback_data='2')

            markup.row(buttonA, buttonB)
            markup.row(buttonC, buttonD)

    
    
            bot.delete_message(chat_id = messege, message_id = id)
            bot.send_message(messege, qwestions[nq], reply_markup = markup)
            print('g')


@bot.message_handler(commands=['start'])
def start(message):
    pre()
    pas = 0
    bot.send_message(message.chat.id, 'Привет!')
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton('Да', callback_data='да')
    buttonB = types.InlineKeyboardButton('Нет', callback_data='нет')

    id = message.chat.id
    markup.row(buttonA, buttonB)
    bot.send_message(message.chat.id, 'Сейчас идет игра. Ты в ней участвуешь?',reply_markup = markup)
    '''
    while con1 != True:
        pas += 0
    answers=[]         
    qwestions = []
    nq = randomq[0]
    with open('answers.txt') as answer:
        answers = answer.readlines()
    with open('qwestions.txt') as qwestion:
        qwestions = qwestion.readlines()
    answers[nq] = answers[nq].split('. ')
            
            
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton(answers[nq][0], callback_data='1')
    buttonC = types.InlineKeyboardButton(answers[nq][2], callback_data='3')
    buttonD = types.InlineKeyboardButton(answers[nq][3], callback_data='4')
    buttonB = types.InlineKeyboardButton(answers[nq][1],callback_data='2')

    markup.row(buttonA, buttonB)
    markup.row(buttonC, buttonD)

    
    
    bot.send_message(message.chat.id, qwestions[nq], reply_markup = markup)
            
    print('f')
    for i in range(1,):
        qwestion(randomq[i],message.chat.id)
    ''' 

#@bot.message_handler(content_types=["Нет"])
#def no(message):
    #bot.sendMessage(message.chat.id, 'Хорошо. Подожди, когда эта игра закончится.')
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    #bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == 'нет':
        answer = 'Хорошо. Подожди, когда эта игра закончится.'
        bot.send_message(call.message.chat.id, answer)
    elif call.data == 'да':
        if len(players) < 6:
            players.append(call.message.chat.id)
            print(players)
            answer = 'Для начала тебе надо ответить на несколько вопросов:'
            bot.send_message(call.message.chat.id, answer)
            con1 = True
            answers=[]         
            qwestions = []
            nq = randomq[t]
            with open('answers.txt') as answerd:
                answersss = answerd.readlines()
            
            with open('qwestions.txt') as qwestion:
                qwestions = qwestion.readlines()
            answerss = answersss[nq].split('. ')
                   
                    
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton(answerss[0], callback_data='1')
            buttonC = types.InlineKeyboardButton(answerss[2], callback_data='3')
            buttonD = types.InlineKeyboardButton(answerss[3], callback_data='4')
            buttonB = types.InlineKeyboardButton(answerss[1], callback_data='2')
        
            markup.row(buttonA, buttonB)
            markup.row(buttonC, buttonD)
 
    
            answerd.close() 
            qwestion.close() 
            bot.send_message(call.message.chat.id, qwestions[nq], reply_markup = markup)
            print()
            
            
            print('f')

            

    elif call.data == '4' or call.data == '2' or call.data == '1' or call.data == '3':
        filel = []
        with open('game.txt', 'r') as file:
            print(file)
            filel = file.readlines()
            d = players.index(call.message.chat.id)
            print(filel)
            filel[d] = call.data
        with open('game.txt', 'w') as filew:
            filew.writelines(filel)
        a = tn()
        if a <= 9:
            qwestionsss(call.message.chat.id,call.message.id,randomq[a])
        else:
            bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
            bot.send_message(call.message.chat.id, 'УРА!!!')
            

bot.polling(none_stop=True, interval=1)  
  
