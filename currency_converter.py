def main():
    print("This program converts us dollars to Pound Sterling")
    print("")
    dollars = float(input("Please enter amount in usd: "))
    #pounds = convert_to_pounds (dollars)
    pounds = (lambda dollars: dollars * 0.82)(dollars)
    print(f"That will give you {pounds:.2f} pounds")
    print("")

#def convert_to_pounds(dol):
#    return dol * 0.82

#convert_to_pounds = lambda dollars: dollars * 0.82

main()