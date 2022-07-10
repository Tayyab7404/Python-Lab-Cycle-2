# Program 9:

l = [n for n in input("Enter the numbers: ").split()]

l.sort(reverse = True)
max = ''
for n in l:
    max += n

print(max)
