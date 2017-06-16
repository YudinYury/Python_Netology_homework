'''lesson_1_5 homework
Имеется группа студентов, у каждого из которых есть следующие характеристики: имя, фамилия, пол, предыдущий опыт в
программировании (бинарная переменная), 5 оцененных по 10-бальной шкале домашних работ, оценка за экзамен по 10-балльной шкале.
Необходимо написать программу, которая в зависимости от запроса пользователя будет выводить:
обратить внимание:
- чтобы отрабатывалась ситуация с полными тезками отличниками
- не должно быть дублирования кода (и цикла) - использовать одну функцию при разнице в одном параментре в данных
'''

#TODO 3:
# определять лучшего студента, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен в виде:
# Лучший студент: S с интегральной оценкой Z
# если студент один или:
# Лучшие студенты: S... с интегральной оценкой Z
# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение.
# Студентов должно быть не менее 6.
# Код должен быть грамотно декомпозирован (максимально используйте функции).

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
#############################################################################################################
def get_aver_homework(pers):
    aver_hw=0
    summ_hw=0
    rt=0
    for i in pers['homework']:
        summ_hw+=int(i)
        rt += 1

    aver_hw=summ_hw/rt
    # print('rates=', rt, '   summ=', summ_hw,'   aver=', aver_hw)
    return aver_hw
#############################################################################################################
def get_integral_grad(persn):
    grad=float(0)
    grad=round(0.6*get_aver_homework(persn)+0.4*int(persn['exam']),2)
    # print(persn['name'], ' ', grad)
    return grad
#############################################################################################################
def get_best_stud (gr):
    best_students= [float(0)]
    new_integral_grad=float(0)
    for person in gr:
        new_integral_grad=get_integral_grad(person)
        # print(type(new_integral_grad), 'new integral_grad=', new_integral_grad)
        # print('best_students = ', best_students)
        # print(person)
        if new_integral_grad > best_students[0]:
            best_students.clear()
            best_students.append(new_integral_grad)
            best_students.append(person['name'] + ' '+ person['family'])
        elif new_integral_grad == best_students[0]:
            best_students.append(person['name'] + ' '+ person['family'])

    return best_students
#############################################################################################################

def main():
    best_list=[]
    quantity=0
    best_list=get_best_stud(group)
    quantity=len(best_list)
    if quantity == 2:
        print('Лучший студент: {0} с интегральной оценкой {1}'.format(best_list[1], best_list[0]))
    else:
        print('Лучшие студенты:')
        for i in best_list[1::]:
            print(i)
        print('с интегральной оценкой {0}'.format(best_list[0]))

#############################################################################################################

main()

