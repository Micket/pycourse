import datetime
from collections import Counter, defaultdict

# 1. parse lines from the license server
#2023-01-12 user=ohmanm version=1.0.1
#2023-01-12 user=ohmanm version=1.0.1

def parse_line(line: str):
    date, user, version = line.split(' ')
    year, month, day = date.split('-')
    user = user.split('=')[-1]
    version = version.split('=')[-1]
    version = tuple(int(x) for x in version.split('.'))
    date = datetime.date(year=int(year), month=int(month), day=int(day))
    return date, user, version

x = parse_line('2023-01-12 user=ohmanm version=1.0.1')
print(x)


def collect_license_data(logfile):
    last_use = dict()
    user_usage = defaultdict(Counter)
    with open(logfile) as file:
        for line in file:
            date, user, version = parse_line(line.strip())
            if version in last_use:
                last_use[version] = max(last_use[version], date)
            else:
                last_use[version] = date

            user_usage[user][version] += 1
    return user_usage, last_use

user_usage, last_use = collect_license_data('example.txt')
print(user_usage, last_use)

# do something more with the data

