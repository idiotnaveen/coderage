num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input()
    num_array.append(int(n))
for i in range(int(num)-1):
    for j in range(int(num)-1):
        if num_array[j]>num_array[j+1]:
            temp=num_array[j]
            num_array[j]=num_array[j+1]
            num_array[j+1]=temp
print num_array
