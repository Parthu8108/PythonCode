num=7

if num > 1:
    for i in range(2,num):
        if(num % i)==0:
            print(num,'not prime')
            break
    else:
        print(num,'prime')
        #break

else:
   print('not prime')
