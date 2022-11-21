s1=input()
s2=input()
l=s2[-1]

count=0
for i in s1:
    if i==l:
        count+=1
print(count)
