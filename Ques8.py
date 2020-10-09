def check_int(l):
	for i in range(0, len(l),1):
		if not l[i].isnumeric():
			return False
	return True

def count_odd(l):
	if check_int(l):
		count = 0
		for i in range(0,len(l),1):
			if int(l[i]) % 2 != 0:
				count += 1
		print("The NO. of ODD Number is: ", count)

def largest_str(l):
	flag = True
	for i in range(0, len(l), 1):
		if type(l[i]) != str:
			flag = False
			
	if flag:
		largest = l[0]
		for i in l:
			if len(i) > len(largest):
				largest = i
		print("Largest string: ", largest)
	else:
		print("List does not contain all strings!")	

def display_reverse(l):
	for i in range(len(l)-1, -1, -1):
		print(l[i], end=" ")
	return


def find_item(l):
	item = input("\nEnter an element: ")
	for i in range(0, len(l), 1):
		if item == l[i]:
			print("Item found at index: ", i)
			return
	print("Item not found")


def remove_item(l):
	item = input("\nEnter an element: ")
	for i in range(0, len(l), 1):
		if item == l[i]:
			l.remove(item)
			print("Item removed")
	return


def sort_desc(l):
	print(sorted(l, reverse=True))
	return
	

def common(l1, l2):
	common = []
	for i in range(0, len(l1), 1):
		for j in range(0, len(l2), 1):
			if l1[i] == l2[j]:
				common.append(l1[i])
	if common:
		print("Common elements: ", common)
	else:
		print("No common element")
	return
	
def main(l):
	print("\n Menu")
	print("Press 1 for Checking If all Numbers are INTEGERS:")
	print("Press 2 for Counting the Odd Numbers if list is Numeric:")
	print("Press 3 for Display the Largest String:")
	print("Press 4 for List Reverse:")
	print("Press 5 for Finding Items in List:")
	print("Press 6 to Remove Items from List")
	print("Press 7 for Sorting List in Descending Order")
	print("Press 8 for Finding the common Elements fron Another List")
	print("Press 9 for EXIT")
	option = input("You Pressed: ")
	switcher = {
        '2' : count_odd,
        '3' : largest_str,
        '4' : display_reverse,
        '5' : find_item,
        '6' : remove_item,
        '7' : sort_desc,
        '8' : common,
        '9' : quit
    }
	if option == '1':
		if check_int(l):
			print("All elements are numbers")
		else:
			print("All elements are not numbers")
	elif option == '8':
		l2 = []
		n = int(input("Enter the size of new list: "))
		for i in range(0, n, 1):
			l2.append(input("Enter element: "))
			common(l, l2)
	else:
		func = switcher.get(option, lambda: print("Invalid Choice!"))
		func(l)

if __name__ == "__main__":
	l = []
	n = int(input("Enter the size of list: "))
	for i in range(0, n,1):
		l.append(input("Enter element: "))
	ch = 'y'
	while ch.lower() == 'y':
		main(l)
		ch = input("\nWant to continue? [y/n]: ")
