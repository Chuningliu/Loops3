# Write a program to find the greatest common divisor (GCD) 
# or highest common factor (HCF) of given two numbers.


y=int(input("Enter the number"))
z=int(input("Enter the number"))
i=0
gcd=0
while i<=y and i<=z:
    if y%i==0 and z%i==0:
        gcd=i
    i+=1
print (gcd)