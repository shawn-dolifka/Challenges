'''
Given a 32-bit signed integer, reverse digits of an integer.

=======================

Example 1:

Input: 123
Output: 321

=======================

Example 2:

Input: -123
Output: -321

=======================

Example 3:

Input: 120
Output: 21

Assume we are dealing with an environment which could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume 
that your function returns 0 when the reversed integer overflows.

=======================

This solution's logic only works in Python. Size of "Int" in Python is unlimited. In C++, Java, etc.,
reversing 2,147,483,647, then trying to convert to an "int" type would cause an overflow

'''

def reverse(x):
	x_string = str(x)
	num_list = list(x_string)
	reverse = ''
	while len(num_list) != 0:
		if num_list[-1] == '-':
			reverse = num_list.pop() + reverse 
			continue
		reverse = reverse + num_list.pop()
	reverse = int(reverse)
	if reverse > 2147483647 or reverse < -2147483647:
		print('0')
		return 0
	else:
		print(reverse)
		return reverse

#Main body
if __name__ == '__main__':
	numbers = [123, -123, 120, 2147483647, -2147483647]
	for x in range(len(numbers)):
		reverse(numbers[x])

'''
Expect the answers"
321
-321
21
0
0
'''