'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

===================================================

Note to self. Python returns "index out of bounds" while using [-1] on an empty list.
Had to use a slice to check the top of the stack, hence why checking for parenthesis
is done inside lists

'''

def isValid(s):
	if s == "":
		return print("String empty")
	stack = []
	for x in range(len(s)):
		if (not stack) and (s[x] == ")" or s[x] == "}" or s[x] == "]"):
			print("False")
			return False
		elif (s[x] == ")") and (stack[-1:] == ["("]):
			stack.pop()
		elif (s[x] == "}") and (stack[-1:] == ["{"]):
			stack.pop()
		elif (s[x] == "]") and (stack[-1:] == ["["]):
			stack.pop()
		else:
			stack.append(s[x])
	if not stack:
		print("True")
		return True
	else:
		print("False")
		return False

#Main body
if __name__ == '__main__':
	parenthesis = ["()", "({[]})","[", "(", "{", "[[[{{{((()))}}}]]]", "[[",""]
	for x in range(len(parenthesis)):
		isValid(parenthesis[x])

'''
Should return:
True
True
False
False
False
True
False

'''
	