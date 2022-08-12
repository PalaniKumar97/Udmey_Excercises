#for i in range(5):
Name=input("Enter your Name:")
Age=int(input("Enter your Age:"))

if Age<=18:
    print("You are Eligible to Vote,",Name,'and',"Your Age is:",Age)
    print("You are Eligible to vote in this Election")
elif Age>18:
    print("You are Eligible to Vote,", Name, 'and', "Your Age is:",Age)
    print("You are not Eligible to vote in this Election")
else:
    print("Invalid Request from user 1")