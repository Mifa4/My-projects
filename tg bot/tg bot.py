import time
import telebot

bot = telebot.TeleBot('7420887381:AAGecl7rRITDSIXzxJS9uePhAOlibGhIL90')

print('bot was started.')

while True:
    try:
        @bot.message_handler(content_types='photo')
        def photo(message):
            if message.from_user.language_code == 'ru':
                bot.reply_to(message,'Я немогу понимать фото но я надеюсь это хорошее фото.')
            else:
                bot.reply_to(message,'I can`t understand phot but I think it is good photo.')

        @bot.message_handler(content_types='audio')
        def audio(message):
            if message.from_user.language_code == 'ru':
                bot.reply_to(message,'Я немогу понимать аудио но я надеюсь это хорошее аудио.')
            else:
                bot.reply_to(message,'I can`t understand audio but I think it is good audio.')

        @bot.message_handler()
        def main(message):
            if message.from_user.language_code == 'ru':
                if message.text == 'Моя тг информация' or message.text == 'Моя информация от телеграмма' or message.text == 'моя информация от телеграмма' or message.text == 'моя тг информация':
                    bot.send_message(message.chat.id,f'<em><b>Ваша информация: </b></em>{message}',parse_mode='html')
                elif message.text == 'старт' or message.text == '/start':
                    bot.send_message(message.chat.id,'<em><b>Я был запущен.</b></em>',parse_mode='html')
                    bot.send_message(message.chat.id,'<em><b>Чтоб увидить больше напишите: </b></em>Помогите или помогите или /help.',parse_mode='html')
                elif message.text == 'Привет' or message.text == 'привет':
                    bot.reply_to(message,f'<em><b>Привет: {message.from_user.first_name} {message.from_user.last_name}.</b></em>',parse_mode='html')
                elif message.text == 'Помогите' or message.text == 'помогите' or message.text == '/help':
                    bot.send_message(message.chat.id,'<em><b>Все команды:</b></em>',parse_mode='html')
                    bot.send_message(message.chat.id,'Моя тг информация или Моя информация от телеграмма или моя тг информация или моя информация от телеграмма. (выводит вашу информацию)')
                    bot.send_message(message.chat.id,'старт или /start. (выводит стартовое сообщение)')
                    bot.send_message(message.chat.id,'Привет или привет. (Привет)')
                    bot.send_message(message.chat.id,'Помогите или помогите или /help. (Помгает тебе)')
                    bot.send_message(message.chat.id,'Спасибо или спасибо. (Пожалуйста)')
                    bot.send_message(message.chat.id,'Как тебя зовут или как тебя зовут. (Муня зовут?)')
                    bot.send_message(message.chat.id,'Как дела или как дела. ( :) )')
                    bot.send_message(message.chat.id,'Бот или бот. (???)')
                    bot.send_message(message.chat.id,'Пока или пока. (Поко, ой)')
                    bot.send_message(message.chat.id,'Не матерись или :] . (!!!)')
                elif(message.text == '838838'):
                    bot.send_message(message.chat.id,'<em><b>Привет Костя, первый тестер.Ты крутой.</b></em>',parse_mode='html')
                elif(message.text == 'Спасибо' or message.text == 'спасибо'):
                    bot.send_message(message.chat.id,f'<em><b>Пожалуйста, {message.from_user.first_name} {message.from_user.last_name}.</b></em>',parse_mode='html')
                elif(message.text == 'Мут на десять секунд' or message.text == 'Мут на 10 секунд'):
                    i = 1
                    while True:
                        time.sleep(1)
                        bot.send_message(message.chat.id,f'<em><b>{i}</b></em>',parse_mode='html')
                        i += 1
                        if i > 10:
                            break
                elif(message.text == 'Как тебя зовут' or message.text == 'как тебя зовут'):
                    bot.send_message(message.chat.id,f'<em><b>Меня зовут Mini coder.</b></em>',parse_mode='html')
                elif(message.text == 'Как дела' or message.text == 'как дела'):
                    bot.send_message(message.chat.id,f'<em><b>Я бот у меня нет дел.</b></em>',parse_mode='html')
                elif(message.text == 'бот' or message.text == 'Бот'):
                    bot.send_message(message.chat.id,f'<em><b>Что вам нужно?</b></em>',parse_mode='html')
                elif message.text == 'пока' or message.text == 'Пока':
                    bot.send_message(message.chat.id,'<em><b>К сожелению я не понимаю контекст "Пока".</b></em>',parse_mode='html')
                    bot.send_message(message.chat.id,f'<em><b>Пока {message.from_user.first_name} {message.from_user.last_name}.</b></em>',parse_mode='html')
                elif(message.text == 'Хуй' or message.text == 'хуй' or message.text == 'Ебать' or message.text == 'ебать' or message.text == 'Блять' or message.text == 'блять'):
                    #Я ненавижу маты поэтому проверка на их наличие
                    print('пользователь ввел мат')
                    bot.send_message(message.chat.id,f'<em><b>Пожалуйста НЕ МАТЕРИТЕСЬ!!! Вы меня поняли {message.from_user.first_name} {message.from_user.last_name}.</b></em>',parse_mode='html')
                    if message.text == 'Хуй' or message.text == 'хуй':
                        bot.send_message(message.chat.id,f'<em><b>Пожалуйста не пишите слово х*й.</b></em>',parse_mode='html')
                    if message.text == 'Ебать' or message.text == 'ебать':
                        bot.send_message(message.chat.id,f'<em><b>Пожалуйста не пишите слово е#*ть.</b></em>',parse_mode='html')
                    if message.text == 'Блять' or message.text == 'блять':
                        bot.send_message(message.chat.id,f'<em><b>Пожалуйста не пишите слово е#*ть.</b></em>',parse_mode='html')

                else:
                    print(f'Русский, {message.text}')
                    bot.send_message(message.chat.id,'<em><b>Я не понимаю эту команду.</b></em>',parse_mode='html')
            else:
                if message.text == 'My tg info' or message.text == 'My telegram info' or message.text == 'my telegram info' or message.text == 'my tg info':
                    bot.send_message(message.chat.id,f'<em><b>You telegram info: </b></em>{message}',parse_mode='html')
                elif message.text == 'start' or message.text == '/start':
                    bot.send_message(message.chat.id,'<em><b>I am was start.</b></em>',parse_mode='html')
                    bot.send_message(message.chat.id,'<em><b>to see more write: </b></em>Help or help or /help.',parse_mode='html')
                elif message.text == 'Hello' or message.text == 'hello':
                    bot.reply_to(message,f'<em><b>Hello: {message.from_user.first_name} {message.from_user.last_name}.</b></em>',parse_mode='html')
                elif message.text == 'Help' or message.text == 'help' or message.text == '/help':
                    bot.send_message(message.chat.id,'<em><b>All comands:</b></em>',parse_mode='html')
                    bot.send_message(message.chat.id,'My tg info or My telegram info or or my tg info my telegram info. (print your info)')
                    bot.send_message(message.chat.id,'start or /start. (print start message)')
                    bot.send_message(message.chat.id,'Hello or hello. (Hello)')
                    bot.send_message(message.chat.id,'Help or help or /help. (Help you)')
                    bot.send_message(message.chat.id,'Thankyou or thankyou. (thankyou too)')
                    bot.send_message(message.chat.id,'What your name or what your name. (My name?)')
                    bot.send_message(message.chat.id,'How are you or how are you. ( :) )')
                    bot.send_message(message.chat.id,'Bot or bot. (???)')
                    bot.send_message(message.chat.id,'Goodbye or goodbye. (Goodbye)')
                elif(message.text == '838838'):
                    bot.send_message(message.chat.id,'<em><b>Hello Kostya, first tester.You realy cool.</b></em>',parse_mode='html')
                elif(message.text == 'Thankyou' or 'thankyou'):
                    bot.send_message(message.chat.id,f'<em><b>Thankyou {message.from_user.first_name} {message.from_user.last_name} too.</b></em>',parse_mode='html')
                elif(message.text == 'What your name' or message.text == 'what your name'):
                    bot.send_message(message.chat.id,f'<em><b>My name is Mini coder.</b></em>',parse_mode='html')
                elif(message.text == 'How are you' or message.text == 'How are you'):
                    bot.send_message(message.chat.id,f'<em><b>I am very good because I am bot.</b></em>',parse_mode='html')
                elif(message.text == 'bot' or message.text == 'Bot'):
                    bot.send_message(message.chat.id,f'<em><b>What do you need?</b></em>',parse_mode='html')
                elif message.text == 'goodbye' or message.text == 'Goodbye':
                    bot.send_message(message.chat.id,f'<em><b>Goodbye {message.from_user.first_name} {message.from_user.last_name}.</b></em>',parse_mode='html')
                else:
                    print(f'English, {message.text}')
                    bot.send_message(message.chat.id,'<em><b>I am don`t registry this command</b></em>',parse_mode='html')
        bot.polling(none_stop=True)
    except :
        print('!!! ??? Error Ошибка!?')
        
        continue