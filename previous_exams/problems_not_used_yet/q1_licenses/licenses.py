import datetime
from collections import Counter, defaultdict

# 1. 1p: parse lines from the license server
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

# 2. 3p Parse the entire logfile with license checkouts
# into 2 dictionaries:
# A. that maps each version to its latest usage date
# B. that maps each user to how many times they've used each version

def collect_license_data(logfile):
    last_use = dict()
    users_use = defaultdict(Counter)
    with open(logfile) as file:
        for line in file:
            date, user, version = parse_line(line.strip())
            if version in last_use:
                last_use[version] = max(last_use[version], date)
            else:
                last_use[version] = date

            users_use[user][version] += 1
    return users_use, last_use

users_use, last_use = collect_license_data('example.txt')
print("Philip used v1.2.4", users_use['philip'][(1, 2, 4)], "times")
print("Conrad used v1.2.4", users_use['conrad'][(1, 2, 4)], "times")
print("0.1.4 was last used", last_use[(0, 1, 4)])

# 3. 1.5p write a function that displays the stats for a paricular version:
def check_usage(version, last_use, users_use):
    if version in last_use:
        print(f"v{version[0]}.{version[1]}.{version[2]} was used as recently as {last_use[version]}")
        for user, user_use in users_use.items():
            if version in user_use:
                print(f"{user:<10}: {user_use[version]:>2} times")
    else:
        print(f"version {version[0]}.{version[1]}.{version[2]} has not been used")

check_usage((1, 2, 3), last_use, users_use)
check_usage((1, 2, 4), last_use, users_use)

# 4. 1p check major version usage
def check_major(major_version, last_use):
    print(f"Major version {major_version}:")
    for version, date in sorted(last_use.items()):
        if version[0] == major_version:
            print(f'v{version[0]}.{version[1]}.{version[2]}: {date}')

check_major(1, last_use)
