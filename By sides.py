print('Welcome to "BhangChogra DJ Gaming" ')
print("draw your Triangle and find it's name")
a=int(input('lenght of 1st side--->   '))
b=int(input('lenght of 2nd side--->   '))
c=int(input('lenght of 3rd side--->   '))
if (a==b and b==c and c==a):
	print('Equelateral triangle')
elif ((a==b and b!=c) or (a==c and c!=b) or (b==c and c!=a)):
	print('Isoscale triangle')
elif (a!=b and b!=c and c!=a):
	print('Scalen triangle')
else:
	print('invaled input')