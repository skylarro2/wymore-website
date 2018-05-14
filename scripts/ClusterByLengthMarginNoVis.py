import sys

if len(sys.argv) != 5:
	print("ARGUMENTS NEEDED: input_file output_file min_length max_length")
	exit()

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])
min_length = int(sys.argv[3])
max_length = int(sys.argv[4])

in_file = open(input_file,"r")
out_file = open(output_file,"w")

text = in_file.readlines()

count = 0
identifier = ''
for t in text:
	if t[0] == '>':
		identifier = t
	elif min_length <= len(t) and len(t) <= max_length:
		out_file.write(identifier)
		out_file.write(t)
		count += 1

out_file.close()		
print "NUMBER OF SEQUENCES OUTPUT: ", count       
