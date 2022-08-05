def skip_elements(elements):
	# code goes here
	new_list = []
	for count, value in enumerate(elements):
		if count % 2 == 0:
			new_list.append(value)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']