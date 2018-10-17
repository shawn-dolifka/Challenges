'''
This program takes a sentence and reverses the order of the words in it
"I am Sam" will become "Sam am I"
'''

def string_reverse(string):
	stack = []
	reverse = string.split()
	for x in range(len(reverse)):
		stack.append(reverse[x])
	reverse_word = ''
	while stack:
		reverse_word = reverse_word + " " + stack.pop()
	return reverse_word[1:]

if __name__ == '__main__':
	test_string = "I want a cookie"
	print(test_string)
	test_string = string_reverse(test_string)
	print(test_string)
