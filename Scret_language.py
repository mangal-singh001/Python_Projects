import random
import string
str = input("Enter string  : ")
str1 = str.split(" ")
coding = input("1 for coding and 0 for decoding : ")
coding = True if(coding=="1") else False
if coding:
    nstr = []
    for words in str1:
     if len(words) <= 3:
        nstr.append(words[::-1])
     else:
        prefix = random.choice(string.ascii_uppercase) * 3
        suffix = random.choice(string.ascii_lowercase) * 3
       
        new_str = prefix + words[1:] + words[0] + suffix
        nstr.append(new_str)
    print(" ".join(nstr))
        
        
else:
    nstr = []
    for words in str1:
     if len(words) <= 3:
        nstr.append(words[::-1])
     else:
        new_str = words[3:-3] 
        new_str = new_str[-1] + new_str[:-1]
        nstr.append(new_str)
    print(" ".join(nstr))