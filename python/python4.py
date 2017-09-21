cars = 100 #Sets car variable to 100
space_in_a_car = 4.0 #Sets s pace_in_a_car variable to 4.0
drivers = 30 #Sets driver variable to 30
passengers = 90 #Sets Passengers variable to 90
cars_not_driven = cars - drivers #variable created to find out the amount of
#cars not driven
cars_driven = drivers #Creates a new variable and sets the value to the same as
#drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "Cars avaiable."
print "There are", drivers, "Drivers available."
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
