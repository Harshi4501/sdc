Generate first N number of Fibonacci numbers. Take N value from user
n = int(input("Enter the value of 'n': "))
a=0
b=1
print("Fibonacci Series:")
for i in range(1,n+1):
  print(a,end='\t')
  c=a+b
  a=b
  b=c
