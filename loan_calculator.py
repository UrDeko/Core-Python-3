money_owed = float(input("How much money do you owe:"))
apr = float(input("What is your annual percentage rate:"))
payment = float(input("Money per month:"))
months = int(input("Months:"))

monthly_rate = apr/100/12

for i in range(months):
    interest = money_owed * monthly_rate
    money_owed += interest

    if (money_owed - payment < 0):
        print(f"The last payment is {money_owed}. You paid off the loan in {i + 1} months")
        break

    money_owed -= payment

    print(f"Paid {payment} of which {interest} was interest. Now I owe {money_owed}")