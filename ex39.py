ten_things = "Apples Oranges Crows Telephone Light Sugar" 
print "Wait there's not 10 things in that list, lets fix that"
stuff = ten_things.split(' ')
more_stuff = ['day', 'night', 'song', 'Frisbee', 'Corn', 'banana', 'girl', 'boy']

while len(stuff) < 10: #really dont like while x != y leaves a lot of room for error -> infi loop
    next_one = more_stuff.pop()
    print "adding: ", next_one
    stuff.append(next_one)
    print "there's %d items now" % len(stuff)

print "there we go: ", stuff
print "lets do some things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
