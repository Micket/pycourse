from collections import defaultdict

# Part A
def read_users(filename):
    users = dict()
    with open(filename) as file:
        for line in file:
            data = line.split(':')
            if int(data[2]) >= 500:
                users[data[0]] = data[4]
    return users

# Part B
def read_groups(filename):
    groups = defaultdict(list)
    with open(filename) as file:
        for line in file:
            group_name, password, gid, users = line.split(':')
            for user in users.strip().split(','):
                groups[user].append(group_name)
    return groups

# Part C
def print_user_table(names, groups):
    # Longest username (minimum 4)
    max_user = max(max([len(name) for name in names.keys()]), 4)
    # Longest name (minimum 4):
    max_name = max(max([len(name) for name in names.values()]), 4)

    format_string = '{:<' + str(max_user) + '} | {:<' + str(max_name) + '} | {}'
    print(format_string.format('User', 'Name', 'Groups'))
    print('-' * (max_user) + '-+-' + '-' * max_name + '-+-' + '-' * 6)
    for user, name in sorted(names.items()):
        user_groups = ', '.join(groups[user])
        print(format_string.format(user, name, user_groups))

names = read_users('passwd.txt')
groups = read_groups('group.txt')
print_user_table(names, groups)
