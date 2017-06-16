'''lesson_1_5 homework
Имеется группа студентов, у каждого из которых есть следующие характеристики: имя, фамилия, пол, предыдущий опыт в
программировании (бинарная переменная), 5 оцененных по 10-бальной шкале домашних работ, оценка за экзамен по 10-балльной шкале.
Необходимо написать программу, которая в зависимости от запроса пользователя будет выводить:
обратить внимание:
- чтобы отрабатывалась ситуация с полными тезками отличниками
- не должно быть дублирования кода (и цикла) - использовать одну функцию при разнице в одном параментре в данных
'''

#TODO 2:
# среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола б)наличия опыта в виде:
#         Средняя оценка за домашние задания у мужчин: A
#         Средняя оценка за экзамен у мужчин: B
#         Средняя оценка за домашние задания у женщин: C
#         Средняя оценка за экзамен у женщин: D
#
#         Средняя оценка за домашние задания у студентов с опытом: E
#         Средняя оценка за экзамен у студентов с опытом: F
#         Средняя оценка за домашние задания у студентов без опыта: G
#         Средняя оценка за экзамен у студентов без опыта: H
# где A, B, C, D, E, F, G, H - вычисляемые значения;

#TODO 3:
# определять лучшего студента, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен в виде:
# Лучший студент: S с интегральной оценкой Z
# если студент один или:
# Лучшие студенты: S... с интегральной оценкой Z
# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение.
# Студентов должно быть не менее 6.
# Код должен быть грамотно декомпозирован (максимально используйте функции).

import copy
import math

group = [
    {'name':'Tony',  'family':'Moore', 'gender':'m', 'experience':False, 'homework':[9,9,10,10,9], 'exam':9},
    {'name':'Kevin', 'family':'Brown', 'gender':'m', 'experience':False, 'homework': [6,7,8,9,10], 'exam':9},
    {'name':'Rayan', 'family':'Evans', 'gender':'m', 'experience':False, 'homework': [7,7,6,9,8], 'exam':8},
    {'name':'Alex',  'family':'Wilson', 'gender':'f','experience':True, 'homework': [10,8,9,10,10], 'exam':10},
    {'name':'Mary',  'family':'Hall', 'gender':'f',  'experience':False, 'homework': [6,5,6,8,7], 'exam':7},
    {'name':'Juri',  'family':'Judi', 'gender':'m',  'experience':True, 'homework': [10,9,10,8,10], 'exam':10},
    {'name':'Aaron', 'family':'Harris', 'gender':'m','experience':False, 'homework': [6,5,6,5,7], 'exam':6},
    {'name':'Ameli', 'family':'Moore', 'gender':'f', 'experience':False, 'homework': [6,7,9,8,9], 'exam':8},
    {'name':'Juri',  'family':'Judi', 'gender':'m',  'experience':False, 'homework': [8,10,10,9,10], 'exam':10},
]
user_cmd_list = ['m', 'f', 'q']
exp_list=['y', 'n', 'q']
str_for_gender='Pls enter gender "f"(for male) or "m" (for male) or "q" (for Quit):'
str_for_exp='Do they have experience in programming? Pls enter gender "y"(for YES) or "n" (for NO) or "q" (for Quit):'
#############################################################################################################
def get_exam_average_rating(gr):
    aver_exam=0
    summ_exam=0
    rt=0
    for person in gr:
        summ_exam+=int(person['exam'])
        rt += 1
    aver_exam=summ_exam/rt
    # print('rates=', rt, '   summ=', summ_exam,'   aver=', aver_exam)
    return aver_exam
#############################################################################################################
# gr is group list (dict type); gender = m (for male) or f (for famale) or mf (for all)
def get_exam_average_rating_for_gen_and_exp(gr, gen, exp):
    # print('gender=',gen, ' | ', 'experience=',exp)
    aver_exam=0
    summ_exam=0
    rt=0
    for person in gr:
        if gen is None:
            if exp is None:
                summ_exam += int(person['exam'])
                rt += 1
            elif exp == person['experience']:
                summ_exam += int(person['exam'])
                rt += 1
        elif person['gender'] in gen:
            if exp == person['experience']:
                summ_exam += int(person['exam'])
                rt += 1
            elif exp is None:
                summ_exam += int(person['exam'])
                rt += 1
        else:
            pass

        # print('rates=', rt, '   summ=', summ_exam,'   aver=', aver_exam)

    if rt!=0:
        aver_exam = summ_exam / rt
    else:
        aver_exam = rt
    return aver_exam

