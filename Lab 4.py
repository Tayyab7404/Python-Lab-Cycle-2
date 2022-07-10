# Program 4:

heads = int(input("Enter number of heads: "))
legs = int(input("Enter number of legs: "))

chickens = abs((4*heads) - legs) // 2
rabbits = abs((2*heads) - legs) // 2

if chickens + rabbits != heads:
    print("No solution")
    
else:
    print("Chickens = ",chickens)
    print("Rabbits = ",rabbits)
