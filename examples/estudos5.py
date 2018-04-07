from collections import namedtuple
import csv


def its_name_startswith_r(person):
    return person.name.startswith('R')

Person = namedtuple('Person', ['name', 'age', 'address'])

# this file is in directory files of this project
# it's has to be moved to /tmp/ of your machine to code works fine.
with open('/tmp/file_to_create_persons.csv', 'rt') as file:
    persons_in_file = csv.reader(file, delimiter=',', quotechar='|')
    list_person = []

    for row in persons_in_file:
        list_person.append(Person(*row))


for person in list_person:
    if its_name_startswith_r(person):
        print(person.name, person.age, person.address)

file.close()
