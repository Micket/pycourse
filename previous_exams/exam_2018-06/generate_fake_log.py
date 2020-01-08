# Generar fejkade loggfiler.

from datetime import datetime
from random import randint, choice, uniform

def print_event(date, event, user, ip, text=None):
    dstr = date.strftime('[%Y-%m-%dT%H:%M:%S]')
    if text is None:
        print('{} - {}: {}@{}'.format(dstr, event, user, ip))
    else:
        print('{} - {}: "{}" {}@{}'.format(dstr, event, text, user, ip))

def rand_ip():
    return '{}.{}.{}.{}'.format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))

def rand_hour(a, b):
    date = datetime.now()
    return date.replace(second=randint(0, 59)).replace(minute=randint(0, 59)).replace(hour=randint(a, b))

users = ['micke', 'thomas', 'kristoffer', 'hebbe', 'glenn', 'kal', 'ada', 'svea']

filenames = ['stuff', 'things', 'trinkets', 'important stuff', 'readme', 'results', 'temp', 'tmp']
local_ips = [rand_ip() for _ in range(5)]
global_ips = [rand_ip() for _ in range(10)]

for _ in range(20):
    date = rand_hour(6, 18)
    ip = choice(local_ips)
    user = choice(users[0:2])
    print_event(date, 'LOGIN_SUCCESS', user, ip)

for _ in range(30):
    date = rand_hour(9, 15)
    ip = choice(local_ips)
    user = choice(users[0:3])
    print_event(date, 'LOGIN_SUCCESS', user, ip)

for _ in range(5):
    date = rand_hour(19, 23)
    ip = choice(local_ips)
    user = choice(users[0:3])
    print_event(date, 'LOGIN_SUCCESS', user, ip)

for _ in range(20):
    date = rand_hour(0, 23)
    ip = choice(local_ips)
    user = choice(users[1:])
    print_event(date, 'LOGIN_FAILED', user, ip)

for _ in range(20):
    date = rand_hour(0, 4)
    ip = choice(global_ips)
    user = choice(users[3:])
    print_event(date, 'LOGIN_FAILED', user, ip)

for _ in range(60):
    date = rand_hour(17, 23)
    ip = choice(global_ips)
    user = choice(users[3:])
    print_event(date, 'LOGIN_FAILED', user, ip)


for _ in range(10):
    date = rand_hour(9, 16)
    filename = choice(filenames)
    ip = choice(local_ips)
    user = choice(users[0:3])
    print_event(date, 'FILE_UPLOAD', user, ip, filename + '.txt')

for _ in range(2):
    date = rand_hour(7, 13)
    ip = choice(local_ips)
    user = users[1]
    print_event(date, 'CHANGED_PASSWORD', user, ip, '********')

"""
[2018-05-06T13:35:45] - LOGIN_FAILED: mikael@123.45.67.89
[2018-05-06T14:03:10] - LOGIN_SUCCESS: thomas@10.20.30.40
[2018-06-06T15:35:45] - FILE_UPLOAD: "exam_results.txt" mikael@123.45.67.89
"""
