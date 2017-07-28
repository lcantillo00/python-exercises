x = input("Enter a sentence")

x = x.lower()   # convert to all lowercase

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {} # empty dictionary
for char in x:
        if char in alphabet: # ignore any punctuation, numbers, etc
                if char in letter_count:
                        letter_count[char] = letter_count[char] + 1
                else:
                        letter_count[char] = 1

keys = letter_count.keys()
keys.sort()
for char in keys:
        print(char, letter_count[char])
# ///////////////////////////////////another way
mystr=input("enter you string")
mystr.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count={}
for i in mystr:
    if i in alphabet:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
mykeys=count.keys()
mykeys.sort()
for i in mykeys:
    print(i,count[i])
