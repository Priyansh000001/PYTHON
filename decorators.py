# decorators 
# In Python, decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code.
# A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
# Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional
# functionality to existing functions or methods in a clean, reusable way.

# def my_decorator(display):
#     def wrapper():
#         print("This task will run before the main funtion runs")
#         display()
#         print("This is task which will run after the main funtion runs")
#     return wrapper
# @my_decorator
# def display():
#     print("this is another task")
#     print("this is the display function")
# display()

# def decorator(func):
#     def wrapper(a, b):
#         print("This task will run before the main function runs")
#         result = func(a, b)
#         print("This task will run after the main function runs")
#         return result
#     return wrapper
# @decorator
# def multiply(a, b):
#      print(a * b)

# def add(a, b):
#     print(a + b)
# add(2,5)
# multiply(2, 3)

# def log(func):
#     def wrapper(username,amount):
#         print(f"user name :{username}")
#         print(f"the transaction time {datatime.datatime.now()}")
#         func(username,amount)
#         print("transaction completed successfully")
#     return wrapper
# @log
# def deposit(user,amount):
#     print(f"the {amount} deposited {user}")

# def withdraw(user,amount):
#     print(f"the {amount} withdrawn by {user}")
# withdraw("john_doe",100)

