'''
This program calculates a speeding ticket based on the speed limit
1. get the speed limit
2. get the clocked speed
3. Calculate the speeding ticket
4. return the result
Gene Rocha
11/7/2019
'''
# get the speed limit from the input and return
def speedLimit():
    speed = int(input("Enter the speed limit:"))
    return speed
# get the recored speed form the input and return
def recordedSpeed():
    clockedSpeed = int(input("Enter the clocked speed:"))
    return clockedSpeed
# Podunksville speeding amounts
# $50 and $5 for each mph over the limit
# $200 for any speed over 90 mph
# calculate the speeding ticket
def calculateSpeedTicket():
    ticket = ""
    # invoke the function speedLimit
    speed = speedLimit()
    # invoke the function recordedSpeed
    clockedSpeed = recordedSpeed()
    speedDif = clockedSpeed - speed
    if clockedSpeed > speed:
        if clockedSpeed < 90:
            ticket = ((speedDif * 5) + 50)
        else: 
            ticket = ((speedDif * 5) + 250)
    return ticket
# invoke the function calculateSpeedTicket and return the print the result
def main():
    ticket = calculateSpeedTicket()
    if ticket:
        print("The amount of the speeding ticket is ${0:0.2f}".format(ticket))
    else:
        print("The clocked speed was legal and a speeding ticket should not be issued")
main()
