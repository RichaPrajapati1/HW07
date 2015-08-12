# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################

# Write a list of first and last names
#[First Last, First Last, etc]

def is_sorted(list_):
	previous = list_[0]
	for thing in list_:
		if thing < previous:
			return False
		previous = thing
	return True

	
##############################################################################
def main():
	# list1 = ['apple', 'bear', 'cat']
	# print is_sorted(list1)
	pass
	
	
if __name__ == '__main__':
    main()
