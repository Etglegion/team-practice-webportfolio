import telebot

b = telebot.TeleBot("8723840481:AAHYintRJ9P52qls7PuIzX6CVM0M3Sxectw")
s = {}

@b.message_handler(content_types=['text'])
def u(m):
    try:
        c = m.chat.id
        x = m.text

        if x == "/start" or x == "Привет!":
            k = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            k.add(telebot.types.KeyboardButton("Оставить заявку"), telebot.types.KeyboardButton("Команда"),telebot.types.KeyboardButton("Привет!"))
            b.send_message(c, 'Добро пожаловать! Это telegram-бот проекта "Так Сяк".', reply_markup=k)
            return

        if x == "Команда":
            b.send_message(c, "Портфолио команды из 5 человек.")
            return

        if x == "Оставить заявку":
            s[c] = True
            b.send_message(c, "ТЗ:")
            return

        if s.get(c):
            s[c] = False
            b.send_message(c, "Заявка принята.")
            print(x)
            return
            
        b.send_message(c, "Выберите из меню.")
        
    except Exception as e:
        print(e)

while True:
    try:
        b.polling(none_stop=True)
    except Exception as e:
        print(e)
