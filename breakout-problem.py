'''  
Question: Given a list of n numbers, determine if it contains any duplicate numbers.

1 (Restate). So for this problem I need to create a function that takes in a list of numbers and returns True
if any number in the list appears twice and False otherwise?
2 (Clarify). Should I return the actual number or just a Boolean? Is the list sorted? Are the numbers an int or float?
3 (Assumptions). I assume that the function takes in one input, which is a list of numbers, and return a Boolean. 
4 (Solutions). For this problem, I guess you could solve it by brute force and just loop through each number and checking
it against all the other numbers and see if they match; if they match then return True, and False otherwise. 
The time complexity for that would be quite slow, to the order of 0(n^2).

To solve this problem in linear time where I only have to loop through the numbers array once would be to maybe to 
create a set and check to see if the number is not in the set then I add it to the set and keep going down the
numbers array. However, if the number in the numbers array is found in the set, which mean that we have seen
that number before, and return True. Since we only need to loop throught the array once the time complexity is linear
which is 0(n)

input 						output
list = [2, 6, 4, 7, 6] -> 	True
list2 = [2, 6, 4, 7, 3] -> 	False

Pseudocode:
create set()
loop through the list for each number
	check to see if number in the set
		if not in set add to set
	else if number is in the set 
		return True
return False because not in set.


'''

list_with_duplicate = [2, 6, 4, 7, 6]
list_without_duplicate = [2, 6, 4, 7, 3]

### First attempt
# new_set = set()
# for number in list_of_numbers:
# 	if number not in new_set:
# 		new_set.add(number)
# 	else:
# 		return True
# return False


### Improved attempt
def if_duplicate(a_list):
	unique_set = set()
	for number in a_list:
		if number in unique_set:
			return True
		unique_set.add(number)
	return False

print(if_duplicate(list_with_duplicate)) # Should return True
print(if_duplicate(list_without_duplicate)) # SHould return False


"""
Question: Find the longest substring of unique letters in a given string of n letters.

1 (Restate). I will be given a string and I should return the longest substring in that given string that has 
all unique letters.
2 (Clarify). Should I return the actual string or just the length of the longest substring?
3 (Assumptions). I assume that the function takes in one input, which is a string a returns a string also
4 (Solutions). I think to solve this it's probably a good idea to loop through the string and only add string 
to a new list that contains only unique characters. If the new list encounters a letter that it has already seen
then the new list should reset and repeat the process.

input 					output
string = "abcababab" -> 	abc
string2 = "wpwkwwaaw -> 	pwk

Pseudocode
loop through the string 
	if letter not found in new array, add to it
	if letter is found in new array, it's seen before so start the new array at the from the point where seen letter 
	to the end of the new array
	find the length of the new array, and compare to a new variable called max length, starting at 0, and set the length
	of the new array as the max length, and updating max length every time. 
	
	also check to see if the max length is equal to the length of the new array, if so then make a copy of that array
	to be return as the array with the substring
return the longest unique substring


"""
def find_unique_subtring(string):
	unique_string = []
	max_length = 0

	for letter in string:
		if letter in unique_string:
			unique_string = unique_string[unique_string.index(letter)+1: ] # Set the unique string to start after the found letter

		unique_string.append(letter)
		max_length = max(max_length, len(unique_string))

		

	return unique_string


print(find_unique_subtring("wpwkwwaaw"))
