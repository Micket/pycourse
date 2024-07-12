# A
config = read_ini('default_config.ini')
print(config)

# B
game_options = {'Graphics': {'resolution': '1920x1080', 'texture_quality': 'high'},
                'Gameplay': {'difficulty': 'medium', 'lives': '9'}}
write_ini('game_options.ini', game_options)

# C
config = read_ini('default_config.ini')
user = read_ini('user_overrides.ini')
apply_overrides(config, user)
write_ini('config.ini', config)
