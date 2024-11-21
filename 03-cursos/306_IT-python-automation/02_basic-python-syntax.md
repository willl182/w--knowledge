---

# Basic Python Syntax

---

This module covers essential Python programming concepts related to data handling, functions, and decision-making structures. Below are the main ideas and relevant definitions:

*1. Key Concepts*:
- **Data Types**: Different kinds of data that Python can manipulate, such as integers, floats, strings, and booleans.
- **Type Conversion**: The process of converting one data type to another, like changing a string to an integer.
- **Variables**: Named references that store data values, allowing for easy access and manipulation.

*2. Functions*:
- **Defining Functions**: Creating reusable blocks of code that can be executed whenever needed.
- **Parameters**: Inputs that a function can take to perform its operations.
- **Return**: A statement used to send back a result from a function to the calling code.
- **Code Reuse**: The practice of writing functions to avoid repeating code and enhance efficiency.

*3. Code Style and Refactoring*:
- **Refactoring**: The process of restructuring existing code without changing its behavior to make it more readable and maintainable.
- **Comments**: Notes within the code that provide explanations or context, improving code clarity.

*4. Comparisons and Conditional Logic*:
- **Equality and Logical Operators**: Tools to compare data and make decisions based on conditions:
  - **Equality Operators**: `==`, `!=`
  - **Logical Operators**: `and`, `or`, `not`
- **Branching with Conditionals**:
  - **if**: Executes a block of code if a condition is true.
  - **else**: Provides an alternative block if the `if` condition is false.
  - **elif**: Allows checking multiple conditions in sequence.

This module emphasizes understanding and manipulating data, creating efficient and reusable code with functions, and applying logical operations for decision-making in Python.

## Expressions and Variables

### Basic Python syntax

This section emphasizes the importance of mastering Python syntax and basic programming concepts. Here's a breakdown of the main ideas and relevant definitions:

*1. Programming Foundations*:
- **Syntax**: The set of rules that defines the structure and arrangement of code in a programming language. Similar to learning a spoken language, understanding syntax is crucial to effectively communicating with a computer.
- **Basic Concepts**: The focus is on core programming elements like:
  - **Variables**: Containers for storing data values.
  - **Expressions**: Combinations of variables and operators that produce a result.
  - **Functions**: Reusable pieces of code designed to perform specific tasks.
  - **Conditional Blocks**: Code structures (like `if` statements) that allow for decision-making based on conditions.

*2. Approach to Learning Programming*:
- Learning to code requires continuous practice and immersion, similar to acquiring a new spoken language. It involves:
  - Breaking down complex concepts into manageable parts.
  - Gradually building skills through exercises and practice.
  - Combining simple constructs to tackle more complex problems over time.

*3. Practice and Skill Development*:
- Emphasizes the importance of repetitive practice to strengthen programming skills, just like physical training at a gym.
- Encourages learners to revisit concepts through videos and quizzes as many times as needed to reinforce understanding.

Overall, this section is a reminder that programming is a skill developed over time with practice, and that understanding basic syntax is the first step toward building more complex and powerful code.

### Python Syntax

This reading introduces the basics of Python syntax, semantics, and best practices, emphasizing their importance for effective programming and communication with computers.

*1. Python as a Language*:
- **Syntax**: The set of rules for structuring code in Python, including words, punctuation, and their arrangement. Correct syntax is essential for the computer to interpret commands.
- **Semantics**: The meaning conveyed by the code written in proper syntax. It determines what the code is actually instructing the computer to do.
- Learning Python’s syntax and semantics is similar to learning a spoken language—requiring practice, exposure, and familiarity with how instructions are communicated.

*2. Basic Elements of Python Syntax*:
- **Variables**: Names representing stored data. Variables can hold different data types like strings, tuples, lists, dictionaries, and objects.
- **Keywords**: Reserved words in Python that have specific purposes (e.g., `in`, `not`, `or`, `for`, `while`, `return`).
- **Operators**: Symbols used for performing operations (e.g., `+`, `-`, `*`, `/`, `**`, `%`, `//`, `<`, `>`, `==`,).
- **Expressions**: Combinations of variables, numbers, and operators that return a result when evaluated.
- **Functions**: Groups of statements designed to perform tasks and return values. Functions allow for code reuse and organization.

