def say_hello():
    print("Hello World")


def say_hello_name(name):
    print("Hello", name)

# say_hello()


'''
say_hello_name("Pawan")
say_hello_name("Kartik")
say_hello_name("Adi")

'''


def addTwo(num1, num2):
    ans = num1 + num2
    print(ans)


def add_two_with_return(num1, num2):
    ans = num1 + num2
    return ans


addTwo(10, 15)
addTwo(100, 35)

sum = add_two_with_return(10, 15)
print("Sum with return function = ", sum)
