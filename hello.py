str="this is python programming "
a=''
t=0
b=20
coun=0
for i in str:
    
    if(i!=' '):
        a+=i
    elif(i==' '):
        l=len(a)
        
        if(l>t):
            t=l
            pos1=coun
        if(b>=l):
            b=l
            pos2=coun
        a=''
    coun+=1
print("the largest word is")
print(pos1)
i=pos1-t
while(i<pos1):
    print(str[i])
    i=i+1
print("the smallest word is")
print(pos2)
print(b)
k=pos2-b
while(k<pos2):
   print(str[k])
   k+=1




