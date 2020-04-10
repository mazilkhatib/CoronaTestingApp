from flask import Flask, request
from counter1 import count
import telegram
from telebot.credentials import bot_token, bot_user_name,URL
from bs4 import BeautifulSoup
import requests

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    global count
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)


    if text == '/start':
        bot.sendMessage(chat_id=chat_id, text='Welcome to the system !! now type some commands..', reply_to_message_id=msg_id)
    elif text == 'test':
        count = 0
        bot.sendMessage(chat_id=chat_id, text='To test the chances please respond to the commands according to the symptoms present\n\n1.Fever(f)\n\n2.Cough(c)\n\n3.Shortness of breath(b)\n\n4.Pain or pressure in chest(p)\n\n5.Confusion or inability to wakeup(cc)\n\n6.Trouble Breathing(bb)\n\n7.Bluish lips or face.(bbb)\n\nNote: Please follow above commands step by step as per symptoms', reply_to_message_id=msg_id)
    elif text == 'f':
        count = count + 14.2
        bot.sendMessage(chat_id=chat_id, text='The chances increased by 14.285% \n\n Total = '+str(count)+'%', reply_to_message_id=msg_id)
    elif text == 'c':
        count = count + 14.2
        bot.sendMessage(chat_id=chat_id, text='The chances increased by 14.285% \n\n Total = '+str(count)+'%', reply_to_message_id=msg_id)
    elif text == 'b':
        count = count + 14.2
        bot.sendMessage(chat_id=chat_id, text='The chances increased by 14.285% \n\n Total = '+str(count)+'%', reply_to_message_id=msg_id)
    elif text == 'p':
        count = count + 14.2
        bot.sendMessage(chat_id=chat_id, text='The chances increased by 14.285% \n\n Total = '+str(count)+'%', reply_to_message_id=msg_id)
    elif text == 'cc':
        bot.sendMessage(chat_id=chat_id, text='The chances increased by 14.285% \n\n Total = '+str(count)+'%', reply_to_message_id=msg_id)
    elif text == 'bb':
        count = count + 14.2
        bot.sendMessage(chat_id=chat_id, text='The chances increased by 14.285% \n\n Total = '+str(count)+'%', reply_to_message_id=msg_id)
    elif text == 'bbb':
        count = count + 14.2
        bot.sendMessage(chat_id=chat_id, text='The chances increased by 14.285% \n\n Total = '+str(count)+'%', reply_to_message_id=msg_id)
    elif text == 'cases':
        url = "www.worldometers.info/coronavirus/"
        r  = requests.get("http://" +url)
        data = r.text
        soup = BeautifulSoup(data,features="lxml")
        arr=[]
        for link in soup.find_all('div',class_="maincounter-number"):
            arr.append(link.text)
        bot.sendMessage(chat_id=chat_id, text='Total Cases: {}'.format(arr[0]), reply_to_message_id=msg_id)

    elif text == 'Cases':
        url = "www.worldometers.info/coronavirus/"
        r  = requests.get("http://" +url)
        data = r.text
        soup = BeautifulSoup(data,features="lxml")
        arr=[]
        for link in soup.find_all('div',class_="maincounter-number"):
            arr.append(link.text)
        bot.sendMessage(chat_id=chat_id, text='Total Cases: {}'.format(arr[0]), reply_to_message_id=msg_id)

    elif text == 'deaths':
        url = "www.worldometers.info/coronavirus/"
        r  = requests.get("http://" +url)
        data = r.text
        soup = BeautifulSoup(data,features="lxml")
        arr=[]
        for link in soup.find_all('div',class_="maincounter-number"):
            arr.append(link.text)
        bot.sendMessage(chat_id=chat_id, text='Total Deaths: {}'.format(arr[1]), reply_to_message_id=msg_id)

    elif text == 'Deaths':
        url = "www.worldometers.info/coronavirus/"
        r  = requests.get("http://" +url)
        data = r.text
        soup = BeautifulSoup(data,features="lxml")
        arr=[]
        for link in soup.find_all('div',class_="maincounter-number"):
            arr.append(link.text)
        bot.sendMessage(chat_id=chat_id, text='Total Deaths: {}'.format(arr[1]), reply_to_message_id=msg_id)

    elif text == 'recover':
        url = "www.worldometers.info/coronavirus/"
        r  = requests.get("http://" +url)
        data = r.text
        soup = BeautifulSoup(data,features="lxml")
        arr=[]
        for link in soup.find_all('div',class_="maincounter-number"):
            arr.append(link.text)
        bot.sendMessage(chat_id=chat_id, text='Total Recovered: {}'.format(arr[2]), reply_to_message_id=msg_id)

    elif text == 'Recover':
        url = "www.worldometers.info/coronavirus/"
        r  = requests.get("http://" +url)
        data = r.text
        soup = BeautifulSoup(data,features="lxml")
        arr=[]
        for link in soup.find_all('div',class_="maincounter-number"):
            arr.append(link.text)
        bot.sendMessage(chat_id=chat_id, text='Total Recovered: {}'.format(arr[2]), reply_to_message_id=msg_id)

    elif text=='news':
        main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
        open_bbc_page = requests.get(main_url).json()
        article = open_bbc_page["articles"]
        results = ''
        for ar in article:
            results=results+ar["title"]+'\n\n'
        bot.sendMessage(chat_id,'News:\n{}'.format(results))

    elif text=='News':
        main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
        open_bbc_page = requests.get(main_url).json()
        article = open_bbc_page["articles"]
        results = ''
        for ar in article:
            results=results+ar["title"]+'\n\n'
        bot.sendMessage(chat_id,'News:\n{}'.format(results))

    elif text == 'pre':
        bot.sendMessage(chat_id,"1.Regular hand washing. \n 2. Covering mouth and nose when coughing and sneezing \n 3. If you are taking care of someone who is sick, try to stay 6 feet away – this is the distance virus-containing droplets can travel through a sneeze or cough \n 4. Avoid close contact with anyone showing symptoms of respiratory illness such as coughing and sneezing. \n 5. Avoid touching your eyes, nose, and mouth \n 6. Clean and disinfect frequently touched objects and surfaces using a regular household cleaning spray or wipe.")
        bot.sendPhoto(chat_id, open("un.png", 'rb'))
        bot.sendPhoto(chat_id, open("pre.png", 'rb'))
    elif text=='Pre':
        bot.sendMessage(chat_id,"1.Regular hand washing. \n 2. Covering mouth and nose when coughing and sneezing \n 3. If you are taking care of someone who is sick, try to stay 6 feet away – this is the distance virus-containing droplets can travel through a sneeze or cough \n 4. Avoid close contact with anyone showing symptoms of respiratory illness such as coughing and sneezing. \n 5. Avoid touching your eyes, nose, and mouth \n 6. Clean and disinfect frequently touched objects and surfaces using a regular household cleaning spray or wipe.")
        bot.sendPhoto(chat_id, open("un.png", 'rb'))
        bot.sendPhoto(chat_id, open("pre.png", 'rb'))
    elif text=='sym':
        bot.sendMessage(chat_id, "Reported illnesses have ranged from mild symptoms to severe illness and death for confirmed coronavirus disease 2019 (COVID-19) cases.These symptoms may appear 2-14 days after exposure (based on the incubation period of MERS-CoV viruses).\n1.Fever\n2.Cough\n3.Shortness of breath\n4.Trouble breathing\n5.Persistent pain or pressure in the chest\n6.New confusion or inability to arouse\n7.Bluish lips or face")
        bot.sendPhoto(chat_id, open("sy.png", 'rb'))
    elif text=='Sym':
        bot.sendMessage(chat_id, "Reported illnesses have ranged from mild symptoms to severe illness and death for confirmed coronavirus disease 2019 (COVID-19) cases.These symptoms may appear 2-14 days after exposure (based on the incubation period of MERS-CoV viruses).\n1.Fever\n2.Cough\n3.Shortness of breath\n4.Trouble breathing\n5.Persistent pain or pressure in the chest\n6.New confusion or inability to arouse\n7.Bluish lips or face")
        bot.sendPhoto(chat_id, open("sy.png", 'rb'))
    elif text=='top':
        bot.sendPhoto(chat_id, open("covid-1.png", 'rb'))
    elif text=='Top':
        bot.sendPhoto(chat_id, open("covid-1.png", 'rb'))
    elif text=='op':
        bot.sendPhoto(chat_id, open("covid-1.png", 'rb'))
    elif text=='Op':
        bot.sendPhoto(chat_id, open("covid-1.png", 'rb'))
    else:
        bot.sendMessage(chat_id=chat_id, text='Enter a valid command', reply_to_message_id=msg_id)


    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
