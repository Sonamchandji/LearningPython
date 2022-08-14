# To check if a given year is leap year or not!

# A given year will be leap year if its a century year and divided by 400 or if it is not a century year then divided by 4!

# Display message to user for input year to be checked

year=int(input("Enter a year to be checked, please! "))
print("Checking if given year {} is leap year".format(year))

# To check if year is century year & a leap year

if (year%100 == 0) :
    if (year%400 == 0):
       print("The year {} is leap year as it is divide by 400. ".format(year))
    else:
        print("The given year {} is not a leap year as it is divide by 100 but not by 400 ".format(year))

# To check if its not century year but still a leap year
elif (year % 4 ==0):
    print("The given year {} is a leap year as it is divided by 4 but not by 100 and 400".format(year))

# Display that year is not a leap year
else:
    print("The given year {} is not a leap year as it is neither divided by 4 and nor by 100 & 400".format(year))


#

#

#