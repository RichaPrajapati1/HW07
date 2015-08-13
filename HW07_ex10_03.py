# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################

# Write a list of first and last names
#[First Last, First Last, etc]

# def cumulative_sum(list_):
# 	retun_list = []
# 	first = 0
# 	second = 0
# 	for thing in list_:
# 		second = first + thing
# 		retun_list.append(second)
# 		first = second
# 	return retun_list

def cumulative_sum(list_):
	return [sum(list_[:i+1]) for i in range(len(list_))]
	
##############################################################################
def main():
	# list1 = [1,2,3]
	# print_list = cumulative_sum(list1)
	# print print_list
	pass
	
if __name__ == '__main__':
    main()
