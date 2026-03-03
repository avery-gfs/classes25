#include <stdio.h>

int main() {
	int r0 = 10;
	int r1 = 1;

	while (r0 != 0) {
		r1 *= r0;
		r0 -= 1;
	}

	printf("%d\n", r1);
}
