ct = ""
pt = "Hello"
key = 3 
for i in pt:
    if i.isnumeric():
        ct = ct + i 
    else:
        x = ord(i)
        if x == 10 or x == 32 :
            ct = ct + chr(x)
        elif chr(x).islower:
            ct = ct + chr((x-ord('a')+key)%26)
        elif chr(x).isupper():
            ct = ct + chr((x-ord('A')+key)%26)
        else :
            ct = ct + i 
print(ct)
