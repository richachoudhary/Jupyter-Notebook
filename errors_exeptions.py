try:
	f = open('testfile', 'r')
	f.write('Test this file')
except IOError:
	print('Error: Could not find the file or write data')
else:
	print('No Error in Code')
finally:
	print('Executing finally clause.')
