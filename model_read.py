import os

def read_file(name):
    data = open(name, 'r')
    isempty = os.stat(name).st_size
    if isempty == 0:
        print('Телефонная книга пуста, давайте запишем новый контакт!')
    else:
        for line in data:
            print(line)
    data.close()