
# count = 0;
# print("initial count is ", count)

# sum = 0;
# print("initial sum is ", sum)


# for i in [3, 41, 12, 9, 74, 15]:
#     count += 1;
#     print("Final count", count)

#     sum = sum + i;
#     print("Final sum", sum)

#     avg = sum / count
    

# print("Average is ", avg)

# print("begin")

# for elem in [3, 41, 12, 9, 74, 15]:
#     if elem > 20:
#         print("Larger than 20 ", elem)

# print('Done')

# smallest = None

# for elem in [3, 41, 12, 9, 74, 15]:

#     if smallest is None:
#         smallest = elem
#     elif elem < smallest:
#         smallest = elem
#         print("smallest value is ", smallest)

# print("finally the smallest is ", smallest)


# gun = "dick"

# print("the maximum alphabet in the string is ", max(gun))

# gun = "dick"

# print("the minimum alphabet in the string is ", min(gun))

# new = "Bob"
# print(new.lower())

# new = "Bob"
# print(new.upper())

# fun = "banaana"

# print(fun.find("na"))

# fun = "bana" 

# new_fun = fun.replace('ana', 'y')

# print(new_fun)

# # get rid of whitespace
# fun = " danny "
# print(fun.lstrip())
# print(fun.rstrip())
# print(fun.strip())

# fun = "banaana"

# print(fun.startswith('b'))
# print(fun.startswith('d'))



# email = 'christopher.owusu@st.gimpa.edu.gh som' 

# find_st = email.find('st.')
# print("found st. at ", find_st)

# next_dot = email.find(' ', find_st)
# print("next dot after st. is at ", next_dot)

# school_name = email[find_st+3 : next_dot]
# print("school name is ", school_name)

# #reading files
# fhand = open('new.txt')

# for elems in fhand:
#     print(elems)

# #counting lines in a file
# fhand = open('new.txt')

# count = 0

# for line in fhand:
#     count += 1
#     print(line)
#     print(count)



# fhand = open('new.txt')

# read_file = fhand.read()

# print(len(read_file))   


# get_file_name = input("Enter file name: ")

# try:
#     num = open(get_file_name)
# except:
#     print("there is no file called " , get_file_name)
#     quit()


# for elem in get_file_name:
#     print(elem)

# # making list

# stuff = list()

# stuff.append('book')
# stuff.append('pen')
# stuff.append('eraser')

# print(stuff)

# if not 'book' in stuff:
#     print("Yes")

# stuff.sort()
# print(stuff)

# # Using split() keyword
# fun = "Here We Go Again"

# print(fun.split())

# fun = "Here:We:Go:Again"

# print(fun.split(':'))

# email = 'christopher.owusu@st.gimpa.edu.gh'

# spi = email.split('.')

# print(spi[2])


# # Using dictionaries
# num = dict()    # or you can use {} to define a dictionary

# num['nam'] = 2
# num['am'] = 8
# num['naml'] = 4
# num['namk'] = 6

# print(num)

# num['am'] = 89
# print(num)

# num['bam'] = 23
# print(num)

# new = ["a", "b", "c", "a", "b", "c", "d"]
# count = {}

# for elem in new:
#     count[elem] = count.get(elem, 0) + 1
# print(count)


# # Tuple
# c = {'a': 1, 'b':2, 'c':3, 'd':4}

# text = open('new.txt')
# count = {}

# for lines in text:
#     words = lines.split()
#     for word in words:
#         count[words] = count.get(word, 0) + 1

# print( sorted( [ (v,k) for k,v in c.items() ] ) )


# # Regular Expression

# import re

# text = 'my 2 namw 4 is 5 onona 6 jnsnc 9 jnna0'
# y = re.findall('[0-9]+', text)

# print(y)


# # Socket

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect('something.com', 80)

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
# mysock.close()


# #ASCII 

# print(ord('H'))

# # Using urllib

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# for hand in fhand:
#     print(hand.decode().strip())

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = {}

# for line in fhand:
#     words = line.decode().split('\n')
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
        
# print(counts)

# # Web Scraping

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# get_link = input('Enter url: ')

# html = urllib.request.urlopen(get_link).read()
# soup = BeautifulSoup(html, 'html.parser')

# #retrive all anchor tags
# tags = soup('a')

# for tag in tags:
#     print(tag.get('href', None))

# # XML Schema

# import xml.etree.ElementTree as ET

# data = '''
#     <person>
#     <name> Chuck Noris </name>
#     <phone type="intl"> +233 244 1713 55 </phone>
#     <email hide="yes" />
#      </person>
# '''
# tree = ET.fromstring(data)

# print("Name: ", tree.find('name').text)
# print("Attr: ", tree.find('email').get('hide'))


# data = '''
# <begin>
#     <users>
#         <user x="2">
#             <id> 01 </id>
#             <name> Chuck Dicks </name>
#          </user>
#          <user x="7">
#             <id> 02 </id>
#             <name> Chuck Bicks </name>
#          </user>
#          <user x="9">
#             <id> 03 </id>
#             <name> Chuck Chicks </name>
#          </user>
#      </users>
#  </begin>
# '''

# trees = ET.fromstring(data)
# new = trees.findall('users/user')
# print("no of elements in the string: ", len(new))
# for elem in new:
#     print("name: ", elem.find('name').text)
#     print("id: ", elem.find('id').text)
#     print("user no: ", elem.get('x'))


# #JSON
# import json

# data = '''
#     [
#         {'name' : "chuck noris",
#         'id': "1",
#         'x' : "007"},
#         {'name' : "chuck norty",
#         'id': "2",
#         'x' : "003"},
#         {'name' : "Buck noris",
#         'id': "3",
#         'x' : "005"}
#     ]

# '''

# tree = json.loads(data)

# print("lenght: ", len(tree))

# for elem in tree:
#     print("name:", elem['name'])


# # Classes

# class newClass:
#     x = 0
    
#     def new(self):
#         self.x += 1
#         print("So far: ", self.x)

# bun = newClass()
# bun.new()
# bun.new()
# bun.new()

# y = 'Hello World'

# print(dir(y))

# # Object Lifecycle

# class PartyAnimal:
#     x = 0
#     name = ''

#     def __init__(self, nam):
#         self.name = nam
#         print(self.name,'constructed')
#     def party(self):
#         self.x = self.x + 1
#         print(self.name,'party count',self.x)

# q = PartyAnimal('Quincy')
# m = PartyAnimal('Miya')

# q.party()
# m.party()
# q.party()
# m.party()

# # Objects: Inheritance

# class PartyAnimal:
#     x = 0
#     name = ''

#     def __init__(self, nam):
#         self.name = nam
#         print(self.name,'constructed')
#     def party(self):
#         self.x = self.x + 1
#         print(self.name,'party count',self.x)

# class Solution(PartyAnimal):
#     points = 0
    
#     def touchdown(self):
#         self.points += 7
#         self.party()
#         print(self.name, "points", self.points)


# q = PartyAnimal('Quincy')
# m = Solution('Miya')

# q.party()
# m.party()
# m.touchdown()