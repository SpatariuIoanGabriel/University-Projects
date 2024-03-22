#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include "complex_test.h"

int comparator(const void* a, const void* b) {
	if (((Complex*)a)->real - ((Complex*)b)->real < 0)
		return -1;
	return 1;
}

int comparator1(const void* a, const void* b) {
	if (((Complex*)a)->imag - ((Complex*)b)->imag < 0)
		return -1;
	return 1;
}

int comparator2(const void* a, const void* b) {
	if (complex_mag(*(Complex*)a) - complex_mag(*(Complex*)b) < 0)
		return -1;
	return 1;

}

int main(int argc, char** argv) {

	run_complex_tests(true);

	Complex c1 = complex_create(1, 1);

	float mag = complex_mag(c1);
	printf("c1 mag: %f\n", mag);

	float phase = complex_phase(c1);
	printf("c1 phase: %f\n", phase);

	Complex conjugate = complex_conjugate(c1);
	printf("c1 conjugate: ");
	complex_display(conjugate);

	complex_scalar_mult(&c1, 5);
	printf("c1 multiply with scalar 5: ");
	complex_display(c1);

	float r, ang;
	complex_to_polar(c1, &r, &ang);
	printf("polar coordinates are: radius %f and angle %f\n", r, ang);


	Complex *c2 = (Complex*)malloc(sizeof(Complex));

	*c2 = complex_create(1, -1);

	float mag2 = complex_mag(*c2);
	printf("c2 mag: %f\n", mag2);

	float phase2 = complex_phase(*c2);
	printf("c2 phase: %f\n", phase2);

	Complex conjugate2 = complex_conjugate(*c2);
	printf("c2 conjugate: ");
	complex_display(conjugate2);

	complex_scalar_mult(c2, 7);
	printf("c2 scalar_mult: ");
	complex_display(*c2);

	float r2, ang2;
	complex_to_polar(c1, &r2, &ang2);
	printf("polar coordinates are: radius %f and angle %f\n", r2, ang2);

	printf("c1 + c2 = ");
	complex_display(complex_add(c1, *c2));

	printf("c1 - c2 = ");
	complex_display(complex_subtract(c1, *c2));

	printf("c1 * c2 = ");
	complex_display(complex_multiply(c1, *c2));
	
	free(c2);
	if (argc != 2) {
		printf("Usage invalid");
		return 0;
	}
	FILE* fp = fopen(argv[1], "r");
	if (fp == NULL) {
		printf("Couldn't open the file");
		return 0;
	}
	const int length = 1000;
	Complex* container = (Complex*) malloc(length * sizeof(Complex));
	int it = 0;
	while (!feof(fp)) {
		Complex c;
		fscanf(fp, "%f%f", &c.real, &c.imag);
		container[it] = c;
		it++;
	}
	
	qsort(container, it, sizeof(Complex), comparator);

	printf("\n\nsort after real part:\n\n");

	for (int i = 0; i < it; i++)
		complex_display(container[i]);

	qsort(container, it, sizeof(Complex), comparator1);

	printf("\m\nsort after imaginary part:\n\n");
	
	for (int i = 0; i < it; i++)
		complex_display(container[i]);

	qsort(container, it, sizeof(Complex), comparator2);

	printf("\nsort after maginitude:\n\n");

	for (int i = 0; i < it; i++)
		complex_display(container[i]);

	free(container);
	return 0;
}