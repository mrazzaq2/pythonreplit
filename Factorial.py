def calculate_factorial(number):
  factorial = 1
  if number < 0:
      print("Factorial is not defined for negative numbers")
  else:
      for i in range(1, number + 1):
          factorial *= i
      return factorial

num= int(input())
result = calculate_factorial(num)
print(f"The factorial of {num} is: {result}")
