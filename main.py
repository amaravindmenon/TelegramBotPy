import telebot

API_KEY = "Your Key";


bot = telebot.TeleBot(API_KEY);

@bot.message_handler(func=lambda msg: msg.from_user)
def send_hello_message(msg):
    text1 = msg.json["text"]
    if msg.json["text"].startswith('/data'):
        text = text1.replace("/data ","")
        with open('metadata/data/data1.txt', 'r', encoding = "utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.lower()
                if text in line:
                    bot.reply_to(msg,line)
                    print(line)
    else:
        bot.reply_to(msg, "currently we dont have this data")

bot.polling()    
