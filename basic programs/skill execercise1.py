n=int(input("Enter a Number"))
if n==0:
    print("wrong input")
else:
    for i in range(n,n+1):
        val=n*(n*1)
        print(val)



x=0
str1="thisismycountryindia"
for i in str1:
    x=x-1
    print(str1[0:x])
for i in str1:
    x=x+1
    print(str1[0:x])

#program to print stars
def print_square(size):
    for i in range(size):
        for j in range(size):
            print('*', end=' ')
        print()

print_square(5)

#format predefined function
#decimal-define
a1=1045
a2=format(a1,'b')
print(a2)

a1=1045
a3="10100"
a2=int(format(int(a3,2),'d'))
print(a2)

a4=1045
a5=format(a4,'x')
print(a5)

#skill-1 ques-2

num = '10'
print(type(num))
converted_num = int(num)
print(type(converted_num))

print(converted_num + 20)

#skill-1 ques-1
numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = [float(num) for num in numbers.split()]
print("List of floats:", numbers_list)
average = sum(numbers_list) / len(numbers_list)
print("Average:", average)

#skill-1 ques-3
z1 = complex(2, 3)
z2 = complex(1, 2)
x = z1 + z2
print("Addition is:", x)

#skill-1 ques-4
integer_input = int(input("Enter an integer: "))
float_value = float(integer_input)
print("Integer entered:", integer_input)
print("Converted float:", float_value)

