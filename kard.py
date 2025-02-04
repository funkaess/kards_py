import telebot
from telebot import types
import random
import time
from datetime import datetime, timedelta


ids = {}
id = 0

times1 = datetime(2025,1,1)
times = datetime(2025,1,1)

bot = telebot.TeleBot('7061508426:AAE1xgjp9bWchtIoIC3Q3vaoTAbR5-y3wKU')
@bot.message_handler(commands = ['start'])
def start(message):
    global id
    global ids
    id = message.from_user.id
    if str(id) not in ids:
        ids[str(id)] = 0 
    bot.send_message(message.chat.id, f"привет, {message.from_user.username}, ваши очки: {ids[str(id)]}", parse_mode = "html")

   
print(1)


@bot.message_handler(commands = ['points'])
def points(message):
    global ids
    global id
    bot.send_message(message.chat.id, ids[str(id)], parse_mode = "html")

rare = 1000
epic = 2000
myth = 5000
leg = 10000


@bot.message_handler(content_types = ['text'])
def get_user_text(message):
    global ids
    global id
    global rare
    global epic
    global myth
    global leg
    global times
    global times1
    global times2
    if message.text == 'торнадо':
        a = 'камару.jpg' 
        b = 'funkes.jpg' 
        c = 'ceresit.jpg' 
        d = 'vasago.jpg' 
        e = 'angry.jpg' 
        f = 'hew tornadko.jpg' 
        g = 'ghost drako.jpg' 
        h = 'chister.jpg' 
        i = 'tornadko.jpg' 
        j = 'drako.jpg'
        k = 'angelo.jpg'
        l = 'fire.jpg'
        m = 'fizhma.jpg'
        n = 'megabox.jpg'
        o = 'mks.jpg'
        p = 'openthedoor.jpg'
        q = 'paralilipid.jpg'
        r = 'sirniki.jpg'
        s = 'sirnikiprice.jpg'
        clovar = {a:f"камару \nредкость: редкий",
                  b:f"фанкис \nредкость: эпик",
                  c:f"церезит \nредкость: эпик",  
                  d:f"вассаго \nредкость: редкий", 
                  e:f"злои рома \nредкость: эпик",
                  f:f"новогодний торнадо \nредкость: легендарный",
                  g:f"призрачный всадник драко \nредкость: легендарный",
                  h:f"чистер \nредкость: редкий",
                  i:f"торнадо \nредкость: мифик",
                  j:f"новогодний драко \nредкость: мифик",
                  k:f"виноградни сок \nредкость:редкий",
                  l:f"спайк с огонечком \n редкость:редкий",
                  m:f"фiжма \nредкость:легендарный",
                  n:f"пикми мега ящик \nредкость:мифик",
                  o:f"мочковатая корневая система \nредкость:эпик",
                  p:f"легенд танос \nредкость:эпик",
                  q:f"паралiлiпiд \nредкость:мифик",
                  r:f"сырники \nредкость:легендарный",
                  s:f"грей, неплачь \nредкость:мифик"}
        times = datetime.now()
        choise = random.choice([a, d, h, k, l, a, d, h, k, l, a, d, h, k, l,a, d, h, k, l, a, d, h, k, l, a, d, h, k, l, a, d, h, k, l,a, d, h, k, l, a, d, h, k, l, a, d, h, k, l,a, d, h, k, l, a, d, h, k, l, a, d, h, k, l, a, d, h, k, l, b, c, o, e, p, b, c, o, e, p, b, c, o, e, p, b, c, o, e, p, b, c, o, e, p, b, c, o, e, p, i, j, n, q, s, i, j, n, q, s, i, j, n, q, s, i, j, n, q, s, i, j, n, q, s, f, g, r, m, f, g, r, m, f, g, r, m, f, g, r, m, f, g, r, m])
        photo = open(choise,'rb')
        times2 = times - times1
        if id != 0:
            if times2 > timedelta(seconds = 1):
                if choise == a or choise == d or choise == h or choise == k or choise == l:
                    ids[str(id)] = ids.get(str(id)) + rare         
                elif choise == b or choise == c or choise == e or choise == o or choise == p:
                    ids[str(id)] = ids.get(str(id)) + epic
                elif choise == i or choise == j or choise == n or choise == q or choise == s:
                    ids[str(id)] = ids.get(str(id)) + myth
                elif choise == f or choise == g or choise == m or choise == r:
                    ids[str(id)] = ids.get(str(id)) + leg
                bot.send_photo(message.chat.id, photo, caption = f"{clovar[choise]}\n ваши очки: {ids[str(id)]}")
                times1 = datetime.now()
            
            
        else:
            bot.send_message(message.chat.id, 'Сначала нажмите комманду /start!', parse_mode = "html")

        
           
            



        


        











bot.polling(none_stop = True)