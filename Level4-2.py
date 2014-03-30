import urllib
import re

link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = 16044 / 2

url = urllib.urlopen(link + str(num))
i = 0

while (i < 400):
    text = url.readlines()
    print text
    found = text[0].find('next nothing is ')
    if found > 0:
        num = int(text[0][found+16:])
        print num
        url = urllib.urlopen(link + str(num))
        i = i + 1
    else:
        break