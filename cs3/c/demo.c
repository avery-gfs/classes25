#include <stdio.h>

int main() {
    char message[] = "Hello world!";

    for (int i = 0; message[i] != '\0'; i++) {
        if (message[i] >= 97 && message[i] <= 122) {
            printf("%c\n", message[i] - 32);
        } else {
            printf("%c\n", message[i]);
        }
    }
}
