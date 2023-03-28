f=open("text.txt","w")
f.write("""1
2
3
4
5
6
7
8
9
10""")
f.close()
f=open("text.txt","r")
even= open("even.txt","w")
odd=open("odd.txt","w")
even.close()
odd.close()
even1 = open("even.txt","a")
odd1 = open("odd.txt","a")
for i in f:
    if int(i)%2==1:
        odd1.write(i)
    else:
        even1.write(i)
print("done")
