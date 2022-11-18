/* This program computes the volume of a sphere with a 10 metre radius.
 * The formula to calculate the volume: v = 4/3(pi * r^3) */

# include <stdio.h>

int r = 10;             // Here is an example of a variable declarationa and initialization
double pi = 3.14159, v;    // We can declare, initialize (or both) multiple variables of the same type on one line

int main (int argc, char *argv[]) {
    printf("The volume of a sphere given a radius of %d metres is:%f.3\n", // The printf statement is lengthy here. The statement is broken up over multiple lines, which thankfully C allows us to do :)
            r, 4.0/3.0 * (pi * (10 * 10 * 10)));                           // The caveat here it that the quoted text including the format specifier before the first `,` needs to be on one line            
}


