num=int(input('Please input number => '))
spc=' '*max(0,num-1)

for i in range(1,2*num,2):
    ast='*'*max(1,i)
    out=spc+ast
    print(out)
    spc=spc.replace(' ','',1)
