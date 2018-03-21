flag = 1
while(flag==1):
    ch=input("enter the character:")
    if (ch>="a" or ch>="A") and (ch<="z" or ch<="Z"):
        print("Alphabet")
    else:
        print("Not Alphabet")
        flag =1