#############################################################################################################
def get_group_average_rating(gr):
    aver_rt=0
    sum_rt=0
    rt=0 # буду считать количество оценок
    for person in gr:
        for i in person['homework']:
            sum_rt+=int(i)
            rt += 1
        # print(rt)

    aver_rt=sum_rt/rt
    # print('rates=', rt, '   summ=', sum_rt,'   aver=', aver_rt)
    return aver_rt
#############################################################################################################
def get_group_average_rating_for_gen_and_exp(gr, gen, exp):
    # print('gender=',gen, ' | ', 'experience=',exp)
    aver_rt=0
    summ_rt=0
    rt=0  # буду считать количество оценок
    for person in gr:
        if gen is None:
            if exp is None:
                for grade in person['homework']:
                    # print('grade=', grade)
                    summ_rt += int(grade)
                    rt += 1
            elif exp == person['experience']:
                for grade in person['homework']:
                    summ_rt += int(grade)
                    rt += 1
        elif person['gender'] in gen:
            if exp is None:
                for grade in person['homework']:
                    summ_rt += int(grade)
                    rt += 1
            elif exp == person['experience']:
                for grade in person['homework']:
                    summ_rt += int(grade)
                    rt += 1
        else:
            pass

        # print('rates=', rt, '   summ=', summ_exam,'   aver=', aver_exam)

    if rt!=0:
        aver_rt = summ_rt / rt
    else:
        aver_rt = rt
    return aver_rt


#############################################################################################################

def get_user_cmd(str,cmd_list):
    gender='q'
    while True:
        # print('Pls enter gender "f"(for male) or "m" (for male) or "q" (for Quit):')
        print(str)
        gender = input().lower()
        if gender in cmd_list:
            return gender
        else:
            print('wrong input')
            continue
    return gender
#############################################################################################################

def main():
    # gender=''
    # gender=get_user_cmd(str_for_gender, user_cmd_list)
    # if gender=='q':
    #     print('Bye ... ')
    #     exit(0)
    # experience=None
    # exp_tmp=''
    # exp_tmp = get_user_cmd(str_for_exp, exp_list)
    # if exp_tmp == 'q':
    #     print('Bye ... ')
    #     exit(0)
    # if exp_tmp == 'y':
    #     experience=True
    # if exp_tmp == 'n':
    #     experience = False
    # print('gender=', gender, ' | experience=',experience,type(experience))

    print('Средняя оценка за домашние задания у мужчин: ', round(get_group_average_rating_for_gen_and_exp(group, 'm', None),1))
    print('Средняя оценка за экзамен у мужчин: ', round(get_exam_average_rating_for_gen_and_exp(group, 'm', None),1))
    print('Средняя оценка за домашние задания у женщин: ', round(get_group_average_rating_for_gen_and_exp(group, 'f', None),1))
    print('Средняя оценка за экзамен у женщин: ', round(get_exam_average_rating_for_gen_and_exp(group, 'f', None),1))
    print(' ')
    print('Средняя оценка за домашние задания у студентов с опытом: ', round(get_group_average_rating_for_gen_and_exp(group, None, True),1))
    print('Средняя оценка за экзамен у студентов с опытом: ', round(get_exam_average_rating_for_gen_and_exp(group, None, True),1))
    print('Средняя оценка за домашние задания у студентов без опыта: ', round(get_group_average_rating_for_gen_and_exp(group, None, False),1))
    print('Средняя оценка за экзамен у студентов без опыта: ', round(get_exam_average_rating_for_gen_and_exp(group, None, False),1))

    # print(' ')
    # print('Средняя оценка за домашние задания по группе: ', round(get_group_average_rating_for_gen_and_exp(group, None, None),1))
    # print('Средняя оценка за экзамен: ', round(get_exam_average_rating_for_gen_and_exp(group, None, None),1))

#############################################################################################################

main()