```python
def to_celsius(x):
   '''Convert Fahrenheit to Celsius'''
   return (x-32) * 5/9
to_celsius(75)
```

- **Conditional Statements**: Code that guides the program's flow based on conditions, using structures like `if`, `elif`, and `else`.


```python
number = -4
if number > 0:
    print('Number is positive.')
    elif number == 0:
    print('Number is zero.')
    else:
print('Number is negative.')
```

*3. Common Errors and Conventions*:
- Incorrect syntax or misuse of keywords leads to syntax errors.
- Naming rules help standardize code for readability:
  - Names should avoid spaces and should use snake_case (e.g., `student_name`).
  - Descriptive names are preferred for clarity.
  - Names cannot start with a number and should mix upper and lower case appropriately.

```python
print(This will throw an error because I didn’t make it a string.)
```

*4. Best Practices in Python*:
- **The Zen of Python**: A set of principles guiding Python code design, emphasizing readability, simplicity, and clarity. Key ideas include:
  - Simple is better than complex.
  - Readability is crucial.
  - Errors should not be ignored unless explicitly handled.
  - There should be one clear way to do something, even if it isn’t immediately obvious.

- **PEP 8**: A comprehensive style guide for Python, covering best practices for writing clean and readable code. PEP (Python Enhancement Proposals) offers standards to guide the development and maintenance of Python code, especially as it is an open-source language.

*5. Key Takeaways*:
- Mastery of Python syntax and semantics is fundamental to becoming proficient in programming.
- Familiarity with Python's naming conventions, best practices, and resources like the PEP 8 guide will enhance your ability to write clear and effective code.
- Continuous exposure, practice, and adherence to coding principles are crucial for learning Python and leveraging it for data analysis and other tasks.


### Data Types in Python

This reading focuses on the concept of data types in Python, explaining their significance, usage, and potential pitfalls. Understanding how Python categorizes and manages data is crucial for effective programming.

#### **1. Definition of Data Types**:
Data types in Python categorize and represent various forms of information that a program can manipulate. Common data types include:
- **String** (`str`): A sequence of characters enclosed in quotes. It is used to represent text data.
- **Integer** (`int`): A whole number without a decimal or fractional component (e.g., 1, 42, -5).
- **Float** (`float`): A real number that includes a decimal or fractional part (e.g., 3.14, -2.5).

#### **2. Handling Different Data Types**:
- Mixing incompatible data types, such as trying to add an integer and a string, will cause errors. For example, `7 + "8"` will trigger a `TypeError`.
- Errors are a normal part of programming. They act as indicators that guide programmers to correct and understand code issues.
- The error message in the example tells us that Python cannot perform operations between different data types unless explicitly converted or handled.

#### **3. Importance of Consistency in Data Types**:
- Each data type has a specific function and meaning. For example, a file name would use a string, while its size would be an integer.
- When working with code—especially code written by someone else—it is essential to verify data types to avoid unexpected behavior. The `type()` function in Python can be used to check the data type of a variable.

#### **4. Common Data Types**:
- **String (`str`)**: Text data enclosed in single, double, or triple quotes.
- **Integer (`int`)**: Whole numbers without a decimal.
- **Float (`float`)**: Numbers with a decimal point.

#### **5. Best Practices**:
- Keep data types consistent within operations. For instance, add integers to integers, concatenate strings with strings, and avoid mixing incompatible types.
- Use the `type()` function to clarify the data type when in doubt, which is particularly useful when handling unfamiliar or complex code.
- Data types provide structure to the information, enabling Python to manage and manipulate data effectively.

The reading emphasizes that while only a few data types are introduced here, more will be covered as programming skills advance. Understanding how to work with basic data types forms the foundation for managing more complex data structures in the future.



The code raises an error because in Python, you cannot directly add an integer to a string using the `+` operator. In this example:

```python
print("1234" + 5678)
```

Here’s why the error occurs:

