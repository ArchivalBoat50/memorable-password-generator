import os, random, string

def passwordGen():
    length = 13
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024)) 
    print(''.join(random.choice(chars) for i in range(length)))

passwordGen()
