# Program 8:

def isLeapyear(y):
  return True if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else False

y = int(input("Enter the starting year: "))

n = y
count = 0
leaps = []

while count != 15:
  if isLeapyear(y):
    leaps.append(y)
    count += 1
  y += 1

print(f"The list of first 15 leap years starting from {n} are: ", leaps)
