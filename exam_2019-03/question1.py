def read_ini(filename):
    options = dict()
    category = None
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if len(line) > 0 and line[0] != '#':
                if line[0] == '[':
                    category = line.strip('[]')
                    options[category] = dict()
                else:
                    if category is None:
                        raise ValueError('Category not specified')
                    parameter, value = line.split('=', maxsplit=1)
                    options[category][parameter.strip()] = value.strip()
    return options


def write_ini(filename, options):
    with open(filename, 'w') as f:
        for section, parameters in options.items():
            f.write('[{}]\n'.format(section))
            for parameter, value in parameters.items():
                f.write('{}={}\n'.format(parameter, value))
            f.write('\n')


def apply_overrides(config, user):
    for user_section, user_options in user.items():
        if user_section in config:
            for user_parameter, user_value in user_options.items():
                if user_parameter in config[user_section]:
                    config[user_section][user_parameter] = user_value
                else:
                    hint = ''
                    for section, options in config.items():
                        if user_parameter in options:
                            hint = 'Did you mean to put this under \'{}\''.format(section)
                            break
                    print('Parameter \'{}\' not found under section \'{}\'. {}'.format(
                        user_parameter,
                        user_section,
                        hint))
        else:
            print('Section \'{}\' not found in default config. Skipping.'.format(user_section))


config = read_ini('default_config.ini')
user = read_ini('user_overrides.ini')
apply_overrides(config, user)
write_ini('config.ini', config)
