#!/usr/bin/env python3

#----------------------------------------
def joiner(items):
	num_items = len(items)
	if num_items == 0:
		return ''
	elif num_items == 1:
		return items[0]
	elif num_items == 2:
		return ' and '.join(items)
	else:
		items[-1] = ' and ' + items[-1]
		return ', '.join(items)

#----------------------------------------

def main():
	items = []
	
	while True:
		item = input('What {}are you bringing? [q to quit]'.format('else ' if items else ''))
		if item == 'q':
			break
		elif len(item.strip()) > 0:
			if item in items:
				print('You said "{}" already.'.format(item))
			else:
				items.append(item)
				print("We'll have {}.".format(joiner(items.copy())))
	print('Bye.')

#----------------------------------------
if __name__ == '__main__':
	main()
