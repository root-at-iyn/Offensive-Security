/* This program computes the volume of a sphere with a 10 metre radius.
 * The formula to calculate the volume: v = 4/3(pi * r^3). 
 *
 * While the orginal program getSphereVolume works, it's not flexible at the moment.
 * Every time we want to change the radius value, the program would need to be re-complied.
 * This program introduces the scanf function, which can be used to prompt the user for a radius value
 * The radius value is fed into the function  */

# include <stdio.h>

double radius = 0;          // We give radius an initial value of 0. The value will be modified after the value is received from the user by scanf. The type is changed to double to allow more precision
double pi = 3.14159, v;     // We can declare, initialize (or both) multiple variables of the same type on one line

int main (int argc, char *argv[]) {
    printf("Enter a radius value: ");   // Print the message on the terminal to the user
    
    scanf("%lf", &radius) ;  // Get the radius value entered by the user. The `&` (address of) operator is used to save the input into the memory location of the variable radius.
                             // The format specifier `%lf` tells scanf to only accept numerical input of type double. This will also accept regular integers.
    
    v = 4.0/3.0 * (pi * (radius * radius * radius));       // The expression of the formulas calculation  is saved into the variable `v`
    
    printf("The volume of a sphere given a radius of %.1f metres is: %.2f\n", radius, v);                           
}

/* The output when running the program should be similar to:
 *
 * Enter a radius value: 10
 * The volume of a sphere given a radius of 10.0 metres is: 4188.79
 *
*/
