#THIS IS CREATED BY AIBAL AND ANY ERROR IN THIS CODE IS NATURAL SO TAKE IT ON THAT SENSE.

print("Program to find the sum of 1+x+x^3+x^5+x^7.......N \n")
x=int(input("Input the number : "))
i=0
n=int(input("Input limit : "))

s=1

    
while i<=n:
    i=i+1
   
    if (i%2==1):
        s=int(s)+x**i
        
else:print ("sum is : "+str(s))
