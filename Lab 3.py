# Program 3:

x = int(input("Enter number of 1 rupee coins: "))
y = int(input("Enter number of 5 rupee coins: "))
z = int(input("Enter amount to be paid: "))

if (x + y*5)==z:
    print("1 rupee coins = ",x,"\t5 rupee coins = ",y)

elif (x + y*5) < z:
    print(-1)

else:
    coins_5 = z//5
    coins_1 = z - (coins_5*5)
    print("1 rupee coins = ",coins_1,"\t5 rupee coins = ",coins_5)
