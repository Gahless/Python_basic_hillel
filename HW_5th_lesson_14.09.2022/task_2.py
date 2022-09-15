
num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))
num_3 = float(input('Enter third number: '))

max = ""

if num_2 < num_1 > num_3 or num_2 == num_1 > num_3 or num_2 < num_1 == num_3 or num_2 == num_1 == num_3:
    max =  num_1
elif num_1 < num_2 > num_3 or num_1 < num_2 == num_3:
    max = num_2
elif num_1 < num_3 > num_2:
    max = num_3
else:
    print('Unknown error')
    exit()

print(max)

