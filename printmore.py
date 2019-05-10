print("Welcome user:")
print("Please enetr your name:")
name=raw_input();
print("Please enetr your place:")
place=raw_input();
print("The name of the user is:" +name.upper())
print("The place of the user is:" +place.lower())


print('I havce %d cats'%6 )
print('I havce %2d cats'%6 )
print('I havce %0.2d cats'%2 )
print('I havce %6f cats'%6 )
print('I havce %0.2f cats'%6 )

#EXAMPLE OF .format
print('no1 {0:d} no2 {1:d} no3 {2:d} '.format(6,5,2) )
print('I have {0:d} cats'.format(7) )
print('I have {0:d} cats'.format(8) )

#example of \
total=6+5+4 \
    +4
print(total)

print('no1 {0:d}'+ \
'no2 {1:d}'+ \
' no3 {2:d} '.format(6,5,2) )


