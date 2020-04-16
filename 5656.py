'''
返回二叉树第n行,第k个节点

'''
def find(root,n,k):
    listall=[]
    tmplist=[root]
    listall.append(tmplist)
    while set(tmplist)!=None:
        tmplist2=[]
        for i in tmplist:
            if i!=None:
                tmplist2.append(i.left)
                tmplist2.append(i.right)
        tmplist=tmplist2
        listall.append(tmplist)
    return listall[n][k] # 写完了 O(2*yezi)   O(yezi)  O1