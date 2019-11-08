'''
This program will output the wind chill table for the temp and wind speed
Gene Rocha
10/17/19
'''
import math
def windChill(airTemp,wind):
    # formula from the  National Weather Service
    temp = 35.74 + 0.6215 * airTemp - 35.75 * math.pow(wind,0.16) + 0.4275 * airTemp * math.pow(wind,0.16)
    return temp
#- Rows represent wind speed for 0 to 50 in 5 mph increments.
# - Columns represent temperatures from -20 to +60 in 10-degree increments
def main():
    # create wind speed with range 0 - 50 and increment by 5
    windSpeed = range(0,55,5)
    # create temperatures with range -20 - 60 and increment by 10
    temperatures = range(-20,65,10)
    # print the string Temperature and center
    print("{:^60}".format("Temperature (F)"))
    # loop through the wind speed 
    for wind in windSpeed:
        # change the number 0 to calm and decrease the width so the first temperature will line up with the windchill
        if wind == 0:
            print("{:<2}" .format("calm"), end=" ")
        # for every wind speed above 0 left align and add width of 6
        else:
            print("{:<6}" .format(wind), end=" ")
        # loop through the temperatures
        for temp in temperatures:
            # formula only applies for wind speeds > 3 mph
            if wind < 3:
                # print the temps with right align and width of 5
                print("{:>5}" .format(temp),end=" ")
            else:
                # invoke the windChill function and pass the variables temp and wind
                print("{:>3}".format(round(windChill(temp,wind)))," ",end=" ")
        # print a new line
        print()
main()