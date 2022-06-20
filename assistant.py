import os
import playsound
from playsound import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch


wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()

def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound("sound.mp3", False)
    #os.remove("/home/monsieurkang/PycharmProjects/SpeechProcessing/sound.wav")


#speak("abbc")



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return 0
#get_audio()

def stop():
    speak("Hẹn gặp lại bạn sau!")
#stop()



def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Tôi không nghe rõ. Bạn nói lại được không!")
    time.sleep(10)
    stop()
    return 0




def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Chiều nay bạn có dự định gì không ?".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))
    time.sleep(5)
#hello("quang")

def introduce():
    speak("Tôi là trợ lý ảo của bạn. Bạn có thể gọi tôi là chị google phiên bản shopee cũng được.")
    time.sleep(10)

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")

#get_time("ngày")

# phai sua lai link
def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        #
        #os.staWindowrtfile(
            #'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        #Linux
        os.system('/usr/share/man/man1/google-chrome.1.gz')

    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile(
            'C:\Program Files\Microsoft Office\\root\Office16\\WINWORD.EXE')
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile(
            'C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE')
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")

#open_application('google')


def open_website(text):
    reg_ex = re.search('tìm kiếm (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False
#open_website("mở Doulingo")

# def open_google_and_search(text):
#     search_for = text.split("kiếm", 1)[1]
#     speak('Okay!')
#     driver = webdriver.Chrome(path)
#     driver.get("https://www.google.com")
#     que = driver.find_element_by_xpath("//input[@name='q']")
#     que.send_keys(str(search_for))
#     que.send_keys(Keys.RETURN)
# open_google_and_search("doulingo")

def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.")

#play_song()


def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        text = get_text()
        speak('Sau đây là kết quả nổi bật')
        contents = wikipedia.summary(text).split('\n')
        print(contents[0])
        # speak(contents[0])
        time.sleep(2)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = get_text()
            if "có" not in ans:
                break
            #speak(content)
            print(content)
            time.sleep(2)


    except:
        speak("Tôi không định nghĩa được thuật ngữ của bạn. Nhắc lại giùm tôi nhé")
        time.sleep(2)

#tell_me_about()

def help_me():
    speak("""Tôi có thể giúp bạn thực hiện một số yêu cầu sau đây:
    1. Giới thiệu bản thân
    2. Hiển thị thời gian   
    3. Mở ứng dụng trên máy tính    
    4. Tìm kiếm trên Google
    5. Phát nhạc
    6. Tra cứu thuật ngữ """)
    time.sleep(20)

#help_me()

def thank_you():
    speak("Không có gì đâu mà, hi hi")
    time.sleep(5)


def assistant():
    name = "Thắng"

    if name:
        hello(name)
        while True:
            text = get_text()
            if not text:
                break
            elif "dừng lại" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                stop()
                break
            elif "có thể làm gì" in text:
                help_me()

            elif "chào trợ lý ảo" in text:
                hello(name)
            elif "mấy giờ" in text or "ngày" in text:
                get_time(text)
            elif "tìm kiếm" in text:
                open_website(text)
            elif "thank you" in text or "cảm ơn" in text:
                thank_you()
            elif "nghe nhạc" in text or "chơi nhạc" in text:
                play_song()
            elif "định nghĩa" in text:
                tell_me_about()
            elif "bạn là ai" in text or "giới thiệu về bạn" in text:
                introduce()
            else:
                speak("Bạn cần tôi giúp gì nào?")


assistant()