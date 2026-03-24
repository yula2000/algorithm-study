arr = map(int,input().split())

for i in arr:
    if i**2+(i+1)**2 == (i+3)**2:
        print('right')
    else:
        print('wrong')
