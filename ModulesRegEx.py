#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math
def calculate_square_root():
    try:
        number = float(input("Enter a number to find the square root: "))
        
        if number < 0:
            print("Cannot calculate the square root of a negative number.")
        else:
            square_root = math.sqrt(number)
            print(f"The square root of {number} is {square_root:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

calculate_square_root()


# In[13]:


def generate_random_number():
    random_number = random.randint(1, 100)
    print(f"Random number between 1 and 100: {random_number}")

generate_random_number()


# In[11]:


def calculate_factorial():
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial = math.factorial(number)
            print(f"The factorial of {number} is {factorial}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

calculate_factorial()


# In[9]:


# area_calculator.py
import math_operations 

def main():
    print("Area Calculations")
    print("=================")
    
    radius = float(input("Enter the radius of the circle: "))
    print(f"Area of the circle: {math_operations.area_of_circle(radius):.2f}")

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f"Area of the rectangle: {math_operations.area_of_rectangle(length, width):.2f}")

    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"Area of the triangle: {math_operations.area_of_triangle(base, height):.2f}")

if __name__ == "__main__":
    main()


# In[1]:


# temperature_calculator.py
import temperature_conversion  

def main():
    print("Temperature Conversion")
    print("======================")

    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = temperature_conversion.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
    celsius = temperature_conversion.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

if __name__ == "__main__":
    main()


# In[ ]:




