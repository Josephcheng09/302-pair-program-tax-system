import sys
import tkinter
import math


basic_tax_reduction = int(132000)#allow change 4 future
mpf_reduction = int()
tax = int()
income = int()
x = int()

def inputNumer(message):
    while True:
        try:
            usersinput = int(input(message))
        except ValueError:
            print("Please input number")
            continue
        else:
            return usersinput
            break

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
        mpf_reduction = (income_input *0.05)  #MPF reduction for $7100 - $30000/month
    print("MPF reduction:", mpf_reduction)
    return mpf_reduction

def net_income(income_input):
    income = income_input - calculate_mpf_reduc(income_input) - basic_tax_reduction
    #print(income)
    return income

def net_incomes(income_input):#standard
    incomes = (income_input - calculate_mpf_reduc(income_input))*0.15 
    return incomes

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
                tax = 1000 + 3000 + 5000 + 7000 + (0.17*((income-200000)))
            return tax
        except TypeError:
            print ("Error")
            break

def tax41():
    #tax calculation for single and test the program is working or not 
    income_input = inputNumer("Enter your annual income:")
    print("-------Result-------")
    income = net_income(income_input)
    x = tax(income)
    print("Annual Income:", income_input)
    if income <=0 :
        print ("Net Income: 0")
    else:
        print("Net Income:", income)
    print("Progressive rate tax Payable by You:", x)
    s = net_incomes(income_input)
    print("Standard rate tax Payable by You:", s)
    if x >s:#recommendation
        print("Standard rate is better")
    else:
        print("Progressive rate is better")

    print("\n-------END-------\n")

    
def tax42():#tax calculation for two
    input1 = inputNumer("Enter the first person annual income:")
    input2 = inputNumer("Enter the second person annual income:")
    print("-------Result of the first person-------")
    income = net_income(input1)
    x = tax(income)
    print("Annual Income of the first person:", input1)
    if income <=0 :
        print ("Net Income of the first person: 0")
    else:
        print("Net Income of the first person:", income)
    print("Progressive rate tax payable by the first person:", x)
    s = net_incomes(input1)
    print("Standard rate tax payable by the first person:", s)
    x1 = income
    x2 = x
    s1 = s
    '''
    the Result of the first person
    --------------
    the Result of the second person
    '''
    print("-------Result of the second person-------")
    income = net_income(input2)
    x = tax(income)
    print("Annual Income of the second person:", input2)
    if income <=0 :
        print ("Net Income of the second person: 0")
    else:
        print("Net Income of the second person:", income)
    print("Progressive rate tax payable by the second person:", x)
    s = net_incomes(input2)
    print("Standard rate tax payable by the second person:", s)
    x1 += income#Joint
    x2 += x#Seperate
    x1 = tax(x1)
    s1 += s
     
    
    print("-------Recommendation-------")
    print("Progressive rate - Seperate Payment:", x2)
    print("Progressive rate - Joint Payment:", x1)
    print("Standard rate Payment:", s1)
    
    if x1 >s1:#recommendation
        print("Standard rate is better")
    elif x1 > x2:
        print("Progressive rate - Seperate Payment is better")
    else:
        print("Progressive rate - Joint Payment is better")
    
    
    print("\n-------END-------\n")
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
        elif choice == "Q" or choice == "q":
            print ("You quit the Tax System")
            exit()

        else:
            sys.stderr.write("\nWrong input, please try again\n")



if __name__ == "__main__":
    main()
