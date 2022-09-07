import csv
import json
import os
from mimesis import Address, Generic, Finance, Person
from transliterate import translit


try:
    os.mkdir("schedules")
except FileExistsError:
    print('Already have the directory, Working...')


fieldnames = ['Nomber', 'Working Company', 'Passanger Name', 'departure point', 'departure time', 'destination point',
              'arrival time', 'cost ticket']

with open("schedules/schedule.csv", "w", newline='') as fh:
    writer = csv.DictWriter(fh, lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()

address_ua, address_en, generic, finance, person = Address('uk'), Address('en'), Generic('ru'), Finance('en'), Person('uk')

for i in range(300):
    work_company = finance.company()
    pass_name = translit(person.full_name(), language_code='uk', reversed=True)
    dep_point = translit(address_ua.city(), language_code='uk', reversed=True)
    dep_time = str(generic.datetime.time())[0:5]
    dest_point = address_en.city()
    arr_time = str(generic.datetime.time())[0:5]
    cost_ticket = finance.price(minimum=100, maximum=9000)
    with open("schedules/schedule.csv", "a", newline='') as fh:
        writer = csv.DictWriter(fh, lineterminator='\n', fieldnames=fieldnames)
        writer.writerow({'Nomber': i+1, 'Working Company': work_company, 'Passanger Name': pass_name,
                         'departure point': dep_point, 'departure time': dep_time, 'destination point': dest_point,
                         'arrival time': arr_time, 'cost ticket': cost_ticket})


def reader_csvdb() -> dict:
    dict_flew = {}
    try:
        with open("schedules/schedule.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dict_flew.update({row.get('Nomber'): row})
        return dict_flew
    except Exception as error:
        print(f'Something WRONG! {error}')
        raise error


flew_db = reader_csvdb()
print(flew_db)


def json_writer(flew_db: dict, directory: str) -> None:
    try:
        with open(directory, "w") as fh:
            json.dump(flew_db, fh, indent=4, sort_keys=True)
        print('succes dumped!')
    except Exception as error:
        print(f'Something WRONG! {error}')
        raise error


json_writer(flew_db, "schedules/schedule.json")
