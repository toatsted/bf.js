import sys
import bf

f = open(sys.argv[1], 'r')
query = f.read().rstrip('\n')
f.close()

print(bf.read(query))