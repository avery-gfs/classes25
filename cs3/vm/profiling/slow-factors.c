#include <stdio.h>

int main() {
	long n = 1000000000001;
	int d = 2;

	while (n > 1) {
		if (n % d) {
			d += 1;
		} else {
			printf("%d\n", d);
			n /= d;
		}
	}
}
