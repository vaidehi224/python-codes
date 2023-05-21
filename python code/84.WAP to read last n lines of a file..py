def LastNlines(fname, N):
	with open(fname) as file:
		# loop to read iterate
		# last n lines and print it
		for line in (file.readlines() [-N:]):
			print(line, end ='')

if __name__ == '__main__':
	fname = "file.txt"
	N = 6
	try:
		LastNlines(fname, N)
	except:
		print('File not found')
