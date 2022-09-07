import requests
import json
from bs4 import BeautifulSoup
import datetime
import csv
import os


"""
Main part of exercise
"""

try:
    os.mkdir("pars")
except FileExistsError:
    print('Already have the directory, Working...')

response = requests.get('https://httpbin.org/anything')
content_text = response.text
content_json = response.json()

print(f'response.status_code: \n {response.status_code}')
print(f'content_text: \n {content_text}')
print(f'content_json: \n {content_json}')

with open("pars/content.html", "w+", encoding="utf-8") as file:
    file.write(content_text)

with open("pars/content.json", "w+") as fh:
    json.dump(content_json, fh, indent=4, sort_keys=True)

response = requests.get('https://direct.it-kharkiv.com/wp-content/uploads/2020/04/hillil.png')

with open("pars/hillil.png", "wb") as file:
    file.write(response.content)


"""
Second part of exercise "Вигадай ще кілька задач, попрактикуйся з модулем"
"""


def usd_pars():
    url = 'https://kurs.com.ua/valyuta/usd'

    headers = {
        "Accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    with open("pars/usd.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open("pars/usd.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    usd_course = []

    course_usd = soup.find_all(class_="course")

    for course_usd in course_usd:
        course_usd = course_usd.text.strip().split("\n")
        usd_course.append(course_usd)

    usd_buy = round((float(usd_course[0][0])), 2)
    usd_sell = round((float(usd_course[1][0])), 2)
    usd_black = round((float(usd_course[2][0])), 2)
    return [usd_buy, usd_sell, usd_black]


def eur_pars():
    url = 'https://kurs.com.ua/valyuta/eur'

    headers = {
        "Accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    with open("pars/eur.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open("pars/eur.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    eur_course = []

    course_eur = soup.find_all(class_="course")

    for course_eur in course_eur:
        course_eur = course_eur.text.strip().split("\n")
        eur_course.append(course_eur)

    eur_buy = round((float(eur_course[0][0])), 2)
    eur_sell = round((float(eur_course[1][0])), 2)
    eur_black = round((float(eur_course[2][0])), 2)
    return [eur_buy, eur_sell, eur_black]


fieldnames = ['datetime', 'dollars buy', 'dollars sell',
              'dollars commercial', 'euro buy', 'euro sell', 'euro commercial']

with open('pars/sheet_course.csv', "w", newline='') as fh:
    writer = csv.DictWriter(fh, lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()


def save_course(usd_pars, eur_pars):
    usd_pars_list = usd_pars()
    eur_pars_list = eur_pars()
    myData = [[datetime.datetime.today().strftime("%d.%m %H:%M"), usd_pars_list[0], usd_pars_list[1], usd_pars_list[2],
               eur_pars_list[0], eur_pars_list[1], eur_pars_list[2]]]
    with open('pars/sheet_course.csv', 'a') as myFile:
        writer = csv.writer(myFile, lineterminator='\n')
        writer.writerows(myData)
    print("Writing completed")
    print(f'today ({myData[0][0]}) course is:\n'
          f'dollars buy {usd_pars_list[0]}\n'
          f'dollars sell {usd_pars_list[1]}\n'
          f'dollars commercial {usd_pars_list[2]}\n'
          f'euro buy {eur_pars_list[0]}\n'
          f'euro sell {eur_pars_list[1]}\n'
          f'euro commercial {eur_pars_list[2]}\n')


save_course(usd_pars, eur_pars)

