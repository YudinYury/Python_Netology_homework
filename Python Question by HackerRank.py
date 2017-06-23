''' решение задач с HackerRank
'''

#TODO 2:
# CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
# Specifications of HEX Color Code
#
# ■ It must start with a '#' symbol.
# ■ It can have  3 or 6  digits.
# ■ Each digit is in the range of 0  to F. (1,...,9,0,A,B,C,D,E and F).
# ■  A-F letters can be lower case. (a,b,c,d,e and f are also valid digits).
# Valid Hex Color Codes
# #FFF
# #025
# #F0A1FB
# Invalid Hex Color Codes
# #fffabg
# #abcf
# #12365erff
# You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
# CSS Code Pattern
# Selector
# {
# 	Property: Value;
# }
# Input Format
# The first line contains N, the number of code lines.
# The next N lines contains CSS Codes.
# Constraints  0 < N < 50
# Output Format: Output the color codes with '#' symbols on separate lines.
# Sample Input
# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }
# Sample Output
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff

# ss_list=[
#     '#BED',
#     '{',
#     '    color: #FfFdF8; background-color:#aef;',
#     '    font-size: 123px;', '',
#     '}',
#     '#Cab',
#     '{',
#     '    background-color: #ABC;',
#     '    border: 2px dashed #fff;',
#     '}'
# ]
# sstr='#BED{    color: #FfFdF8; background-color:#aef;    font-size: 123px;}#Cab{    background-color: #ABC;    border: 2px dashed #fff;}'

signature_list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
hex_list=[]  # список для результата
# n = int(input())
n=11
ss=''
it=0
body_of_tag=0
for ss in ss_list:
    step = 0
    if ss.find('{') != -1:
        body_of_tag=1
        # print('Вошли в тело')
        continue
    if ss.find('}') != -1:
        body_of_tag=0
        # print('Вышли из тела')
        continue

    while body_of_tag:
        it=ss.find('#',it,)
        if it == -1:
            it=0
            break
        it+=1
        # print('begin find in ', ss[it::1])
        new_num_str = '#'

        for single in ss[it::1]:
            if single.lower() in signature_list:
                new_num_str+=single
                # print('new_num_str=',new_num_str)
            else:  # закончился порядок цифр (0...9, A...F)
                # print('end of find')
                it += len(new_num_str)  # пропускаем уже проверенную строку и дальше будем искать с нового места
                step += len(new_num_str)
                # print('it=', it, ' ss()=',ss[it::1])
                # print('body_of_tag =', body_of_tag)

                if len(new_num_str)==4 or len(new_num_str)==7:
                    hex_list.append(new_num_str)
                    # print('hex_list', hex_list)
                    new_num_str = ''
                    break
                else:
                    new_num_str=''
                    break

for out in hex_list:
    print(out)


