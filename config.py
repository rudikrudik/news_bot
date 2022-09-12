import simplelog

config_dict = {}
config_state = True

try:
    with open('config.ini', 'r') as config_file:
        for line in config_file:
            if line[:1] != '#' and line[:1] !='\n':
                try:
                    k, v = [word.strip() for word in line.split('=')]
                    config_dict[k] = v
                except ValueError:
                    print('Value error: expected 2, got 1. Check config.ini')
                    simplelog.write_log('Value error: expected 2, got 1. Check config.ini')
                    config_state = False

except FileNotFoundError:
    print('Config file "config.ini" not found')
    simplelog.write_log('Config file "config.ini" not found')
    config_state = False

except PermissionError:
    print('Not permission to read file "config.ini"')
    simplelog.write_log('Not permission to read file "config.ini"')
    config_state = False

try:
    if config_dict['TOKEN'] == '':
        print('Value "TOKEN" is empty')
        simplelog.write_log('Value "TOKEN" is empty')
        config_state = False

except KeyError:
    print('Directive "TOKEN" not set in config.ini')
    simplelog.write_log('Directive "TOKEN" not set in config.ini')
    config_state = False

try:
    if config_dict['CHAT_ID'] == '':
        print('Value "CHAT_ID" if empty')
        simplelog.write_log('Value "CHAT_ID" if empty')
        config_state = False

except KeyError:
    print('Directive "CHAT_ID" not set in config.ini')
    simplelog.write_log('Directive "CHAT_ID" not set in config.ini')
    config_state = False


if config_state == False:
    simplelog.write_log('Read config.ini => ERROR')
    exit()
else:
    simplelog.write_log('Read config.ini => OK')