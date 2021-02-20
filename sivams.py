# if elif statement

age = 25
if age < 20:
    print("welcome to our site")
elif age > 20:
    print("sorry you are not applicable")
else:
    print("you are perfect")

# for loop

foods = ['burger', 'pizza', 'sweets', 'rasgulla', 'rice']

for f in foods:
    print(f)
    print(len(f))

# Range and while

for x in range(10, 40, 2):
    print(x)

buttcrack = 5
while buttcrack < 10:
    print(buttcrack)
    buttcrack += 1

# comment & Break

magicNumber = 23
for n in range(101):
    if n is magicNumber:
        print(n, "is the magic Number")
        break
    else:
        print(n)

# Continue

numberTaken = [2, 5, 7, 15, 18]
print("here is the no. that are still available")

for n in range(1, 20):
    if n in numberTaken:
        continue
    print(n)


# function

# defining a function

def bitcoin_to_usd(btc):
    usd = btc * 527
    print(usd)


# calling a function

bitcoin_to_usd(4.3)


# return values

def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 8
    return girls_age


suraj_limit = allowed_dating_age(20)
print("Suraj is dating a girl", suraj_limit, "or older")


# default values of argument

def get_gender(sex='unknown'):
    if sex is 'm':
        sex = "male"
    elif sex is 'f':
        sex = "female"
    print(sex)


get_gender('m')
get_gender('f')
get_gender()

# variable scope

a = 25  # this is global variable


def core():
    b = 45  # this is local variable
    print(a)


def mass():
    print(a)


core()
mass()


# Keyword argument

def dumb_sentence(name="suraj", action="ate", item="sugar"):
    print(name, action, item)


dumb_sentence()
dumb_sentence(item="silently")
dumb_sentence("muskan", " is", " tatti")


# flexiable no. of argument

def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)


add_numbers(3, 5)
add_numbers(3, 45, 644, 6444, 6655255, 87564)


# Unpacking arguments

def health_calculator(age, apples_ate, cigrate_smoked):
    answer = (100 + age) + (apples_ate * 3.5) - (cigrate_smoked * 2)
    print(answer)


suraj_data = [20, 50, 2]
health_calculator(*suraj_data)

#sets

grocery={'rice','oil','milk','honey','beer','milk'}
print(grocery)

if 'milk' in grocery:
    print("you have already milk")
else:
    print("you need milk")


#Dictionary

classmates={'labham':' cool but smels','muskan':' clever but arogant','dishant':' sweet but good'}
print(classmates)
print(classmates['dishant'])

for k,v in classmates.items():
    print(k+v)

#module

import module

module.fish()

import random
x=random.randrange(1,1000)
print(x)

# Download image from web

import random
import urllib.request

def download_web_image(url):
    name=random.randrange(1,2000)
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://wallpaperaccess.com/full/533108.jpg")

# Writting a file

fw=open('sample.txt','w')
fw.write('Hello world ,i am suraj\n')
fw.write('i like to code whole night\n')
fw.close()

#reading a file

fr=open('sample.txt','r')
text=fr.read()
print(text)
fr.close()

#Downloading files from web

from urllib import request
goog_url='https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1562477544&period2=1594099944&interval=1d&events=history'

def download_stock_data(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n")
    dest_url=r'goog.csv'
    fx=open(dest_url,'w')
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_stock_data(goog_url)

#Building web crawler
'''
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url='https://www.amazon.in/s?k=books&page=2&qid=1594105222&ref=sr_pg_'+str(page)
        source_code = requests.get(url)
        plain_text=source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class':'a-link-normal a-text-normal'}):
            href="https://www.amazon.in"+link.get('href')
            title=link.string
            print(href)
            print(title)
        page+=1

    trade_spider(1)

#dynamic web crawling

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://buckysroom.org" + link.get('href')
        print(href)

trade_spider(3)'''

#You are the only exception

while True:
    try:
        number = int(input("What's your fav number hoss?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break
    finally:
        print("loop complete")

#classes and object

class Enemy:
    life = 3

    def attack(self):
        print("ouch!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()

# init


class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)


jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()

#class vs instance variable

class Girl:
    gender = 'female'

    def __init__(self, name):
        self.name = name


r = Girl('Rachel')
s = Girl('Stanky')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)

# inheritance

class Parent:

    def print_last_name(self):
        print('Roberts')


class Child(Parent):

    def print_first_name(self):
        print('Bucky')

    def print_last_name(self):
        print('Snitzleberg')


bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

#Multiple inheritance


class Mario():

    def move(self):
        print('I am moving!')


class Shroom():

    def eat_shroom(self):
        print('Now I am big!')


class BigMario(Mario, Shroom):
    pass


bm = BigMario()
bm.move()
bm.eat_shroom()

# Threading

import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = BuckysMessenger(name='Send out messages')
y = BuckysMessenger(name='Receive messages')
x.start()
y.start()

#Word frequency counter


import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class': 'index_singleListingTitles'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='"
        for i in range(0, len(symbols):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


start('https://buckysroom.org/tops.php?type=text&period=this-month')

# Unpack list or Tuples


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65, 76, 98, 54, 21])
drop_first_last([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])

#zip ....


first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)

