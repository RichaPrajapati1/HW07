# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################

# def is_sorted(list_):
# 	previous = list_[0]
# 	for thing in list_:
# 		if thing < previous:
# 			return False
# 		previous = thing
# 	return True

def is_sorted(list_):
	return all([list_[i] <= list_[i+1] for i in range(len(list_)-1)])



	
##############################################################################
def main():
	# list1 = [1,2,3]
	# print is_sorted(list1)
	pass
	
	
if __name__ == '__main__':
    main()
