print "enter two nubers"
x=int(input())
y=int(input())
while y!=0:
    if(x%y==0):
        print y
        y=0
    else:
        temp=x
        x=y
        y=temp%y
    
