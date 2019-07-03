from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "first print the whole file:\n"
print_all(current_file)
print "now rewind"
rewind(current_file)
print "lets print 3 lines"
for x in range(3):  #I went ahead and google how to do a for loop in python here to avoid excess typing...
    current_line = x+1
    print_a_line(current_line, current_file)
