n=int(input())
list=[]
for i in range(n):
    list.append(input().split())
res=[]
for i in range(n):
    if list[i][0]=="insert":
        res.insert(int(list[i][1]),int(list[i][2]))
    elif list[i][0]=="print":
        print(res)
    elif list[i][0]=="remove":
        res.remove(int(list[i][1]))
    elif list[i][0]=="append":
        res.append(int(list[i][1]))
    elif list[i][0]=="pop":
        res.pop()
    elif list[i][0]=="sort":
        res.sort()
    elif list[i][0]=="reverse":
        res.reverse()