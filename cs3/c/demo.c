#include <stdio.h>

int main() {
    char message[] = "Hello world!";

    for (char* p = message; *p != '\0'; p++) {
        if (*p >= 97 && *p <= 122) {
            printf("%c\n", *p - 32);
        } else {
            printf("%c\n", *p);
        }
    }
}