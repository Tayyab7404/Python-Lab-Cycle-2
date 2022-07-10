# Program 2

a = [int(x) for x in input("Enter three numbers: ").split()]
if len(a) != 3:
    print('Enter 3 numbers')
    exit(0)
else:
    ans = 1

    if 7 in a:
        if a.index(7)==2:
            ans = -1
        elif a.index(7)==0:
            ans = a[1]*a[2]
        else:
            ans = a[2]

    else:
        ans = a[0]*a[1]*a[2]

    print(ans)
