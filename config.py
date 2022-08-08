config_dict = {}

try:
    with open('config.ini', 'r') as config_file:
        for line in config_file:
            if line[:1] != '#' and line[:1] !='\n':
                k, v = [word.strip() for word in line.split('=')]
                config_dict[k] = v
except FileNotFoundError:
    print('Config file "config.ini" not found')
except PermissionError:
    print('Not permission to read file "config.ini"')

try:
    if config_dict['TOKEN'] == '':
        print('Value "TOKEN" is empty')
except KeyError:
    print('Directive "TOKEN" not set in config.ini')

try:
    if config_dict['CHAT_ID'] == '':
        print('Value "CHAT_ID" if empty')
except KeyError:
    print('Directive "CHAT_ID" not set in config.ini')

