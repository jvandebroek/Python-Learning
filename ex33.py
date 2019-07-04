
def counting_to(x):   
    i = 0
    numbers = [] 
    while i < x+1:
        print "at the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "the numbers: "

    for num in numbers: 
        print num

counting_to(10)
counting_to(3)

