import math

#printing initial message for investment or bond calculation options available
print('''
Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a home loan''')


invest_or_bond = input("Enter either investment or bond from the menu above to proceed: ")

# get a lower case text of the input. Allows whatever input capitalised or not to be recognised as long as spelled correctly
invest_or_bond_lower_case = invest_or_bond.lower()

# check if it's investment
if invest_or_bond_lower_case == "investment":
    print("You chose Investment...")
    deposit_ask = int(input("Please enter the amount you would like to invest: "))
    interest_ask = int(input("Please enter interest rate of your investment: "))
    years_ask = int(input("Please enter how many years you are planning to invest for: "))
    interest = input("Please choose if you want to calculate simple or compound interest: ")

    #calculate simple interest using formula given, A = P*(1+r*t)
    if interest == "simple":
        r = interest_ask / 100
        calc_simple = deposit_ask*(1+r*years_ask)
        simple_interest_state = "Your investment using simple interest after {} years with {} % interest rate will be:  "
        print(simple_interest_state.format(years_ask, interest_ask) + str(round(calc_simple,2)))
        #Used .format(,) to add more information into printed statement to make easier to understand for reader
        #added round() to 2 places, makes more sense as output is currency

    #calculate compound interest using formula given, A = P * math.pow((1+r),t)
    elif interest == "compound":
        r =interest_ask /100
        calc_compound = deposit_ask * math.pow((1+r),years_ask)
        compound_interest_state = "Your investment using compound interest after {} years with {} % interest rate will be:  "
        print(compound_interest_state.format(years_ask, interest_ask) + str(round(calc_compound,2)))

        #else for error message in simple/compound choice input
    else: print("Please input only 'simple' or 'compound' to calculate your answer.")

# check if it's bond
elif invest_or_bond_lower_case == "bond":
    print("You chose Bond...")
    present_value = int(input("Please enter the present value of the house: "))
    interest_ask = int(input("Please enter the interest rate: "))
    month_interest = (interest_ask/100)/12
    months_bond = int(input("Please enter how many months you are planning to pay off bond: "))

    #Calculate with bond repayment formula,  repayment = (i * P)/(1 - (1 + i)**(-n)), then print
    bond_calc = ((month_interest * present_value) / (1 - (1 + month_interest)**(-months_bond)))
    bond_statement = "The amount you should pay each month for {} months is: "
    print(bond_statement.format(months_bond) + str(round(bond_calc,2)))
    ''' For printed amount of bond calc I used round() to two places 
         to make answer more readable and more functional as it is a currency
         I used https://www.w3schools.com/python/ref_func_round.asp for round function instruction.'''

# use else function for error message
else:
    print("Error: Please input only investment or bond.")
