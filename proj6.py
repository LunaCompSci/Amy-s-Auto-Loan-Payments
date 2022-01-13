#CSC110, Christina Nguyen, calcuates financial data based on what the user selects and gives it in a spreadsheet 
def main():
     
    loanAmount, interestRatePerPeriod = inputLoanData() 
    periodNum = showMenu()
    while periodNum != 0:
        pmtAmt = payment(loanAmount, interestRatePerPeriod, periodNum)
        print(pmtAmt) 
        showReport(loanAmount, interestRatePerPeriod, periodNum, pmtAmt)
        periodNum = showMenu()
    
def inputLoanData():
    loanAmount = int(input("Enter loan amount, example 10000: "))
    while loanAmount < 0:  
        print("ERROR: Loan amount cannot be negitive.") 
        loanAmount = int(input("Enter loan amount, example 10000: "))
        
    interestRate = float(input("Enter annual interest rate, example 2.9: "))
    while interestRate < 0:
        print("ERROR: Interest Rate cannot be negitive.")
        intertestRate = float(input("Enter annual interest rate, example 2.9: "))

    interestRatePercent = interestRate / 100
    interestRatePerPeriod = interestRatePercent / 12
    return loanAmount, interestRatePerPeriod 
        
def showMenu():
    print("-" * 32)
    print("Amy's Auto - Loan Report Menu")
    print("-" * 32)
    print("1. 12-month loan")
    print("2. 24-month loan")
    print("3. 36-month loan")
    print("4. 48-month loan")
    print("5. 60-month loan")
    print("0. EXIT")
    choice = int(input("\nChoice: "))

    while choice < 0 or choice >= 6: #should show the Menu again if an invalid choice is given. 
        print("-" * 32)
        print("Amy's Auto - Loan Report Menu")
        print("-" * 32)
        print("1. 12-month loan")
        print("2. 24-month loan")
        print("3. 36-month loan")
        print("4. 48-month loan")
        print("5. 60-month loan")
        print("0. EXIT")
        choice = int(input("\nChoice: "))
        
    periodNum = choice * 12
    return periodNum
    
def payment(loanAmount, interestRatePerPeriod, periodNum):
    pmtAmt = (interestRatePerPeriod * loanAmount) / (1 - (1 + interestRatePerPeriod) ** -periodNum) 
    return round(pmtAmt,2)  
    
def showReport(loanAmount, interestRatePerPeriod, periodNum, pmtAmt):
    print(format("Pmt#",'8s'),format("PmtAmt",'9s'),format("Int",'7s'),format("Princ",'9s'),"Balance")
    print(format("-"*4,'5s'),format("-"*9,'10s'),format("-"*5,'8s'),format("-"*6,'9s'),format("-"*8))

    balance = loanAmount
    for pmtNum in range(1, periodNum): 
        interest = round(balance * interestRatePerPeriod, 2) 
        princ = pmtAmt - interest
        balance -= princ 
        print(format(pmtNum,'4.0f'), format(pmtAmt,'11,.2f'), format(interest,'6,.2f'), format(princ,'9,.2f'), format(balance,'11,.2f')) #When the pmtNum increases, current balance turns into the previous balance. 
        
    interest = round(balance * interestRatePerPeriod, 2)    #accounts for last payment
    lastPmtAmt = balance + interest 
    princ = pmtAmt - interest
    print(format(pmtNum + 1,'4.0f'), format(lastPmtAmt,'11,.2f'), format(interest,'6,.2f'), format(princ, '9,.2f'), format(0,'11,.2f'))
    print(" " * 7, "-" * 9)
    print(format(pmtAmt * pmtNum + lastPmtAmt, '17,.2f'))
    print()
    input("Press <enter> to continue")
    
main()

#I got stuck in a varity of places.
#1.)I got stuck was realizing that it doesn't matter whether I use accounting rounding or normal rounding
#2.)I got stuck was recognizing that negitive scientific notation is close to negitive. I didn't recognize the negitive sign and thought my results were way off.
#3.) I returned periodNum and choice in showMenu when the instructions said I should only return periodNum
#4.) I put calculations in payment instead of showReport
#5.) I overcomplicated line __ by adding 12 instead of multiplying
#6.) I accounted for the last payment inside the for loop when it should have been outside.
#I used two test cases. One was using the results in the instructions and the other was a loan payment of 10000, an interest rate of 2.9 and a 12-month plan which Bill gave a spreadsheet of the results.
#In both test cases, my last test was off by two cents.
#this was because I was scared to use the round() because I didn't fully understand accounting rounding
#Next time, I'll test one thing and make sure it's bullet-proof and not code everything at once
