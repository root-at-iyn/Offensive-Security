/* This program computes the volume of a sphere with a 10 metre radius.
 * The formula is v = 4/3(pi * r^3) */

# include <stdio.h>

int r = 10;
double pi = 3.14, v;

int main (int argc, char *argv[]) {
    printf("The volume of a sphere given a radius of %d is: %f.3\n", r, 4.0/3.0 * (pi * (10 * 10 * 10)));
}


