#! /bin/env python3


from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://v.qq.com/')
bs = BeautifulSoup(html.read(), 'html.parser')
#bs = BeautifulSoup(html.read(), 'lxml')
#bs = BeautifulSoup(html.read(), 'html5lib')

print("bs.head: ")
print(bs.head)

print()
print("bs.meta: ")
print(bs.meta)

print()
print("bs.head.meta: ")
print(bs.head.meta)

print()
print("bs.html.head.meta: ")
print(bs.html.head.meta)

print()
print("bs.html.meta: ")
print(bs.html.meta)
