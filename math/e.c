#include <stdio.h>
#include <math.h>


double e(int n) {
	return pow((1+1/n),n);
}




int main() {

	printf("%f", e(2));


	return 0;
}
