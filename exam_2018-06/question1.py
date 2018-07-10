import datetime
import collections

def parse_login_event(event):
    datestr, text = event.split(' - ', maxsplit=1)
    event_type, message = text.split(':', maxsplit=1)
    if event_type == 'LOGIN_SUCCESS':
        success = True
    elif event_type == 'LOGIN_FAILED':
        success = False
    else:
        return None

    d = datetime.datetime.strptime(datestr, '[%Y-%m-%dT%H:%M:%S]')
    user, ip = message.strip().split('@')
    return d, success, user, ip

def login_stats(filename):
    hour_failed = collections.Counter()
    hour_success = collections.Counter()
    ip_failed = collections.Counter()
    user_failed = collections.Counter()

    with open(filename) as f:
        for line in f:
            results = parse_login_event(line)
            if results is not None:
                time, success, user, ip = results
                if success:
                    hour_success[time.hour] += 1
                else:
                    hour_failed[time.hour] += 1
                    user_failed[user] += 1
                    ip_failed[ip] += 1

    print('Most failed IP: {} ({} attempts)'.format(*ip_failed.most_common(1)[0]))
    print('Most failed user: {} ({} attempts)'.format(*user_failed.most_common(1)[0]))

    print('Hour | Failed | Success')
    print('-----|--------|--------')
    for hour in range(0, 24):
        print('{:4} | {:6} | {:7}'.format(hour, hour_failed[hour], hour_success[hour]))

login_stats('events.log')
