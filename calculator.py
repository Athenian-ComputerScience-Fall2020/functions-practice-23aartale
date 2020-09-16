#collaborators: Jack Chen, Ryan Abar

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

print("select your opperation: ")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")


option = int(input("Enter option 1/2/3/4 "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if option == (1):
    print(addition(a, b))

elif option == (2):
    print(subtraction(a, b))

elif option == (3):
    print(multiplication(a, b))

elif option == (4):
    print(division(a, b))

else:
    print("You did not pick 1,2,3,4 for your option")
            




