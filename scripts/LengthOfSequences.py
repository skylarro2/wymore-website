import sys

if len(sys.argv) != 2:
	print("ARGUEMENTS: input_file")
	exit()

f = open(sys.argv[1],"r")

text = f.readlines()

for t in text:
    if t[0] != '>':
        print(len(t))
