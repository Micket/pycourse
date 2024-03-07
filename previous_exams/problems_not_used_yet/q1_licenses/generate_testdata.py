import random
import datetime

def generate_random_dates(start_date, end_date, num_dates):
    delta = end_date - start_date
    random_dates = []
    for _ in range(num_dates):
        random_days = random.randint(0, delta.days)
        random_date = start_date + datetime.timedelta(days=random_days)
        random_dates.append(random_date)
    return random_dates

def generate_random_tuples(num_tuples):
    random_tuples = []
    bugfix = [0, 4]
    for _ in range(num_tuples):
        random_tuple = (random.randint(0, 2), random.randint(0, 2)+1, random.choices(bugfix, k=1)[0])
        random_tuples.append(random_tuple)
    return random_tuples

def generate_random_usernames(num_usernames):
    usernames = ['rodriquez', 'turanga', 'philip', 'conrad', 'hubert', 'john', 'wong']
    random_usernames = random.choices(usernames, k=num_usernames)
    return random_usernames

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2023, 12, 31)
num = 2000
dates = generate_random_dates(start_date, end_date, num)
usernames = generate_random_usernames(num)
versions = generate_random_tuples(num)
for date, username, version in zip(dates, usernames, versions):
    if date.year == 2023 and version[0] < 2:
        continue
    if date.year == 2022 and version[0] < 1:
        continue
    if date.year == 2021 and version[0] == 2:
        continue
    if date.year == 2020 and version[0] > 0:
        continue

    print(f'{date} username={username} version={version[0]}.{version[1]}.{version[2]}')

