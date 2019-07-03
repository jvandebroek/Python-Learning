from sys import argv

script, filename = argv  #sets variable names to each input from argv

txt = open(filename) #Defines variable "txt" as the file given earlier

print "Here's your file %r:" % filename  
print txt.read()   #Does "read" on the txt file and prints its contents

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt.close()
txt_again.close()
