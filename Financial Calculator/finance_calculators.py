import math
choose_option = input("What would you like to open? Choose between a bond or an investment? ")
if choose_option == "investment":
    print("Welcome to the Investment Calculator! Starting an investment is like a journey and every journey starts with a clear plan. Let us begin drawing up a plan for you")
    deposit = int(input("First thing's first, how much money would you like to invest? "))
    
    print(f"Great! Now, that you have provided me with a deposit amount of  { deposit }, let's determine the interest rate you will earn on your investment.")
    interest_rate = int(input("What is the interest rate you expect to earn? "))
    
    print(f"Excellent! You have selected an interest rate of  {interest_rate}. Now, what is important is that we establish the time period for your investment.")
    time_period = int(input("How many years do you plan to invest for? "))

    print(f"Now that we have established a time period of { time_period } for your investment, let us establish whether you would like to apply compound or simple interest to your investment.")
    interest_type = input("Would you like to apply simple or compound interest? ")

    if interest_type == "simple":
        total_amount_simple = deposit * (1 + (interest_rate / 100) * time_period)
        print(f"You have selected simple interest. Therefore, the future value of your investment will be {total_amount_simple}.")

    elif interest_type == "compound":
        total_amount_compound = int(deposit) * math.pow((1 + (int(interest_rate))),int(time_period)) #** int(time_period)) #/ 100
        str_total_amount_compound = str(total_amount_compound)
        print("You have selected compound interest. Therefore, the future value of your investment will be " + str_total_amount_compound + ".")

elif choose_option == "bond":
    print("Welcome to the Bond Calculator! This signifies the first step towards securing your dream home.")
    pv = input("First thing's first, what is the present value of the house? ")
    int_pv = int(pv)
    print("Thank you so much for providing me with the present value of the house you wish to buy!")
    interest_rate_loan =float(input("Next please provide me with the intrest rate for your bond repayement?"))/100/12
    print("Lastly, please provide me with the duration over which you would like to pay off your loan.")
    duration = float(input("Over how many months would you like to repay your loan: "))
    duration = float(duration)
    loan_repayement = ((interest_rate_loan)*int_pv)/(1 - (1 + interest_rate_loan) ** (-duration))
    str_loan_repayement = str(loan_repayement)
    print("Given the monthly interest, present value of the house, and the number of months over which the bond will be repaid, your monthly bond repayements will be " + str_loan_repayement + ".")
