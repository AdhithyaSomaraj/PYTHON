n=int(input("Enter the number :"))
rev=0
while n!=0:
	rem=n%10
	rev=rev*10+rem
	n=n//10
print("Reverse is {}".format(rev))
