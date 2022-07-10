num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

l1 = []
l2 = []

if num1<num2:
    for i in range(num1, num2+1):
        if i%5 == 0:
            if len(str(i)) == 2:
                if (i//10 + i%10) % 3 == 0:
                    l1.append(i)
    
    print(max(l1))
else:
    print(-1)
    exit(0)
