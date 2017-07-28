def is_sorted(word):

    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
        else:
            return True




print(is_sorted("ABC"))
print(is_sorted("aBc"))
print(is_sorted("dog") )
# Python is "less than" another character if
# it comes before it in alphabetical order,
 # so in order to see if a string is in alphabetical order
 # we just need to compare each pair of adjacent characters.
 # Also, note that you take range(len(word) - 1)
 # instead of range(len(word)) because otherwise you will
 # overstep the bounds of the string on the last iteration
 # of the loop.
# ////////////////////////////////////////////////////
def countstr(frase):
      num=frase.find(",")
      newstr=frase[num:]
      return len(newstr)

print(countstr("Before you go to bed, you need to brush your teeth"))
