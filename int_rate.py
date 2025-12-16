# principal amt, interest rate(pa), tenure (years)
#calculate the monthly repayment
#M = P * R / 1- (1+r)^n
#rpa = monthly rate = rate per annum / 12

def main():
    print ("This is a monthly loan repayment calculator")
    print ("")

    principal = float(input("How much is the loan amount? "))
    rate = float(input("what is the interest rate? "))
    tenure = int(input ("What is the tenure of the loan? "))
    rpa = rate/1200
    number_of_months = tenure * 12
    numerator = rpa * (1 + rpa) ** number_of_months
    #numerator = rpa * ((1 + rpa) ** number_of_months)
    denominator = ((1 + rpa) ** number_of_months) -1
    monthly_payment_amount = principal * numerator / denominator
    #monthly_payment_amount = principal * rpa / (1 - (1 + rpa) ** (-number_of_months))

    #print("Your monthly payment amount is: %.2f " % monthly_payment_amount)
    print(f"Your monthly payment amount is: {monthly_payment_amount:.2f}")

main()

"""
    numerator = rpa (1 + rpa) ** number_of_months
    denominator = ((1 + rpa) ** number_of_months) -1
    monthly_payment_amount = principal * numerator / denominator

    """

