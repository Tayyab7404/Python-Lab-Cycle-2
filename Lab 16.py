def is_vowel_word(word):
    for i in word:
        if i not in "aeiouAEIOU":
            return False
    return True

def sms_encoding(s):
    msg = s.split()
    sms=''
    for i in msg:
        if is_vowel_word(i):
            sms += i + ' '
            continue
        for j in i:
            if j not in "aeiouAEIOU":
                sms += j
        sms += " "
        
    return sms

s = input("Enter a sentence: ")

sms = sms_encoding(s)

print(sms)