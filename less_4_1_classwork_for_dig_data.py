"""lesson_4_1_Classwork "Data processing tools"

"""

from functools import lru_cache


@lru_cache(maxsize=1)
def calc(arg):
    print('calc', arg)
    return arg


print('res', calc(1))
print('res', calc(1))
print('res', calc(2))
print('res', calc(1))
