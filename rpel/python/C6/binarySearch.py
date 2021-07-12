def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	it = 0
	while( first<=last and not found):
		it = it + 1
		mid = (first + last)//2
		if (item_list[mid] == item):
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return [found,mid,it]
	
print(binary_search([1,2,3,5,8,10,14,15,16,17,19,22,24,25,26,28], 26))