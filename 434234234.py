'''
我的解法:
也是想了超久才想好.

二分法写:
[1,3,4,6,7,7]  , 7
返回里面7所有的下标. 4,5

如果没有7 就返回临近的下标.

比如如果是9 就返回 5,None
如果是5 , 就返回2,3


'''





# 还是这个题目. 先找left: 1,3,4,5,6,7,8 找3.5    left的index :特征是右边比3.5大
# 就是不停的二分,找<=num的并且index最大的 数的index
def findleft(list2,num):
    left=0
    right=len(list2)-1

    while left<=right:
        mid=(left+right)//2
        if list2[mid]<=num:
            tmp=mid
            left=mid+1 # 保证之后取的index大于mid
        if list2[mid]>num:
            right=mid-1
    try:
        return tmp
    except:
        return None
print(findleft([1,3,4,5,6,7,8,9,10],4.5))










