print "enter two nubers"
x=int(input())
y=int(input())
temp1=x
temp2=y
while y!=0:
    if(x%y==0):
        ans=(temp1*temp2)/y
        print ans
        y=0
    else:
        temp=x
        x=y
        y=temp%y
    
