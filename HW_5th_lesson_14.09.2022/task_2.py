
a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
c = float(input('Enter third number: '))

max = ""

if b <= a >= c:
    max = a
elif a <= b >= c:
    max = b
elif a <= c >= b:
     max = c

print(max)