- `"1234"` is a **string** (text enclosed in quotes).
- `5678` is an **integer** (a whole number).

*Explanation*:
Python uses the `+` operator for different purposes depending on the data types:
- When both operands are **strings**, the `+` operator performs **concatenation** (joining the strings).
  - Example: `"123" + "456"` results in `"123456"`.
- When both operands are **numbers** (integers or floats), the `+` operator performs **arithmetic addition**.
  - Example: `123 + 456` results in `579`.

In the example `print("1234" + 5678)`, Python doesn't know whether it should concatenate (like it does with strings) or perform addition (like with numbers). Therefore, it raises a `TypeError`, indicating that you cannot combine a `str` (string) and an `int` (integer) directly.

*Solution*:
If you want to concatenate the number with the string, you must first **convert the number to a string** using the `str()` function:

```python
print("1234" + str(5678))
```

This would output:
```
12345678
```

Alternatively, if the intention was to perform arithmetic, you would need both operands to be numbers:

```python
print(1234 + 5678)
```

This would output:
```
6912
```

*Correct Answer*:
The first choice is correct:
> **Because Python doesn't know how to add an integer or float data type to a string.**

### Type Annotation in Python

**Type annotation** is a way to specify the expected data type for variables and function arguments in Python. It acts as a label, helping developers understand what kind of data a variable should hold. While Python is a dynamically typed language (meaning variables can change type), annotations offer clarity, reduce errors, and enhance code readability. Here are the key concepts:

Key Concepts

1. **Type Annotation**:
   - Type annotation is like labeling a container to specify what type of content it should hold. 
   - Example: `name: str = "Betty"` indicates that `name` should be a string (`str`), and `"Betty"` confirms this expectation.
   - Another example: `age: int = 34` uses `int` to annotate that `age` should store an integer.

2. **Benefits of Type Annotations**:
   - **Reduces errors** by clarifying expected data types.
   - **Improves documentation** for others to understand the code easily.
   - **Supports IDEs** and tools like linters to provide better feedback, catching potential mistakes.

3. **Dynamic Typing**:
   - Python does not require fixed variable types, allowing flexibility. 
   - Example:
```python
a = 3           # 'a' is an integer
a = "Hello"     # 'a' changes to a string
```
   - This flexibility enables faster coding but requires caution.

4. **Duck Typing**:
   - In Python, if a variable "acts like" a certain type, it is treated as that type—this is called **duck typing**.
   - Python infers a variable’s type at runtime based on its behavior.

5. **Ways to Annotate Variables**:
   - **Type Comments**: Annotations can be added as comments without affecting code execution.
```python
captain = "Picard"  # type: str
```
   - **Direct Annotation**: Adding the annotation directly to the variable.
```python
captain: str = "Picard"
```
   - Direct annotation is more modern and allows for better integration with tools that check for type consistency.

6. **Type Annotations in Practice**:
   - Useful for complex programming tasks (e.g., object-oriented programming) or function definitions.
   - In data science, annotating every variable can be burdensome, so it's often limited to functions or specific contexts.

7. **Impact on Runtime**:
   - Annotations do not enforce type restrictions at runtime but increase **computational overhead** when integrated with tools that analyze code.
   - Use annotations strategically to avoid performance issues.

*Key Takeaways*

- Type annotations improve code **clarity**, making it easier to read and maintain.
- Python offers multiple ways to annotate variables: choose the one that fits your context, whether it's direct annotation or type comments.
- Avoid excessive annotations, especially in contexts where it could slow down performance, like data processing.

In conclusion, type annotations are a helpful tool in Python, particularly when writing functions or engaging in complex programming. They bring structure to a dynamically typed language while allowing developers to maintain flexibility.



### Data Type Operations and Conversions in Python

Python handles operations between data types with **implicit and explicit conversions**, allowing some types to interact seamlessly while others require a specific transformation. Here’s a breakdown of the core concepts and definitions:

*Key Concepts*

1. **Data Type Compatibility**:
   - You **cannot** use the `+` operator directly between different types, such as an integer and a string, as this will raise an error.
   - However, Python allows operations between an **integer** and a **float** without error because of automatic conversion.

