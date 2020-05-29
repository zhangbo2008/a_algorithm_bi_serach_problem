
def main():
    a = input()
    try:
     a = [int(i) for i in a.split(' ')]
    except:
        print(-1)
        return
    S = a[0]
    N = a[1]
    if S <=0 or S>=100000:
        print(-1)
        return

    if N<=0 or N>=100000:
        print(-1)
        return
    if S!=int(S):
        print(-1)
        return
    if N != int(N):
        print(-1)
        return
    if N%2==0:


        zhongjian1=S/N-0.5
        if zhongjian1!=int(zhongjian1):
            print(-1)
            return
        zhongjian2=S/N+0.5
        kaishi=zhongjian1-N/2+1
        if kaishi<=0:
            print(-1)
            return
        elif kaishi!=int(kaishi ):
            print(-1)
            return
        else:
            kaishi=int(kaishi)
            out=list(range(kaishi,kaishi+N))

            out=[str(i) for i in out]

            print(' '.join((out)))
    else:
        zhoangjian=S/N
        kaishi=zhoangjian-N//2
        if kaishi<=0:
            print(-1)
            return
        elif kaishi!=int(kaishi ):
            print(-1)
            return
        else:
            kaishi = int(kaishi)
            out = list(range(kaishi, kaishi + N))

            out = [str(i) for i in out]

            print(' '.join((out)))
main()