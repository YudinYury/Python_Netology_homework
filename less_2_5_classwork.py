'''lesson_2_5 classwork «Вызов других программ»

'''
# pip install chardet
import chardet
import copy
import os
from pprint import pprint
import sys
import subprocess
import time

##################################################################################################
# with open('recipes.txt', encoding='cp1251') as f:
#     text=f.read()
    # print(text)

##################################################################################################
def main():
    user_name = os.environ['USERNAME']
    print('Hi', user_name)
    # os.environ['MY_NEW_VAR'] = 'NEW_VAR'
    # print(os.environ['MY_NEW_VAR'])

    # for name_env_var, value_env_var in os.environ.items():
    #     print(name_env_var, '->', value_env_var)

    print('This is stdout', file=sys.stdout)
    print('This is stderr', file=sys.stderr)
    sys.stderr.write('This is stderr.write\n')

    # with open('logs.txt', mode='a') as f:
    #     print('This text in file', file=f)

    print(type(sys.argv), sys.argv)
    if len(sys.argv) == 1:
        print('Hello world')
    else:
        print('Hello {}'.format(sys.argv[1]))

    print('--------- call external program')
    subprocess.call('ping yandex.ru')
    process = subprocess.run('ping yandex.ru')  # run возвращает нам объект процесса
    print('Return code "ping yandex.ru" = ', process.returncode)
    # process_2 = subprocess.run('ping yyyyyandex.ru')
    # print('Return code "ping yandex.ru" = ', process_2.returncode)
    print('stdout ping =', process.stdout) # Python перехватит и будет None
    print('stderr ping =', process.stderr)
    print('argv ping =', process.args, type(process.args))
    process = subprocess.run('python less_2_3_classwork.py')
    print('Return code python less_2_3_classwork.py =', process.returncode)

    programm = subprocess.Popen('')


    exit(0)


#################################################################################################
if __name__ == '__main__':
    main()


