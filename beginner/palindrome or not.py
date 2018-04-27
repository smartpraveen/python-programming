s=int(input("Enter the value:"))
temp=s
reverse=0
while(s>0):
      remainder= s%10
      reverse=(reverse*10)+remainder
      s=s//10
if(temp==reverse):
      print("yes")
else:
      print("N0")
