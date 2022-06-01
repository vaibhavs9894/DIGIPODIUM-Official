fname = 'Vijay'
lname = 'Dixit'

# concatenation - joining strings together

fullname = fname + ' ' + lname + ' is the name'
print(fullname)

# duplication - cloning the string

word = 'ha'
print(word * 3)
print('-|-'* 2 )
print('/' * 25)

for i in range(1,10):
    print('$ ' * i)

# membership operator
message = 'the most elephant important thing for a coder is to code'

if 'elephant' in message:
    print('i am in elephant')
if 'thing' in message:
   print('things -> word found')
if 'very' in message:
    print('very -> word found')

if 'z' not in message:
    print('z is not available in message')

