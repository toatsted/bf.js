def read(query):
	output = ''

	query = query
	queryIndex = 0
	mem = [0] * 255
	memIndex = 0

	while(queryIndex < len(query)):

		if(query[queryIndex] == '+'):
			mem[memIndex] += 1

			if(mem[memIndex] >= 255):
				memIndex = 0

		elif(query[queryIndex] == '-'):
			mem[memIndex] -= 1

			if(mem[memIndex] <= -1):
				mem[memIndex] = 255

		elif(query[queryIndex] == '>'):
			memIndex += 1

		elif(query[queryIndex] == '<'):
			memIndex -= 1

		elif(query[queryIndex] == '.'):
			output += chr(mem[memIndex])

		elif(query[queryIndex] == ','):
			inp = input('Input requested: ')
			mem[memIndex] = ord(inp[0])

		elif(query[queryIndex] == '['):

			if mem[memIndex] == 0:
				openB = 0
				queryIndex += 1

				while(queryIndex < len(query)):

					if(query[queryIndex] == ']' and openB == 0):
						break

					elif(query[queryIndex] == '['):
						openB += 1

					elif(query[queryIndex] == ']'):
						openB -= 1
					queryIndex += 1

		elif(query[queryIndex] == ']'):

			if(mem[memIndex] != 0):
				closedB = 0
				queryIndex -= 1

				while(queryIndex >= 0):

					if(query[queryIndex] == '[' and closedB == 0):
						break

					elif(query[queryIndex] == ']'):
						closedB += 1

					elif(query[queryIndex] == '['):
						closedB -= 1
					queryIndex -= 1

		queryIndex += 1

	return output

def main():
	f = open(sys.argv[1], 'r')
	query = f.read().rstrip('\n')
	f.close()

	print('\n', read(query), '\n')

if __name__ == '__main__':
	import sys 
	main()
