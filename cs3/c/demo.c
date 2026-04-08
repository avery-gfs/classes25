#include <stdio.h>

int main() {
    char greeting[] = "Hello";
    char name[] = "Avery";
    greeting[5] = '$';
    printf("%s %s!\n", greeting, name);
}