2. **Implicit Conversion**:
   - When an operation involves a **float** and an **integer**, Python will automatically convert the integer into a float. 
   - This conversion is called **implicit conversion**, where Python adjusts the data type behind the scenes to make the operation compatible.
   - Example:
```python
result = 7 + 3.5  # The integer 7 is implicitly converted to 7.0 (a float)
```
   - The result in such operations is a float.

3. **String Concatenation**:
   - The `+` operator can also concatenate (join) strings together.
   - When combining strings, make sure to add spaces manually, as Python will not do this by default.
   - Example:
```python
greeting = "Hello" + " " + "world!"  # Output: "Hello world!"
```

4. **Explicit Conversion**:
   - If you need to combine a **string** with a number (like an integer or float), you must perform an **explicit conversion**.
   - This involves using a type conversion function, such as `str()`, `int()`, or `float()`.
   - Example:
```python
number = 42
message = "The answer is " + str(number)  # Converts 42 to "42" for concatenation
```
   - Without explicit conversion, an error would occur when trying to concatenate a string with a number.

*Definitions*

- **Implicit Conversion**: Automatic conversion of one data type to another by Python during operations, such as converting an integer to a float when performing mixed arithmetic.
- **Explicit Conversion**: Manual conversion of one data type to another using a function like `str()`, `int()`, or `float()`.

*Key Takeaway*

Python allows operations between compatible types using implicit conversion and requires explicit conversion when combining incompatible types (like strings and numbers). Understanding these conversion rules is crucial for avoiding errors and ensuring correct data manipulation in Python programming.


In this example, you calculated the **average size of files** using basic arithmetic operations and demonstrated how to handle **data type conversions** in Python to produce a user-friendly output.

Here's a breakdown of the key steps involved:

1. **Summing Values**:
   - You began by adding up the sizes of each file using the `+` operator. This step illustrated how Python handles summing a series of integers.
   - Calculation:
```python
total = 2048 + 4357 + 97658 + 125 + 8
# Result: total = 104196
```

2. **Calculating the Average**:
   - The `average` was calculated by dividing the total file size by the number of files. Since division in Python with the `/` operator returns a float, the result retains any decimal part.
   - Calculation:
```python
files = 5
average = total / files  # 104196 / 5 = 20839.2
```

3. **String Conversion for Output**:
   - To concatenate a number with a string (for user-friendly output), you used the `str()` function to **explicitly convert** the numerical average into a string. Without this conversion, Python would raise a `TypeError`.
   - Output statement:
```python
print("The average size is:" + str(average))
# Output: "The average size is:20839.2"
```

*Concepts Illustrated*

- **Basic Arithmetic**: Summing numbers and calculating an average using simple arithmetic operations (`+`, `/`).
- **Data Type Conversion**: Converting a number (float) to a string using `str()` to enable concatenation with other strings.
  
*Key Takeaway*

By converting the numerical result to a string using `str()`, you created a smooth user-friendly message output, illustrating how important **explicit data type conversion** is when handling mixed types in Python. Keep practicing these concepts to become more familiar with Python's data handling!


### Implicit vs Explicit Conversion

In Python, data types can be converted from one form to another, either **implicitly** or **explicitly**. Here are the main concepts:

1. **Implicit Conversion**:
   - This is when Python **automatically** converts one data type to another without any explicit instructions from the programmer.
   - Example: When an integer is combined with a float, Python will convert the integer to a float automatically to perform the operation.

2. **Explicit Conversion**:
   - This is when the programmer **manually** converts a data type using a specific function.
   - Example: To combine a number with a string, you must use functions like `str()` to convert the number to a string before concatenation.

*Key Takeaway*

Implicit conversion simplifies operations but can sometimes lead to unexpected results. Explicit conversion gives the programmer control, ensuring data types are handled correctly for specific operations.


### Studi Guide Expressions and Variables

This guide provides a summary of key concepts from the lesson on **expressions**, **variables**, and **data types**.

*Key Concepts*

1. **Expression**: 
   - A combination of numbers, symbols, or values that, when evaluated, produce a result.

