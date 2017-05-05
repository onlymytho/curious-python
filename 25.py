# Record tester

import Record as r

r.start('a')

def sum():
    num = 0
    for i in range(1,10000, 1000):
        r.start('b')
        for j in range(1,10000):
            (num + i)*j
        r.end('b')
    return num

sum()
r.end('a')
