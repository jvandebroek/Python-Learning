name = 'Zed A. Shaw'
age = 35 
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = height * 2.54
weight_kilo = weight*0.453592

print "Let's talk about %s." % name
print "He's %d inches tall %d cm." % (height, height_cm)  #d = number
print "He's %d pounds heavy %d kilo." % (weight, weight_kilo)
print "Actually that's not too heavy."   
print "He's got %s eyes and %s hair." % (eyes, hair)  #s = string
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print "hello %r hello %r" % (age, name)
