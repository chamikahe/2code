a=int(input("enter the number"))
c=[]
d=""
while a!=0:
    b=input("enter the senternse").split()
    while len(b)!=0:
        c.append(b.pop())
        for i in c:
            d=str(d)+" "+c.pop()
    print(d)
    a=a-1
    d=""