for a, b in names:
    print(a, b)

# Lambda

answer = lambda x: x*7
print(answer(5))

# Min, Max and sorting dictionaries

stock={
'GOOG' : 520.25,
'APPL' : 50.25,
'YOTB' : 20.25,
'AMZN' : 530.25,
'WHO' : 320.25,
'FB' : 120.25,
}

print(min(zip(stock.values(),stock.keys()))) #giving min value

print(max(zip(stock.values(),stock.keys()))) #giving max value

print(sorted(zip(stock.values(),stock.keys()))) #giving sorted list

#pilow
from PIL import Image
img=Image.open("7.jpg")

print(img.size)

#cropping image

area=(100,120,356,456)

crop_image=(img.crop(area))
img.show()

#Combine image together

model=Image.open("8.jpg")
me=Image.open("1.jpg")

area=(100,100,350,350)

model.paste(me,area)

model.show()

# Getting individual channel

print(model.mode)

r,g,b=model.split()
r.show()
g.show()

#Awesome merge effect

model=Image.open("8.jpg")
r1,g1,b1=model.split()
r2,g2,b2=me.split()

new_image=Image.merge("RGB",(r1,g2,b1))
  new_image.show()

# Basic transformation

model=Image.open("8.jpg")

resize_model=model.resize((250,250))
resize_model.show()

flip_model=model.transpose(Image.FLIP_LEFT_RIGHT)
flip_model.show()

spin_model=model.transpose(Image.ROTATE_90)
spin_model.show()

# Modes and filter

#converting RGB mode To Black&white

black_white=model.convert("L")
black_white.show()


from PIL import ImageFilter

model=Image.open("8.jpg")

blur=model.filter(ImageFilter.BLUR)
blur.show()

detail=model.filter(ImageFilter.DETAIL)
detail.show()

edges=model.filter(ImageFilter.FIND_EDGES)
edges.show()

#Struct

from struct import *

#store as bytes data

packed_data=pack('iif',6,12,4.5)
print(packed_data)

print(calcsize("i")))
print(calcsize("iif")))

#To get bytes data back to normal form

original_data=unpack("iif",packed_data)
print(original_data)

# Map

income=[10,50,70]
def double_money(dollars)
 return dollars*2

new_income=list(map(double_money,income))
print(new_income)

#Bitwise operators

#-----Binary AND------

a=50  #110010
b=25  #011001
c=a&b #010000

print(c)

#-----Binary right sift-----

x=240  #11110000
y=x>>3 #00011110

print(y)

#Finding largest and smallest item

import heapq
stocks=[
    {'ticker': 'APPL', 'price': 240},
    {'ticker': 'FB', 'price': 24},
    {'ticker': 'GOOG', 'price': 640},
    {'ticker': 'HCL', 'price': 20},
    {'ticker': 'TCS', 'price': 40}
]

    print(heapq.nsmallest(2,stocks,key=lambda stocks:stocks['price']))

#Dictionary Calculator

stockes={
'GOOG' : 520.25,
'APPL' : 50.25,
'YOTB' : 20.25,
'AMZN' : 530.25,
'WHO' : 320.25,
'FB' : 120.25,
}

min_price=min(zip(stockes.values(),stockes.keys()))
print(min_price)

#Finding most frequent item

from collections import Counter

text="English is a West Germanic language that was first spoken in early medieval England"\ 
     "and eventually became a global lingua franca.[4][5] It is named after the Angles, one"\
    "of the ancient Germanic peoples that migrated to the area of Great Britain that later"\
    "took their name, England. Both names derive from Anglia, a peninsula on the Baltic"\
    "Sea. English is most closely related to Frisian and Low Saxon, while its vocabulary"\
    "has been significantly influenced by other Germanic languages, particularly Old Norse "\
    "(a North Germanic language), as well as Latin and French."

words=text.split()
counter=Counter(words)
top_three=counter.most_common(3)
print(top_three)

#Dictionary multiple key sort

from operator import itemgetter

stockers=[
    {'ticker': 'APPL', 'price': 240},
    {'ticker': 'FB', 'price': 24},
    {'ticker': 'GOOG', 'price': 640},
    {'ticker': 'HCL', 'price': 20},
    {'ticker': 'TCS', 'price': 40}
    ]

for x in sorted(stockers,key=itemgetter('ticker','price')):
    print(x)

#sorting custom object

from operator import attrgetter

class Users:
    def _init_(self,x,y):
      self.name=x
      self.user_id=y

    def _repr_(self):
      return self.name+": "+ str(self.user_id)

users=[
    user('bucky',25),
user('suraj',5),
user('rahul',45),
user('rohan',2),
user('moly',26)
]
for user in sorted(users,key=attrgetter('name')):
    print(user)

#-----------------------------------The  End ------------------------------------------
















