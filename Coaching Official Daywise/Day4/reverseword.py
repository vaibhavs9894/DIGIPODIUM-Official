#wap to accept a word from user and reverse it

a=str(input('enter a String'))
b=''
for char in a:
    print(char)
    b=char + b

print('reverse of string is',b)