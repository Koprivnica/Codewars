"""
There is a bus moving in the city which takes and drops some people at each bus stop.
You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus
(the first item) and the number of people that get off the bus (the second item) at a bus stop.
Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is
the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D
Take a look on the test cases.
Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't
be negative.
The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.
"""



def calc_num_of_people(bus_stops):
    
    # The function calculates the difference between people who enter the bus and people who exit the bus for every station.
    # The sum of all this differences is the final number of people in the bus.
    
    return sum(on - off for on, off in bus_stops)
