l1=[]
for i in range(0,10):
    x=int(input("Enter number:"))
    l1.append(x)
suml=sum(l1)/10
print("average=",suml)
for j in range(5):
    for k in range(j):
        print("*",end=' ')
    print('\n')