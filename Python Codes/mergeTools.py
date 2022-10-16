def merge_the_tools(s, k):
    a=0
    for i in range(len(s)//k):
        t=s[a:a+k]
        ans=[]
        for j in t:
            if j not in ans:
                ans.append(j)
        a=a+k
        print(''.join(map(str,ans)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
