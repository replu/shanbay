#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: replu<chenwang1515@gmail.com>
#         https://github.com/replu
# Created on 2015-03-26 15:00

from sys import argv
import re
import requests

wordListID = input("please input the wordlist ID: ")

linkFile = open("links.txt", 'w')
wordList = open("wordlist.txt", 'w')

# get all the links of every unit
def getLinks(pageID):
    pageLink = 'http://www.shanbay.com/wordbook/' + str(pageID) + '/'
    pageHtml = requests.get(pageLink)
    unitLinks = re.findall("/wordlist/%s/\d+/" % (str(pageID)), pageHtml.text)
    for link in unitLinks:
        link = "http://www.shanbay.com" + link + '\n'
        linkFile.write(link)

# get words in a single unit page
def getWords(theLink):
    for i in range(1, 11):
        wordPage = theLink + '?page=' + str(i)
        targetPage = requests.get(wordPage)
        words = re.findall('<strong>.*</strong>', targetPage.text)
        for word in words:
            wordList.write(word[8: -9] + '\n')

# get all words in a single unit
def getAllUnitWords():
    unitPage = linkFile.readline()
    if unitPage == '\n':
        return 0
    else :
        getWords(unitPage)
        getAllUnitWords()

getLinks(wordListID)

linkFile.close()

linkFile = open("links.txt", 'r')

getAllUnitWords()

linkFile.close()
wordList.close()