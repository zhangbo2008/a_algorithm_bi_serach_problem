#%%
'''
俊哥的解法:

'''
def fl(array):
    w = array[0]
    l = 0
    r = len(array)-1
    if array[r]==w:
        return r
    while r-l>1:
        m = (l+r)//2
        if array[m]>w:
            r = m
        else:
            l = m
    if array[r]==w:
        return r
    else:
        return l

#%%

def fr(array):
    l = 0
    r = len(array)-1
    w = array[r]
    if array[l]==w:
        return l
    while r-l>1:
        m = (l+r)//2
        if array[m]<w:
            l = m
        else:
            r = m
    if array[l]==w:
        return l
    else:
        return r

#%%

def f(array,w):
    if array[0]>w:
        return [None,0],False
    if array[-1]<w:
        return [len(array)-1,None],False
    l = 0
    r = len(array)-1
    while r-l>=0:
        m = (l+r)//2
        if array[m]==w:
            return m,True
        elif array[m]<w:
            l = m+1
        else:
            r = m-1
    return [r,l],False

#%%

def find(array,w):
    x,y = f(array,w)
    if y==False:
        return x
    else:
        array1 = array[:x+1]
        array2 = array[x:]
        a = fr(array1)
        b = fl(array2)
        return [a,b+x]

#%%

tmp=find([1,3,4,6,7,7,7],7)
print(tmp)
#%%


