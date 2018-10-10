'''

Merge two sorted linked lists and return it as a new list. The new list should be made by 
splicing together the nodes of the first two lists. The function must also handle when empty
linked lists are given.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

#Working code, but needs a main body to run tests. Didn't feel like building some linked lists
#to try it out, but it passed Leetcode

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def mergeTwoLists(l1, l2):

	if l1 == None and l2 == None:
		return None
	elif l1 == None:
		return l2
	elif l2 == None:
		return l1

	if l1.val < l2.val:
		new_list = ListNode(l1.val)
		l1 = l1.next
	else:
		new_list = ListNode(l2.val)
		l2 = l2.next

	#Crawler and new_list have the same address in memory.
	crawler = new_list

	while l1 != None and l2 != None:
		if l1.val < l2.val:
			crawler.next = l1
			l1 = l1.next
			crawler = crawler.next
		else:
			crawler.next = l2
			l2 = l2.next
			crawler = crawler.next

	if l1 == None:
		crawler.next = l2
	if l2 == None:
		crawler.next = l1

	return new_list