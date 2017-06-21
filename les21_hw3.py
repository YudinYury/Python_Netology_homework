'''lesson_1_6 homework «Разбор алгоритмических задач с собеседований»
решение задач с HackerRank
'''

#TODO 1:
# Task: Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
# Input Format
# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .
# Output Format: Print the result of hash(t).

# n = int(input())
# integer_list = list(map(int, input().split()))
# t=tuple(integer_list)
# # print(t)
# # print(type(t),t)
# print(hash(t))

#TODO 2:
# Let's learn about list comprehensions! You are given three integers X,Y and Z  representing the dimensions of a cuboid
# along with an integer N. You have to print a list of all possible coordinates given by  (i,j,k)  on a 3D grid where
# the sum of i+j+k  is not equal to N. Here, 0 <= i <= X;  0 <= j <= Y;  0 <= k <= Z
# Input Format:  # Four integers  and  each on four separate lines, respectively.
# Print the list in lexicographic increasing order.
pass
############################################################################################################
TODO 3:
# You are given  numbers. Store them in a list and find the second largest number.
# Input Format:  The first line contains N. The second line contains an array A[] of N  integers each separated by a space.
# Constraints:  2 <= N <=10,   -100 <= A[i] <= 100
# Output Format: Output the value of the second largest number.

n = int(input())
# n=5
arr = list(map(int, input().split()))
second=-1000
max_n=-999
for i in range(n):
    # print('arr[i] =', arr[i], 'max_n =', max_n, 'second =', second, '  =>  ', end='')
    if arr[i] > max_n:
        second=max_n
        max_n=arr[i]
    elif arr[i] > second and arr[i] < max_n:
        second=arr[i]
    # print('max_n =', max_n, 'second =', second)
print(second)

#############################################################################################################

#TODO 4:
# Given the names and grades for each student in a Physics class of N students, store them in a nested list and print
# the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.
# Constraints:
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.
# Output Format: Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple
# students, order their names alphabetically and print each one on a new line.

for _ in range(int(input())):
        name = input()
        score = float(input())


#############################################################################################################

