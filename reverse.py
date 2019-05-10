def rev():
    n=input('Enter the number\n')
    sum=0
    
    while n>0:
        no=n%10
        sum=sum*10+no
        #print(sum)
        n=n/10
        
    print(sum)    
rev()        
        