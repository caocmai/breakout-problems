''' Given a list of n numbers, determine if it contains any duplicate numbers.
list = [2, 6, 4, 7, 6] -> True
set()
loop through the list for each number
	check to see if number in the set, if not in set add to set
	else if number is in the set 
		return True
return False because not in set.
'''

list_of_numbers = [2, 6, 4, 7, 6]

new_set = set()
for number in list_of_numbers:
	if number not in new_set:
		new_set.add(number)
	else:
		return True
return False
