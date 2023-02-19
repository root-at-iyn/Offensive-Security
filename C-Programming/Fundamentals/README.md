# Contents

1. [Intro](README.md#intro)
2. [Variables and Assigments](VARIABLES-ASSIGNMENTS.md)

# Intro

## TL;DR

- All C programs that are executable must have a main function. The main function definiton is case-sensitive and must be lowercase.
- For input and output, you need to add the include directive for the `stdio.h` header file from the C Standard library. This contains the function definitons to use functions like `printf()`.
- In C, statements are terminated with a semicolon `;`
- If your function does not require any parameters, you can add the void keyword in as the parameter to denote that no arguments are required
- Comments in C89 and C99 start with `/*` and end with `*\`. These are known as multiline comments because text within the comment start and end can span multiple lines. In C99 the inline comment `//` was introduced
- The return statement is not mandatory. On termination of the program it will still return the flow of excution back to the OS. When the return statement is included, it is used to return a value to the caller.

## First Program - Hello World

In your favourite text editior, create a file with the name `hello.c`. Open the file and the following code for the hello world example:

```
/* This is the basic hello world C program */

# include <stdio.h>

int main(void){
    printf("Hello, World\n");
    return 0;
}

```

Save the file.
If you are on Linux or MacOS, you can easily compile the C file to an executable on the CLI:

```
cc -o hello hello.c
```
This will create a binary executable file called `hello`. You can confirm it is executable by running the `file` command:

```
file hello
```
This should return something similar to the following (depending on your architecture):

```
hello: Mach-O 64-bit executable arm64
```

You can run this file in the terminal and the expected result should be `Hello, World`

```
./hello
``` 

```
Hello, World
```

