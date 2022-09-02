import random
l= []
for _ in range(10):
    l.append(random.randint(0,100))
print('Original List:\n',l)

pointer = len(l)-1

while pointer != 0:
    for i in range(0,pointer):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
    pointer-=1

print('Sorted List:\n',l)