def leap_y():
    print("")
    year = int(input ("provide the year you would like to check: "))
    if year % 4 == 0:
        print ("This is a leap year")
    else:
        print("This is not a leap year")
        print("\n")

leap_y()
