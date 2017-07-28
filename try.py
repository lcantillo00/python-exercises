# def printing_numbers(i):
#     for number in range(i):
#         number = number + 1
#         print(number)
#         return
#
# number = 50
# printing_numbers(number)
# print(number)
# //////////////////////////////////////////////////
# alist = [4, 2,[3,5], 8, 6, 5]
# blist = []
# for item in alist:
#
#     if type(item) == list:
#         blist.append([])
#
#         for i in item:
#             blist[alist.index(item)].append(i+5)
#
#     else:
#         blist.append(item+5)
#
# print(blist)
# 53 PM]
# added this Python snippet: Chapter 9 Weekly Graded Assignment
# def analyze_text(text):
#   alpha_total = text[:] # takes the full lenght of the sentence
#   individual_let="" # initialize to an empty string, can be set to any string
#   alpha_count =0 # Will count each letter in the string
#   e_count=0 # Will count each 'e' capitalize or lowercase in the sentence of the user input
#
# #create a counter for the amount of individual letters while ignoring the special characters and spaces
#   for letter_position in range(len(text[:])):
#     individual_let =text[letter_position] #indexes each letter in the sentence
#     if (individual_let.isalpha() ==True): #verify that each character in the sentence is an alphabeth
#       alpha_count+=1 # increments the count for each letter that appears
#       if (individual_let).upper()=="E":
#         e_count+=1
#
#   percent_e = (e_count*100)/alpha_count
#   print("The text contains", alpha_count," alphabetic characters, of which ", e_count,"(",percent_e, "%) are \'e\' ." )
# def sort_contacts(contact):
#     result=[]
#     for i in sorted(contact.items()):
#          result.append(i)

#     return result
#     text1={"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
#         "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
#         "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}
#     print((sort_contacts(text1))
# def substitution(text,shift):
#     for i in text:
#         if i.isalpha(): 
#             print(chr(ord(i)+shift%26),end="")
#         else: 
#             print(i,end="")
# print(substitution("hello lily",5))

credit_card_number=input("what is your credit card number:")

if credit_card_number !=16:

    while True:

        input("The credit card must be 16 digits, enter the number again.")

        break

else:

    print("This is a valid number")
