class kmp():
    def __init__(self,pat):  # 这部分生成pat的dp矩阵,是整个算法的核心.
        dp=None
        self.pat = pat
        M = len(pat)
        dp = [[0]*256 for i in range(M) ]  # dp[i][j] 表示pat中i位置,匹配text中元素j,那么pat应该跳转到的下一个位置的索引
        dp[0][ord(pat[0])] = 1  # 从index0 如果匹配上就跳转到1.
        X = 0
        for j in range(1,M):
            for c in range(256):
                dp[j][c] = dp[X][c]
            dp[j][ord(pat[j])] = j + 1 # 匹配成功就进行推进

            # // 更新影子状态
            # // 当前是状态
            # X，遇到字符
            # pat[j]，
            # // pat
            # 应该转移到哪个状态？
            X = dp[X][ord(pat[j])]  # 这个地方是最难的, 跟下面serach代码很像. 右边表示影子进行了匹配,所以影子进行了推进,赋值给影子自己,影子也做更新. 影子跟pat一样,始终向前,不会回滚.
        self.dp=dp
    def search(self,txt):  # txt 是被搜索串, self.pat是匹配串,就是在txt中找到pat出现的索引.
        M=len(self.pat)
        N=len(txt)
        j=0 # j表示当前匹配到的索引.
        for i in range(N):
            j=self.dp[j][ord(txt[i])] # j表示跳转到的下一个索引.
            if (j==M): # 表示当前匹配的已经超过pat索引了,所以匹配玩成.
                return i-M+1 # i是当前txt的索引,剪去pat的距离即可.
        return -1

tmp=kmp('ab').search("111abc")
print(tmp)