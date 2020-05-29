# a=input()

def main():
    a=input()
    zhan=[]
    cnt=0
    maxi=0
    if len(a)>100000:
        print(0)
        return
    for i in a:
        if i=='[':
            zhan.append('[')
        if i=='{':
            zhan.append('{')
        if i=='(':
            zhan.append('(')
        if i==']':
          try:
                if zhan[-1]=='[':
                    cnt+=1
                    zhan.pop(-1)
                else:
                    print(0)
                    return
          except:
                print(0)
                return
        if i=='}':
            try:
                if zhan[-1]=='{':
                    cnt+=1
                    zhan.pop(-1)
                else:
                    print(0)
                    return
            except:
                print(0)
                return
        if i==')':
            try:
                if zhan[-1]=='(':
                    cnt+=1
                    zhan.pop(-1)
                else:
                    print(0)
                    return
            except:
                print(0)
                return
        maxi=max(len(zhan),maxi)
    print(maxi)
    return maxi

main()

