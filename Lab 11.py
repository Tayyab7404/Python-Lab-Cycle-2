def translate(d, wish):
    words = wish.title().split()
    swedish = []
    for i in words:
        swedish.append(d.get(i))
    return " ".join(swedish)

d = {"Merry":"God",
     "Christmas":"Jul",
     "And":"och",
     "Happy":"Gott",
     "New":"Nytt",
     "Year":"Ar"} 

wish = input("Give your wishes in English: ")
print(translate(d, wish))