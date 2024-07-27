# Age Category Program

This simple Python program determines and outputs the age category of a user based on their input. The user is prompted to enter their age, and the program categorizes them into one of several predefined age groups.

## Key Features

### User Input
- The program prompts the user to enter their age.
- The age is read as a floating-point number to handle possible fractional ages.

### Condition Statements
- The program uses a series of if, elif, and else statements to categorize the age into one of the following groups:
- **Not Born Yet:** Age less than 0.
- **Child:** Age between 0 and 12.
- **Teenager:** Age between 13 and 19.
- **Young Adult:** Age between 20 and 29.
- **Adult:** Age between 30 and 64.
- **Senior:** Age 65 and above.

### Output

- The program prints the corresponding age category based on the input.
- A farewell message, "Bye!", is printed at the end.

## Key Concepts Covered

- **User Input:** Using `input()` to read data from the user.
- **Data Conversion:** Converting the input to a floating-point number using `float()`.
- **Conditional Statements:** Using `if`, `elif`, and `else` to handle different conditions.
- **Basic Control Flow:** Demonstrating the flow of a simple program with user interaction and decision-making.
