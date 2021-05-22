#Wap to get Fibonacci series between 0 to 50
a=0
b=1
print('Fibonacci series from 0 to 50 is')
print(a, b,end=" ")
#for i in range(0,8):
c=0 
while c<51: 
    c =a+b
    a=b
    b=c
    print(c,end=" ")