s=input()
max=0
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        if count>max:
            max=count
        count=1
if count>max:
    max=count
print(max)