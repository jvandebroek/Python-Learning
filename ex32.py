hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]
change = ['pennies', 1, 2, 'quarters', 700]

for x in weights:
    print "this is weight %d" % x

for y in eyes:
    print "this is color %s" % y

for x in change:
    print "this is change %r" % x

elements = []

for i in range(6):
    print "adding %d to the list." % i
    elements.append(i)

for i in elements:
    print "Element was: %d" %i

elementz = range(10)
for p in elementz:
    print p
