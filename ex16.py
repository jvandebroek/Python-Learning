from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') #W = write mode, as opposed to r, x, a, t, b
print "truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "im going to write these to the file."

target.write((line1 + "\n"))  #
target.write((line2 + "\n"))  # I combined a few lines here...
target.write((line3 + "\n"))  # could have had it all in one line infact.

print "and finally we close it."
target.close()
