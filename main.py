import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
weather = "https://weather.com/weather/monthly/l/60eb7796d033a593c3294ffa7d76578ee16343ee1b14bbab570b30eee2a0fb0e"
import flask
from flask import request, jsonify


#-------------------------
# def main():
#     potato = "https://genius.com/Rick-astley-never-gonna-give-you-up-lyrics"
#
#     page = requests.get(potato)
#
#     parsedPage = BeautifulSoup(page.content, "html.parser")
#     print(parsedPage)
#     lyrics = parsedPage.find("div", class_="Lyrics__Container-sc-1ynbvzw-10 cvsIWi")
#
#     lyric_list = lyrics.prettify().split("\n")
#
#     lines = []
#     for line in lyric_list:
#         l = line.strip()
#         if len(l) != 0 and l[0] != '<':
#             lines.append(l)
#     print(lines)
#     return lines




# print(lines)

#---------------------



def getMonthlyWeather():
    page = requests.get(weather)

    parsedPage = BeautifulSoup(page.content, "html.parser")

    grid = parsedPage.find("div", class_= "Calendar--gridWrapper--1oa1f")
    temps = grid.find_all("div", class_= "CalendarDateCell--tempHigh--2VBba")
    days = grid.find_all("span", class_= "CalendarDateCell--date--3Fw3h")
    tempList = []
    tempDic = []
    dayList = range(35)
    # for temp in temps:
    #     tempList.append(temp.text)
    # print(temps)
    # print(days)
    # print(range(len(days)))
    # print(range(len(temps)))
    for i in (range(len(days))):
        tempDic.append({
            "day" : days[i].text,
            "temp" : temps[i].text
        })

    print (tempDic)
    return tempDic

# getMonthlyWeather()
# plt.plot(dayList,tempList)
#
# plt.show()
# -----------------------------------------------------------------------------------

