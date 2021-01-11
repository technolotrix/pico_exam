import datetime
import random
import string

def create_test_email(email_str):
    now = datetime.datetime.now()
    unixtime = now - datetime.datetime(1970,1,1)
    t = unixtime.total_seconds()
    return email_str.format(t)

def create_test_password(str_size):
    allowed_chars = string.ascii_letters + '!@#$%^&*()' + '0123456789'
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

if __name__ == '__main__':
    print(create_test_email('foobar{0}@gmail.com'))
    print(create_test_password(10))