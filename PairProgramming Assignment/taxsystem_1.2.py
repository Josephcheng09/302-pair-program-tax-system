import sys
import tkinter
import math


basic_tax_reduction = int(132000)#
mpf_reduction = int()
tax = int()
income = int()
x = int()


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def calculate_mpf_reduc(income_input):

    if (income_input >= 30000*12): #MPF reduction for more than $30000/month
        mpf_reduction = 18000
    elif (income_input < 7100*12): #MPF reduction for less than $7100/month
        mpf_reduction = 0
    else: 
        mpf_reduction = (income_input *0.05)  #MPF reduction for least than $30000/month
    print("MPF reduction:", mpf_reduction)
    return mpf_reduction

def net_income(income_input):
    income = income_input - calculate_mpf_reduc(income_input) - basic_tax_reduction
    #print(income)
    return income

def tax(income):
    while True:
        try:# print(income)
            if (income <= 0):
                tax = 0
                
            elif (income > 0) and (income <= 50000):#income in the range of in the first $50000
                tax = (0.02*income)

            elif (income > 50000) and (income <= 100000):#income in the range of the next $50000
                tax = 1000 + (0.06*((income-50000)))
            
            elif (income > 100000) and (income <= 150000):#income in the range of the second next $50000
                tax = 1000 + 3000 + (0.1*((income-100000)))
                
            elif (income > 150000) and (income <= 200000):#income in the range of the third next $50000
                tax = 1000 + 3000 + 5000 + (0.14*((income-150000)))

            else: #income over the third next $50000
                tax = 1000 + 3000 + 5000 + 9000 + (0.17*((income-200000)))
            return tax
        except TypeError:
            print ("Error")
            break

def tax41():
    #tax calculation for single and test the program is working or not 
    income_input = int(input("Enter your annual income:"))
    income = net_income(income_input)
    x = tax(income)
    print("-------result-------")
    print("Annual Income:", income_input)
    print("Net Income:", income)
    print("Tax payable by you:", x)
    print("-------END-------")

    
def tax42():#tax calculation for two
    input1 = int(input("Enter the first person annual income:"))
    input2 = int(input("Enter the second person annual income:"))
    income = net_income(input1)
    x = tax(income)
    print("-------result of the first person-------")
    print("Annual Income of the first person:", input1)
    print("Net Income of the first person:", income)
    print("Tax payable by the first person:", x)
    x1 = income
    x2 = x
    '''
    the result of the first person
    --------------
    the result of the second person
    '''
    print("-------result of the second person-------")
    income = net_income(input2)
    x = tax(income)
    print("Annual Income of the second person:", input2)
    print("Net Income of the second person:", income)
    print("Tax payable by the second person:", x)
    x1 += income
    x2 += x
    x1 = tax(x1)
    print("-------recommendation-------")
    print("Seperate Payment:", x2)
    print("Joint Payment:", x1)
    
    if x1 > x2:#recommendation
        print("Seperate Payment is better")
    elif x1 < x2:
        print("Joint Payment is better")
    else:
        print("both are okay")
    
    print("-------END-------")
def main():
    instructions = """Please select your marital status by entering one of the following:
       1 to select Single 
       2 to select Married
       Q to end \n"""

    while True:
        print (instructions)#menu  
        choice = input( "Enter your choice:" ) 

        if choice == "1":
            tax41()
        elif choice == "2":
            tax42()
        elif choice == "Q" or "q":
            print ("You quit the Tax System")
            exit()

        else:
            sys.stderr.write("\nWrong input, please try again\n")



if __name__ == "__main__":
    main()
