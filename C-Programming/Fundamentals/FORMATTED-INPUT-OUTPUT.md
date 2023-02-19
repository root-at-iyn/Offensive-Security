# Formatted Input/Output

## Printf

- The `printf` function displays the contents of a string to the terminal.
- Values can be inserted at any place in the string using format specifiers.
- The values can be variables, constants or expressions
- Format specifiers placed within a string begin with `%`.
- After the string is terminated, a `,` separates the string and the `values` that should be substituted in within then format specifiers in the string
- The `%` character determines how the value will be converted from binary form to ascii and printed to the terminal.

## Format Specifiers

There are many format specifiers, but the most commonly used are:

|Specifier |  Usage
|--------- | ---------------------------------|
|%d        | Displays as printed output as decimal (base 10) integers|
|%f        | Displays output as a floating-point number (for numbers with decimal points)|
|%e        | Displays numbers in exponential format|
|%x        | Displays numbers in hexidecimal (base 16) format|
|%g        | Displays floating-point numbers in either decimal or exponential format depending on size|
|%s        | Displays string characters|
|%u        | Displays numbers as unsigned integers|


### Example

```c
# include <stdio.h>

int main(void) {
    int level = 5;
    float score = 9.5;
    char message = "Format Strings 101";

    printf("You are on level: %d\n", level);  // Print level as a decimal number
    printf("Your score is: %.1f\n", score);   // Print score as a floating-point number

    printf("The level in hex: %x\n", level);  // Print level in hex format
    printf("Message: %s\n", message);         // Print the message string (character array)
}

```


## Escape Characters

Escape characters such as `\n` are used in strings to enable control character functionality or prevent certain characters from being interpreted as control characters by the compiler. For example when a `\n` is used in a format string, the string is printed and newline added below.

### Common Escape Characters

Name          |  Character
------------- | ---------
Alert (bell)  |      \n
Backspace     |      \b
New line      |      \n
Horizonal tab |      \t


