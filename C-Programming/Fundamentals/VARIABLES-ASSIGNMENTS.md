# Working with Variables
## TL;DR
- When we want to store a value for reuse in our program we need to assign the value to a variable.
- When we assign variables, we are asking the OS to allocate memory on the stack (which is local to our running process). 
- In C, before you can use a variable, you need to `declare` the variable specifying the data type that will be stored in the variable.
- Each data type has a size which is defined in bytes. Eg. an `int` is 4 bytes and a `char` is 1 byte (a byte is 8 bits).
- When you define a variable name, this is also termed an `indentifier`. Identifiers are case-sensitive and must start with a character, eg. `a-z`, `A-Z`, or `_`
- Identifiers can include alphanumerics or underscores
- Identifiers cannot be one of the `keywords` used in the C language. Keywords in C have special meaning to the complier.
- When a program starts, uninitialsed variables are not guaranteed to be set to zero. If you haven't assigned a default value to the variable and try to use it, you may see garbage data or cause the program to crash.


## Examples

### Variable Declaration

```c
int age;    // Uninitalised variable declaration
```

### Initialised Variable Declaration
```c
double interest_rate = 4.0;     // The variable interest_rate is assigned an initial value of 4.0.
                                // A data type of double allows us to give a value with decimal points for more precision.
```

```c
char firstInitial = 'A'         // Initialisation of a char data type (single character)
```

```c
int pin[6] = {0,6,4,9,1,4}      // Initialisation of an integer data type array (with a size of 6). Arrays are discussed in more depth in ARRAYS.md 
```

### Initialising Multiple Variables

```c
int  received = 0, sent = 0; 
```

## Example Programs

There are more example programs in [variables-assignments](src/variables-assignments)
