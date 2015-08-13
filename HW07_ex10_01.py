# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################

# Write a list of first and last names
#[First Last, First Last, etc]

def nested_sum(list_):
	sum = 0
	for thing in list_:
		if isinstance(thing, list):
			sum += nested_sum(thing)
		else:
			sum += thing
	return sum

	
##############################################################################
def main():
	# list1 = [1,2,[3,4],5]
	# sum_ = nested_sum(list1)
	# #print ("Sum is: %d") %(sum_)
	# print sum_
	pass
	
if __name__ == '__main__':
    main()

