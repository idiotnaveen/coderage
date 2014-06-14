print "enter a number"
sum=0
x=input()
while x!=0:
    y=x%10
    sum=sum*10+y
    x=x/10
print sum
