def sort_contacts(contact):
    result=[]
  
    for key, val  in sorted(contact.items()):
        # for i in val:
        result.append((key,val[0],val[1]))
      
    return result
mylist=({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")})
print(sort_contacts(mylist))
