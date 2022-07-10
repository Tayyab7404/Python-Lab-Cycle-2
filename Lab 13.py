s1 = input("Enter first sentence: ")
s2 = input("Enter second sentence: ")
s = []
for i in s1:
    for j in s2:
        if i == j:
            s.append(i)
            s1=s1.replace(i,'')
            s2=s2.replace(j,'')
            break
if len(s)==0:
    print(-1)

else:
    print(''.join(s).replace(" ",""))