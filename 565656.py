'''
9.输入一个变形数组，及某个数字，输出这个数字在变形数组中的位置
def find_num(array, num)  要求算法复杂度为 log(n)
变形的方法是将一个排好序的数组某个位置之前的数放到数组末尾，比如
原始数组为：
2  3  6  9  10  12  24  34
得到以下变形数组（将2 3 6放在了数组末尾）：
9  10  12  24  34  2  3  6
比如，输入24和变形数组，输出 3
   说明：
1.不需要写变形的code，输入已经是一个变形的数组了
2.不知道具体将多少个数放在了数组的末尾

'''


#9  10  12  24  34  2  3  6
#9  10  12  24  34  100  3  6 7 7.5 7.6 7.7 7.8 7.9
#9  10  12  24  34  100  3  6 7 7.5 7.6 7.7
def findA(array):  # 找到轴的index
    if len(array)==2:
        return 1
    left = 0
    right = len(array) - 1
    mid = (left + right) // 2  # mid始终找中间偏左的na一个.
    if array[left] > array[mid]:
        return findA(array[:mid+1])
    return mid  + findA(array[mid:])
def search(list, key):
    left = 0     # 左边界
    right = len(list) - 1   # 右边界
    while left <= right:
        mid = (left + right) // 2  # 取得中间索引
        if key > list[mid]:
            left = mid + 1
        elif key < list[mid]:
            right = mid - 1
        else:
            return mid
    else:
        return -1

print(findA([10,11,12,32423423,1,2,3,4,5]))
def find_num(array, num):
    tmp=findA(array)
    if num >array[-1]:
        return search(array[:tmp],num)
    else:
        return tmp+search(array[tmp:],num)









tmp=find_num([9  ,10  ,12  ,24,  34 , 2  ,3 , 6],6)
# tmp=find_num([24],24)
print(tmp)






'''
二分法写:
[1,3,4,6,7,7]  , 7
返回里面7所有的下标. 4,5

如果没有7 就返回临近的下标.

比如如果是9 就返回 5,None
如果是5 , 就返回2,3
'''
def search2(list2,num):
    left=0
    right=len(list2)-1
    tmp=[]
    while left<=right:
        mid=(left+right)//2
        if list2[mid]==num:
            tmp.append(mid)
            left=mid+1
            tmp+=search2(list2[:mid],num)
            tmp+=search2(list2[mid+1:],num)
        elif list2[mid]>num:
            right=mid-1
        else:
            left=mid+1
    return tmp
print(search2([1,2,3,6,6,7],5))



def search3(list3,num):

    # 2次对撞指针, 第一次找left, 第二次找right
    # 应该用对撞指针
    left=0
    right=len(list3)-1
    while left<=right:
        mid=(left+right)//2
        if list3[mid]==num:
            tmp.append(mid)
            left=mid+1
            tmp+=search2(list2[:mid],num)
            tmp+=search2(list2[mid+1:],num)
        elif list3[mid]>num:
            right=mid-1
        else:
            left=mid+1
    return left,right

