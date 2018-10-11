'''	
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Assumption: 
Each input will have exactly one solution, and the same element will not appear twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
#Solution is the single pass, hash table method. Will not work if list contains duplicate numbers.

def twoSum(nums,target):
	#Create an empty dictionary
	items = {}

	for x in range(len(nums)):
		#Get the compliment of the number at the current index
		compliment = target - nums[x]

		#Check if the number at the current index is stored in the dictionary.
		#If found, then the solution to Two Sum is found
		if nums[x] in items.keys():
			found = [items.get(nums[x]), x]
			print(found)
			return found

		#Add the compliment to the dictionary. 
		#Key: Compliment, Value: Index
		items[compliment] = x
	print("Not found")

#Main body
if __name__ == '__main__':
	numbers = [2, 7, 11, 15]
	goal = 9
	twoSum(numbers, goal)