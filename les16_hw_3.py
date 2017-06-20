'''lesson_1_6 homework «Разбор алгоритмических задач с собеседований»
решение задач с HackerRank
'''

#TODO 3:
# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Input Format
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
# Constraints
# The elements added to the list must be integers.
#
# Output Format
# For each command of type print, print the list on a new line.

our_list = []
# N = int(input())
N=12
for cmd in range(N):
    cmd_str=input()
    if cmd_str.find('insert') == 0:
        it=cmd_str.find(' ')
        it+=1
        print(cmd_str[it])
        # print('Вошли в тело')
        continue
    if cmd_str.find('print') == 0:
        print(our_list)
        continue
    if cmd_str.find('remove') == 0:
        continue
    if cmd_str.find('append') == 0:
        continue
    if cmd_str.find('sort') == 0:
        continue
    if cmd_str.find('pop') == 0:
        continue
    if cmd_str.find('reverse') == 0:
        continue
    if cmd_str.find('') == 0:
        continue
    if cmd_str.find('') == 0:
        continue
    if cmd_str.find('') == 0:
        continue
    if cmd_str.find('') == 0:
        continue


# si=sstr.find('#')
# if si==-1:
#     print('Not found "#"')
#     exit()
# hex_num_str=''
# for ch in sstr:
#     print(ch)
#     if not ch.isdigit():
#         continue
#     if

