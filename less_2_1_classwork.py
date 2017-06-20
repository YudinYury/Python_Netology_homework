'''lesson_2_1 classwork «Открытие и чтение файла, запись в файл»

'''

import copy
import math
import csv

# less_2_1_class_grades.txt

# f=open('less_2_1.txt')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# f.close()

# try:
#     with open('less_2_1.txt') as f:
#         1/0
#         print(f.readlines())
# except ZeroDivisionError:
#     pass
#     print('aaaaa error!')

# with open('less_2_1.txt') as f:
#     for l in f:
#         print(l.strip())
classes_grades = {}
# with open('less_2_1_class_grades.txt') as f:  # my solution
#     for l in f:
#         l.strip()
#         print(type(l),'l=',l, end='')
#         print('len(l)=', len(l))
#         if len(l) == 3:
#             print('len is 2','l=',l, end='')
#             l=l[:-1:]
#             classes_grades[l]=0
#             cl=l  # store name of school class for use in future
#         elif len(l) > 3:
#             i=0
#             summa=0
#             for gr in l:
#                 if gr.isdigit():
#                     summa+=int(gr)
#                     i+=1
#                 else:
#                     continue
#                     classes_grades[cl]=summa/i
#         elif len(l) == 1:
#             pass
# print(classes_grades)

with open('less_2_1_class_grades.txt') as f:  # teacher solution
    for l in f:
        grade=l.strip()
        marks=f.readline()
        marks_list=marks.split()
        # marks_list = [int(x) for x in marks_list]
        # or make with map()
        marks_list=list(map(int, marks_list))
        # print(marks_list)
        aver = sum(marks_list)/len(marks_list)
        classes_grades[grade]=aver
        f.readline()
print(classes_grades)
max_grade=0
max_clas=''
for key, val in classes_grades.items():
    if val > max_grade:
        max_grade=val
        max_clas=key
print('better class is', max_clas, ' | ', 'max grade =', max_grade)

# 1:07:37

with open('result.txt','w') as f:
    for key, val in classes_grades.items():
        f.write(str('Class {} have average grade {}\n'.format(key,val)))

##################################################################################################
# def main():
#################################################################################################
# main()


