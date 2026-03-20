# Calculate Compound Interest.....

print("Enter the following details to calculate Compound Interest")
principal = float(input("Principal amount: "))
rate = float(input("Rate of interest: "))
time = float(input("Time period: "))
Total_amount = principal * (1 + rate / 100) ** time
Compound_interest = Total_amount - principal
print("Compound Interest: ", Compound_interest)