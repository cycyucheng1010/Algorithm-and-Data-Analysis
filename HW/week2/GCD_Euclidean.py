#最大公因數
num1 = int(input('num1?'))
num2 = int(input('num2?'))
m = max(num1,num2)
n = min(num1,num2)
r = m % n
while r != 0:
    m=n
    n=r
    r=m%n
print(num1,"and",num2,"GCD=",n)