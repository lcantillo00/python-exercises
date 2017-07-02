weekdays=["sunday","monday","tuesday", "wednesday","thursday","friday","saturday"]
starday=int(input("what day you wan to start your trip from 0 to 6"))
duration=int(input("how many days are you planing to travel"))
returnD=starday+duration
nw=returnD%7

if nw==1:
   print("you are going to return  on day " + str(nw) +" monday")
elif nw==2:
     print("you are going to return  on day " + str(nw) +" tuesday")
elif nw==3:
     print("you are going to return  on day " + str(nw) +" wednesday")
elif nw==4:
     print("you are going to return  on day " + str(nw) +"thursday")
elif nw==5:
     print("you are going to return  on day " + str(nw) +"friday")
elif nw==6:
     print("you are going to return  on day " + str(nw) +"saturday")
else:
     print("you are going to return  on day " + str(nw) +" sunday")
