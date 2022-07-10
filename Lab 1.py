# Program 1:

A = int(input("Enter number of Adults: ")) * 37550
C = int(input("Enter number of Children: ")) * (37550/3)

cost = A + C # Actual amount
cost += (0.07 * cost) # Service Tax - 7%
cost -= (0.1 * cost) # Discount - 10%

print("Total Ticket cost = ",cost)
