a=[78,4,55,7]
for i in range(len(a)-1):
    #print ("i",i)
    for j in range(len(a)-1):
        #print ("j",j)
        if a[j+1]<a[j]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print a
