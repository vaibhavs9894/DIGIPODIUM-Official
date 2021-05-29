def agg(*n,o="sum"):
    if n:
        if o=='sum':
            print('total',sum(n))
        elif o=='mean':
            print('mean',sum(n)/len(n))

agg(1,4,55,77,3456,677,2334)
agg(1,4,55,77,3456,677,2334,o='mean')
