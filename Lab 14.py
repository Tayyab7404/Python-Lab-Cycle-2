def rearrange(s):
    vowels = ""
    consonants = ""
    for i in s:
        if i in "aeiouAEIOU":
            vowels+=i
        else:
            consonants+=i
    return consonants+vowels

def encrypt_message(msg):
    words = msg.split()
    encrypted = []
    for i in range(len(words)):
        if i%2 == 0:
            encrypted.append(words[i][::-1])
        else:
            encrypted.append(rearrange(words[i]))
    return " ".join(encrypted)

msg = input("Enter your message: ")

print(encrypt_message(msg))