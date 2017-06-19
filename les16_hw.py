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


#TODO 2:
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have  3 or 6  digits.
■ Each digit is in the range of 0  to F. (1,...,9,0,A,B,C,D,E and F).
■  A-F letters can be lower case. (a,b,c,d,e and f are also valid digits).

Valid Hex Color Codes
#FFF
#025
#F0A1FB

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff

You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern
Selector
{
	Property: Value;
}

Input Format
The first line contains N, the number of code lines.
The next N lines contains CSS Codes.

Constraints
0 < N < 50

Output Format
Output the color codes with '#' symbols on separate lines.

Sample Input
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}
Sample Output
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
#############################################################################################################
#TODO 3:

#############################################################################################################

#TODO 4:

#############################################################################################################

