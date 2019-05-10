def arm():
    n=input('Enter the number\n')
    sum=0
    b=n
    
    while n>0:
        no=n%10
        sum=sum + no*no*no
        #print(sum)
        n=n/10
        
    print(sum) 
    
    if sum == b:
        print('Armstrong')
    else:
        print('Not')
arm()        
        