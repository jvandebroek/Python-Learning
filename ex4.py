cars = 100
space_in_a_car = 4.0 #using 4.0 here as opposed to 30.0 for drivers (a number used for division) is strange to me.
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven  #interestingly if we had 119 passengers this would still suggest
                                                       #that we need 3/car when really it would be closer to 4/car

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#explanation of error: the coder did not define car_pool_capacity before calling to it on line 8.


