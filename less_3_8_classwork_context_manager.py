"""lesson_3_8_Classwork "Patterns"

"""

from  contextlib import contextmanager


# with open('less_3_8_classwork_user_command.py') as f:
#     print(f.read())

@contextmanager
def my_cm():
    print('before')
    try:
        yield
    finally:
        print('after')


with my_cm():
    print('body')
