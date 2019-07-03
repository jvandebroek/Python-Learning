def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "lets do math with functions:" #seems like a sensible thing to do.

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2) #heh

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

print subtract(multiply(divide(add(8,12),10),35),1)
