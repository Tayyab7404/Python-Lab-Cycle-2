def largest(d):
    k = list(d.keys())
    vals = list(d.values())
    large = []
    m = max(vals)
    if vals.count(m) > 1:
        for i in range(len(vals)):
            if m == vals[i]:
                large.append(k[i])
    lens = [len(i) for i in large]
    return (large[lens.index(max(lens))], m)

text = input("Enter the text: ").split()
words = []

for i in text:
    if i not in words:
        words.append(i)

d = {}
for i in words:
    d.update({i : text.count(i)})

w, freq = largest(d)
print(f"The word with highest frequency is \'{w}\' with a frequency of {freq}")
