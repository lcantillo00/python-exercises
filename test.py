# def analyze_text(text):
#   alpha_total = text[:] # takes the full lenght of the sentence
#   individual_let="" # initialize to an empty string, can be set to any string
#   alpha_count =0 # Will count each letter in the string
#   e_count=0 # Will count each 'e' capitalize or lowercase in the sentence of the user input
#
# #create a counter for the amount of individual letters while ignoring the special characters and spaces
#   for letter_position in range(len(text[:])):
#     individual_let =individual_let+text[letter_position] #indexes each letter in the sentence
#     if (individual_let.isalpha() ==True): #verify that each character in the sentence is an alphabeth
#       alpha_count+=1 # increments the count for each letter that appears
#       if (individual_let).upper()=="E":
#         e_count+=1
#
#     percent_e = (e_count*100)/alpha_count
#     result= "The text contains"{}," alphabetic characters, of which {} ({}%)are 'e'.".format(alpha_count,e_count,percent_e)
# text1 = "Eeeee"
# print(analyze_text(text1))
# def sort_contact(contact):
#     result=[]
#
#     for i in sorted(contact.items()):
#         result.append(i)
#     return result
# my={"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
# "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
# "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}
# print(sort_contact(my))



# def analyze_text(text):
#     new_text=text.replace(" ", "")
#     lower_case_e=new_text.count('e')
#     upper_case_e=new_text.count('E')
#     total_e=int(lower_case_e+upper_case_e)
#
#     non_alpha=0
#     for n in string.punctuation:
#         if n in new_text:
#             non_alpha+1
#
#     letters=sum("")
#     for letter in new_text:
#         if letter.isalpha()==True:
#             letters=letters+1
#
#     total_char=letters-non_alpha
#     avg=(100.0*total_e/total_char)
#     return "The text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(letters,total_e,str(avg))

    # return "The text contains {0} alphabetic characters, of which {1} ({2}%) are 'e'.".format(letters,total_e,str(avg))
# def analyze_text(text):
#     # Your code here
#     # % == (qty e)/(total alphabet) * 100
#     count_alpha = 0
#     for a in range(len(text)):
#         if text[a].isalpha():
#             count_alpha += 1
#     total_e = text.count("e") + text.count("E")
#     avg_e = str((total_e / count_alpha) * 100)
#
#     return “The text contains {} alphabetic characters, of which {} ({}%) are ‘e’.“.format(count_alpha,total_e,avg_e)
# test1="eeeee"
# print(analyze_text(test1))
def get_country_codes(prices):
    # your code here
    half = prices.split(',')
    #print(half)
    codes = ""
    
    for char in half:
          codes = codes + char[0:2]

        return codes
print(get_country_codes("NZ$300, KR$1200, DK$5"))
