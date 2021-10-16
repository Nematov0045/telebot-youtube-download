import telebot
from pytube import YouTube
import os
import datetime
# url=input('input url:')
# # YouTube(url).streams.first().download()
# video=YouTube(url)
# video.streams()
curent_path=os.path.abspath(os.getcwd())
token='2021613444:AAE51B9mycU1-4ryWVfF_bqi6qRSwbg26Ss'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start','старт'])
def start_message(message):
    username=message.from_user.first_name
    mess = 'привет' + username + 'просто отправь мне сылку на видео из youtube'
    bot.send_message(message.chat.id,mess)

@bot.message_handler(content_types='text')
def downloader(message):
    url_from_youtube=message.text
    down_path=curent_path+'/videos/'
    filename=str(datetime.datetime.now())
    yout=YouTube(url_from_youtube)
    bot.send_message(message.chat.id,'пожалуйста подождите \n ваше видео в пути')
    YouTube(url_from_youtube).streams.filter(res="720").first().download(filename=filename,output_path=down_path)
    path_url=down_path + filename
    vid = open(path_url,'rb')
    bot.send_video(message.chat.id, vid)
print('bot is working')
bot.infinity_polling() 