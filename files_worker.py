import csv
import json
import os
from mimesis import Address, Generic, Finance, Person
from transliterate import translit


try:
    os.mkdir("pars")
except FileExistsError:
    print('Already have the directory, Working...')


file_path = "schedules/schedule.csv"
fieldnames = ['Nomber', 'Working Company', 'Passanger Name', 'departure point', 'departure time', 'destination point',
              'arrival time', 'cost ticket']

with open(file_path, "w", newline='') as fh:
    writer = csv.DictWriter(fh, lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()

address_ua, address_en, generic, finance, person = Address('uk'), Address('en'), Generic('ru'), Finance('en'), Person('uk')

for i in range(200):
    work_company = finance.company()
    pass_name = translit(person.full_name(), language_code='uk', reversed=True)
    dep_point = translit(address_ua.city(), language_code='uk', reversed=True)
    dep_time = str(generic.datetime.time())[0:5]
    dest_point = address_en.city()
    arr_time = str(generic.datetime.time())[0:5]
    cost_ticket = finance.price(minimum=100, maximum=9000)
    with open(file_path, "a", newline='') as fh:
        writer = csv.DictWriter(fh, lineterminator='\n', fieldnames=fieldnames)
        writer.writerow({'Nomber': i+1, 'Working Company': work_company, 'Passanger Name': pass_name,
                         'departure point': dep_point, 'departure time': dep_time, 'destination point': dest_point,
                         'arrival time': arr_time, 'cost ticket': cost_ticket})

data_flew = []
with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data_flew.append(row)
print(data_flew)


with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    dict_flew = {}
    for row in reader:
        dict_flew.update({row.get('Nomber'): row})
    with open("schedules/schedule.json", "a") as fh:
        json.dump(dict_flew, fh, indent=4, sort_keys=True)
