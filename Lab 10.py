def RLE(st):
    RLEcode =''
    n = len(st)
    i = 0
    while i < n:
        count = 1
        while (i+1 < n and st[i] == st[i + 1]):
            count += 1
            i += 1
        i += 1
        RLEcode += str(count) + st[i - 1]
    return RLEcode

s = input("Enter the string: ")

print(f"RLE code for \'{s}\' is \'{RLE(s)}\'")