import time

# print(time.time())
# print(time.localtime(time.time()))


def showcurrenttime():
    print(time.strftime('%Y-%m-%d\t%H:%M:%S', time.localtime(time.time())))
    return time.strftime('%Y-%m-%d\t%H:%M:%S', time.localtime(time.time()))


def current_date_and_time():
    print(time.strftime('%Y-%m-%d\t%H:%M:%S', time.localtime(time.time())))
    return time.strftime('%Y-%m-%d\t%H:%M:%S', time.localtime(time.time()))


if __name__ == '__main__':
    showcurrenttime()
    current_date_and_time()
