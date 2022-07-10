def no_of_combis(n):
    return 2**n

n = int(input("Enter number of flavours of toppings: "))
print("Number of combinations of coffee: ", no_of_combis(n))