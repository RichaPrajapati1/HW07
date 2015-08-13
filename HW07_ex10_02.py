# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################

# Write a list of first and last names
#[First Last, First Last, etc]

# def capitalize_nested(list_):
# 	return_list = []
# 	for thing in list_:
# 		if isinstance(thing, list):
# 			return_list.append(capitalize_nested(thing))
# 		else:
# 			return_list.append(thing[0].upper() + thing[1:])
# 	return return_list

def capitalize_nested(list_):
	return[capitalize_nested(thing) if isinstance(thing, list) else thing.capitalize() for thing in list_]
	
##############################################################################
def main():
	# list1 = ['apple', ['bear'], 'cat']
	# print_list = capitalize_nested(list1)
	# print print_list
	pass
	
	
if __name__ == '__main__':
    main()
