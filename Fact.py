def siva(x):
    count=0
    for i in x:
        if i.isupper():
          count +=1
    return count      
x='SiVaReDdY'
print(siva(x))
