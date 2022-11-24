# include <stdio.h>

int main() {
   int foo = 2147445026;
   foo += 507917;
   printf("%d\n", foo);
   printf("The size of foo is: %lu\n", sizeof(foo));
}
