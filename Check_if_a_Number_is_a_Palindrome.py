#THIS IS CREATED BY AIBAL AND ANY ERROR IN THIS CODE IS NATURAL SO TAKE IT ON THAT SENSE.
ptint("Program to check the given number is a palindrome\n")
n=int(input("Enter number:"))
temp=n
A=0
while(n>0):
    D=n%10
    A=A*10+D
    n=n//10
if(temp==A):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
