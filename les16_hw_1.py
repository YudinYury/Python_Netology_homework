'''lesson_1_6 homework «Разбор алгоритмических задач с собеседований»
решение задач с HackerRank
'''

#TODO 1:
# Read an integer .
# Without using any string methods, try to print the following:  123 ... N
# Note that "..." represents the values in between.
# Input Format:  The first line contains an integer N.
# Output Format:  Output the answer as explained in the task.

n = int(input())
for i in range(1,n+1,1):
    print(i, end='')

# i=1
# while i <= n:
#     print(i, end='')
#     i+=1


