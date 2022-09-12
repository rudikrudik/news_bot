import time


def write_log(message):
    format_time = time.strftime("%Y-%m-%d %H:%M:%S")
    log_file = open('log.txt', 'a+')
    log_file.write(f'{format_time} {message}\n')
    log_file.close()


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")