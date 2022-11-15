/* This program demontrates how we can use the printf function in C 
 * The task is to draw a checkmark using the asterix character
 * */

# include <stdio.h>


// The line defining the variable "*" declares a character array and intialises it by using the = assignment operator.
// Enclosing the * character in quotes informs the compiler this is a string literal. 
// If we used single quotes, the character would be seen as an integer representation by the compiler and given a numeric value
char star[] = "*";          

int main() {
    printf("            %s\n", star);
    printf("           %s\n", star);
    printf("          %s\n", star);
    printf("         %s\n", star);
    printf("%s       %s\n", star, star);
    printf(" %s     %s\n", star, star);
    printf("  %s   %s\n", star, star);
    printf("   %s %s\n", star, star);
    printf("    %s\n", star);
    return 0;
}

// If your are on a .nix environment, you can compile this code with
// cc -o checkMark checkMark.c
// When you compile this program, you should see the following:

/*
Fundamentals % ./bin/checkMark
            *
           *
          *
         *
*       *
 *     *
  *   *
   * *
    *
*/

