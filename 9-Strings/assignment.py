# def analyze_text(text):
#     filtered=''
#     for c in text:
#         if c.isalpha():
#             filtered=c.lower()
#     # filtered = [c.lower() for c in text if c.isalpha()]
#     cnt = filtered.count('e')
#     result = "The text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(len(filtered),cnt,str(100.0*cnt/len(filtered))[:13])
#     return result
#
#
# # Don't copy these tests into Vocareum
# from test import testEqual
#
# text1 = "Eeeee"
# answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
# testEqual(analyze_text(text1), answer1)
#
# text2 = "Blueberries are tasteee!"
# answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
# testEqual(analyze_text(text2), answer2)
#
# text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
# answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
# testEqual(analyze_text(text3), answer3)
def analyze_text(text):
  individual_let="" 
  for i in text:
      if i.isalpha(): 
         individual_let=individual_let+i.lower()
  count=individual_let.count('e')
  print(count)
  percent_e=int(count*100/len(individual_let))
  

  result= "The text contains {} alphabetic characters, of which {} ({}%)are 'e'.".format(len(individual_let),count,str(percent_e))
  return result
text1 = "Eeeee"
print(analyze_text(text1))

# def analyze_text(text):
#     filtered=''
#     for c in text:
#
#         if c.isalpha():
#             filtered=filtered+c.lower()
#     # filtered = [c.lower() for c in text if c.isalpha()]
#     cnt = filtered.count('e')
#     result = "The text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(len(filtered),cnt,str(100.0*cnt/len(filtered))[:13])
#     return result
#
#
# # Don't copy these tests into Vocareum
# from test import testEqual
#
# text1 = "Eeeee"
# answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
# testEqual(analyze_text(text1), answer1)
#
# text2 = "Blueberries are tasteee!"
# answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
# testEqual(analyze_text(text2), answer2)
#
# text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
# answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
# testEqual(analyze_text(text3), answer3)