2. **Data Types**: 
   - Classes of data, such as **string**, **integer**, **float**, and **Boolean**, each with specific properties and behaviors.

3. **Variable**:
   - An instance of a data type that stores changeable values, represented by a unique name.

4. **Implicit Conversion**:
   - Automatic conversion between data types by the Python interpreter (e.g., adding an integer to a float results in a float).

5. **Explicit Conversion**:
   - Manually converting one data type to another using conversion functions:
     - `str()` - Converts a value to a string.
     - `int()` - Converts a value (usually float) to an integer.
     - `float()` - Converts a value (usually integer) to a float.

6. **Type Annotations**:
   - Optional in Python, but they clarify variable types, making code easier to read and reducing errors. They use the `typing` module and can be used for more complex types like lists or tuples.

*Skills Learned*

1. **Using Variables**:
   - Store values and perform arithmetic operations.

```python
# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests

# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type
```

2. **Explicit Conversion**:
   - Convert values between types (e.g., from float to string).

```
# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.
```

3. **Handling Errors**:
   - **TypeError**: Caused by type mismatches (e.g., trying to add a string and integer).
   - **ZeroDivisionError**: Caused by division by zero, which should be handled appropriately.

```
# The following code causes a type error between a string 
# and an integer:

print("5 * 3 = " + (5*3)) 


# Resolution: 
# print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string. 
```

```
numerator = 7
denominator = 0   # Possible resolution: Change the denominator value 
result = numerator / denominator
print(result)


# One possible assumption for a number divided by zero error might
# include the issue of a null value as a denominator (could happen when
# using a loop to iterate over values in a database). In such cases, the
# desired outcome may be to leave the numerator value intact. The
# numerator value can be preserved by reassigning the denominator with 
# the integer value of 1. The result would then equal the numerator.
```


*Example of Type Annotations:*
```python
import typing
z: str = "Hello, world!"
x: int = 10
y: float = 1.23
list_of_numbers: typing.List[int] = [1, 2, 3]
```

*Key Takeaway:*
Understanding data types and conversions is crucial in programming. Using **explicit conversion** functions and handling **common errors** (like type mismatches and division by zero) ensures code runs smoothly. Type annotations help clarify the code for both developers and tools.


### Quiz

Here are the answers for each question:

### Question 1:
**Problem**: This code should display `2 + 2 = 4`, but there is an error in the code due to an incorrect string concatenation.
- **Fix**: The correct code is:
```python
print("2 + 2 = " + str(2 + 2))
```
  **Explanation**: The expression `2 + 2` is evaluated first, and then the result is converted to a string using `str()` and concatenated with the rest of the message.

### Question 2:
**Problem**: You need to calculate the tip, total amount, and each friend's share correctly and ensure proper data type conversion for the final output.
- **Fix**: The correct code is:
```python
bill = 47.28  # Bill amount
tip = bill * 0.15  # 15% tip
total = bill + tip  # Total bill with tip
share = total / 2  # Split the total between two friends
print("Each person needs to pay: " + str(round(share, 2)))  # Corrected to round the result to 2 decimal places
```
  **Explanation**: The `round(share, 2)` function is used to ensure that the share is displayed with two decimal places.

### Question 3:
**Problem**: The code is designed to divide two equal numbers, and the result is expected to be `1`, but the logic is correct, and there is no actual error in the code. The output is correctly `1.0`.
- **Fix**: No fix is needed, as the original code works correctly:
```python
numerator = 10
denominator = 10
result = numerator / denominator
print(result)
  ```
  **Explanation**: `10 / 10` evaluates to `1.0` (float).

### Question 4:
**Problem**: The goal is to display the sentence `How do you like Python so far?` by combining the variables correctly.
- **Fix**: The correct code is:
```python
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6 + " " + word7)
```
  **Explanation**: Each word is concatenated with spaces in between to form the complete sentence.

### Question 5:
**Question**: What do you call a combination of numbers, symbols, or other values that produce a result when evaluated?
- **Answer**: **An expression**
  **Explanation**: An **expression** is a combination of numbers, variables, or operators that Python can evaluate to produce a result.


### Functions


