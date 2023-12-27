def siva(x):
    count=0
    for i in x:
        if i.isupper():
          count +=1
    return count      
x='SiVaReDdY'
print(siva(x))
######################################

x=[1,2,4]  #output=[6,5,3]

s=[]
for i in range(len(x)):
    s.append(sum(x[:i])+sum(x[i+1:]))
print(s)



