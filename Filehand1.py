#!/usr/bin/env python
# coding: utf-8

# In[23]:


# exersise 2 . Contents copied from one file to another


with open('C:\\Users\\mumth\\Pythonfilesnew\\TheLittlePlant.txt','r',encoding='utf-8') as file1:
    contents = file1.read()
    
with open('C:\\Users\\mumth\\Pythonfilesnew\\TheWiseOld Man.txt','w',encoding='utf-8') as copy:
    copy.write(contents)

    print("Contents copied from one file to another")
    
with open('C:\\Users\\mumth\\Pythonfilesnew\\TheWiseOld Man.txt','r',encoding='utf-8') as copy_read:
    file_copy =copy_read.read()
    print(file_copy)


# In[29]:


#read a file
with open('C:\\Users\\mumth\\Pythonfilesnew\\TheWiseOld Man.txt','r',encoding='utf-8') as file:
    content = file.read()
    print(content)


# In[40]:


#exersise 3
with open('C:\\Users\\mumth\\Pythonfilesnew\\TheWiseOld Man.txt','r',encoding='utf-8') as file3:
 content1=file3.read()
 words = content1.split()
 word_count = len(words)
 print(f"The total number of words in the file is: {word_count}")


# In[50]:


#word count
def count_word_occurrences(file_path, target_word):
    try:
        
        with open(file_path, 'r', encoding='utf-8') as file:
           
            content = file.read()
            
        
        content = content.lower()
        target_word = target_word.lower()
        
        
        words = content.split()
        
       
        word_count = words.count(target_word)
        
        print(f"The word '{target_word}' appears {word_count} times in the file.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'C:\\Users\\mumth\\Pythonfilesnew\\TheWiseOld Man.txt'


target_word = 'seed'

count_word_occurrences(file_path, target_word)


# In[58]:


#covert to an intiger
def convert_to_integer():
    try:
        
        user_input = input("Enter a string to convert to an integer: ")
        
       
        number = int(user_input)
        
        
        print(f"The input '{user_input}' was successfully converted to the integer: {number}")
    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        print(f"Error: The input '{user_input}' is not a valid integer.")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")



convert_to_integer()


# In[60]:


#check negtive value
def check_for_negatives():
    try:
        
        user_input = input("Enter a list of integers separated by commas: ")
        
        
        numbers = [int(num.strip()) for num in user_input.split(",")]
        
        
        for num in numbers:
            if num < 0:
                raise ValueError(f"Negative number found: {num}")
        
        print("All numbers are valid (non-negative).")
    except ValueError as e:
        # Handle negative numbers or invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")


check_for_negatives()


# In[11]:


#avrg of intigers exersice 7
def main():
    try:
       
        user_input = input("Enter a list of integers separated by spaces: ")
        
       
        numbers = [int(x) for x in user_input.split()]
        
        if len(numbers) == 0:
            raise ValueError("The list is empty. Cannot compute average.")
        
        # Compute the average
        average = sum(numbers) / len(numbers)
        
        print(f"The average of the entered integers is: {average}")
    
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("The program has finished running.")

if __name__ == "__main__":
    main()


# In[13]:


def main():
    try:
        # Prompt the user to input a filename
        filename = input("Enter the filename to write to: ")

        # The content to write to the file
        content = "Hello, this is a sample text written to the file!"

        # Open the file in write mode and write content
        with open(filename, 'w') as file:
            file.write(content)
        
        # Print welcome message if no exception occurs
        print("File has been created and written successfully. Welcome!")

    except FileNotFoundError:
        print("Error: The specified file or path could not be found.")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("The program has finished running.")

if __name__ == "__main__":
    main()


# In[15]:


# Base class for Course exersice 9
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
    
    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Credit Hours: {self.credit_hours}")


class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
      
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_info(self):
        
        super().display_info()
        print(f"Required for Major: {'Yes' if self.required_for_major else 'No'}")


class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
       
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_info(self):
        
        super().display_info()
        print(f"Elective Type: {self.elective_type}")


def main():
    
    core_course_1 = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
    core_course_2 = CoreCourse("MATH201", "Advanced Calculus", 4, True)
    elective_course_1 = ElectiveCourse("HIST105", "World History", 3, "liberal arts")
    elective_course_2 = ElectiveCourse("CS230", "Web Development", 3, "technical")

    
    courses = [core_course_1, core_course_2, elective_course_1, elective_course_2]

    
    print("University Course Catalog:")
    print("--------------------------")
    for course in courses:
        course.display_info()
        print("--------------------------")

if __name__ == "__main__":
    main()


# In[5]:


# main.py
from employee import Employee  # Import the Employee class from the employee module

def main():
    # Create an instance of the Employee class
    emp1 = Employee("John Doe", 50000)

    # Display the employee's name and salary
    print(f"Employee Name: {emp1.get_name()}")
    print(f"Employee Salary: ${emp1.get_salary()}")

if __name__ == "__main__":
    main()


# In[ ]:




