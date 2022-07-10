# Program 7:

words = [w for w in input("Enter the words: ").split()]

n1 = n2 = 0

for i in words:
    if 'at' in i:
        n2+=1
        if i.endswith('at'):
            n1+=1
print(f"_at -> {n1}\n%at% -> {n2}")
