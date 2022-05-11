from turtle import *
import sh
import pyspeedtest
import pyfiglet
from time import sleep
import pyshorteners
from gtts import gTTS
import qrcode
import random
from pyfiglet import Figlet

pyfiglet.print_figlet('''Welcome to
nigga tools''')
def qr():
    n = 5
    while True:
        b = input('password:  ')
        if b == 'qrcode':
            print('OK')
            break
        n -=1
        if n > 0:
            print('left', n)
        else:
          print('uncorect')
          exit()
    data = input('link:  ')
    filename = input('name:  ')
    img = qrcode.make(data)
    img.save(filename)

def reading():
    file_to_read = input("the name of a file to read:\n") + '.txt'
    f = open(file_to_read, 'r')
    file_text = f.read()
    f.close()
    filename = input("name for MP3 file:\n")
    audio_created = gTTS(text=file_text, lang='ru')
    audio_created.save(filename)

def url():
    long_url = input("Enter the URL to shorten: ")
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    print("The Shortened URL is: " + short_url)

def creator():
    while True:
        file = (random.randint(1,99))

        sh.touch(str(file) + '.py')
        print(file)

def dead():
    ghoul = input('you are ghoul? 1 - yes.  2 - no')
    if ghoul == '2':
        print('idi nafik debil')
        exit()

    dead = 1000
    while dead>6:
        dead -=7
        sleep(0.03)
        print(dead)
    enigma = input()
    if enigma == '228':
        print('pashalka + 99999 social credit ')
    else:
        print('mudila')

def objem():
    d = int(input('zadaj objem'))
    x = 0
    while True:
        if d == x * x * x:
            print(x)
        x += 1


def virus():
    speed(20)
    color('red')
    bgcolor('black')
    b = 200
    while b > 0:
        left(b)
        forward(b + 3)
        b = b - 1


def speed():
    speed = pyspeedtest.SpeedTest()
    speed.download()
    speed.upload()
    speed.ping()


tool = input('choose tool what you need:\n1-qrcode generator\n2-file creator\n3-text to voice player\n4-url shotener\n5-1000-7\n6-virus\n7-objem\n8-internet-speed\n\n===> ')

if int(tool) == 1:
    qr()
elif int(tool) == 2:
    creator()
elif int(tool) == 3:
    reading()
elif int(tool) == 4:
    url()
elif int(tool) == 5:
    dead()
elif int(tool) == 6:
    virus()
elif int(tool) == 7:
    objem()
