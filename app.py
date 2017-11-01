
def find(ordered_list, element_to_find):
	for element in ordered_list:
		if element == element_to_find:
			return True
		return False

if __name__ == "__main__":
	num_list = [2, 4, 5, 6, 8, 10, 25]
	print(find(num_list, 1)) # prints False
	print(find(num_list, 2)) # prints True
	print(find(num_list, 5)) # prints True
	print(find(num_list, 9)) # prints False
	print(find(num_list, 8)) # prints True