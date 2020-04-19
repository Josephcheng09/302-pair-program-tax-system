
income_input = {}

for key in income_input.keys():
    income_input[key] = income

def calculate_tax(income_input):

    if (income >= 0) and (income <= 1000):
        tax = (0*income)

    elif (income > 1000) and (income <= 10000):
        tax = (0.1 * (income-1000))

    elif (income > 10000) and (income <= 20200):
        tax = ((0.1*(10000-1000)) + (0.15*(income-10000)))

     elif (income > 20200) and (income <= 30750):
        tax = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(income-20200)))

    elif (income > 30750) and (income <= 50000):
        tax = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(income-30750)))

    elif (income > 50000):
        tax = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(50000-30750)) + (0.3*(income-50000)))   
    else:
        pass

    for key in income_input.keys():
        income_input[key] = tax

    return tax