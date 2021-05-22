#wap to count the no of even and odd numbers from a series
a={23,2,58,56,6,7,4,9,65}
evencnt=0
oddcnt=0
for i in a:
    if i%2==0:
      evencnt += 1
    else:
      oddcnt += 1
print('Total Even no are',evencnt)
print('Total Odd no are',oddcnt)