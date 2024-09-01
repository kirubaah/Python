salary = int(input("Salary: "))
age = int(input("Age: "))
if (salary >= 20000 or age <= 25):
    loan = int(input("Loan: "))
    if (loan <= 50000):
        print("Eligible for loan.")
    else:
        print("Maximum loan amount is 50,000.")
else:
    print("Not Eligible for loan.")
