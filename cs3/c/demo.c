#include <stdio.h>
#include <stdbool.h>

int main() {
    for (int n = 1; n <= 100; n++) {
        if (n % 15 == 0) {
            printf("fizz buzz\n");
        } else if (n % 3 == 0) {
            printf("fizz\n");
        } else if (n % 5 == 0) {
            printf("buzz\n");
        } else {
            printf("%d\n", n);
        }
    }
}
