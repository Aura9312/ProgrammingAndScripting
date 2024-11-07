def greet():
    print("Hello, welcome to the functions lab!")

greet()

def greet(name):
    print(f"Hello {name}! Welcome to the functions lab!")

greet("Alice")

def add_numbers(a, b):
    result = a +b
    return result

sum_result = add_numbers(5, 3)
print ("Sum: ", sum_result)

square = lambda x: x*x

print("Square of 5: ",square(5))

def max_of_two(x,y):
    return max(x,y)

max_of_two(10,20)

def calculate(num1, num2, operation):
    if operation == "add":
        return num1+num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    else:
        return num1 / num2

print("Your calculation is: ",calculate(5,4,"add"))
print("Your calculation is: ",calculate(5,4,"subtract"))
print("Your calculation is: ",calculate(5,4,"multiply"))
print("Your calculation is: ",calculate(5,4,"divide"))

def assign_grade():
    student_test_score = int(input("What score did the student achieve? "))
    res = lambda rangecheck: (0 < rangecheck < 100)
    resString = " "
    if not res(student_test_score):
        resString = "Invalid Score"
    else:
        if student_test_score < 60:
            resString = "F"
        elif student_test_score < 70:
            resString = "D"
        elif student_test_score < 80:
            resString = "C"
        elif student_test_score < 90:
            resString = "B"
        else:
            resString = "A"
    print(f"Student result was: {resString}")

assign_grade()


def is_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

numEvOdd = int(input("Please input a number: "))
print("Your number is: ",is_even(numEvOdd))
print(is_even(4))
print(is_even(5))

temperature_classify = lambda tempcheck: "Warm" if (tempcheck <= 25 and not tempcheck <= 10) else "Hot" if (tempcheck >= 10) else "Cold"

print(temperature_classify(15))
print(temperature_classify(5))
print(temperature_classify(45))

