#include "complex_number.h"
#include <math.h>
#include <stdio.h>

Complex complex_create(float real, float imag) {
	Complex c;
	c.real = real;
	c.imag = imag;
	return c;
}

float get_real(Complex c) {
	return c.real;
}

float get_imag(Complex c) {
	return c.imag;
}
void set_real(Complex* c, float real) {
	c->real = real;
} 
void set_imag(Complex* c, float imag) {
	c->imag = imag;
}
Complex complex_conjugate(Complex c) {
	c.imag = -(c.imag);
	return c;
}
Complex complex_add(Complex c1, Complex c2) {
	Complex c3;
	c3.real = c1.real + c2.real;
	c3.imag = c1.imag + c2.imag;
	return c3;
}
Complex complex_subtract(Complex c1, Complex c2) {
	Complex c3;
	c3.real = c1.real - c2.real;
	c3.imag = c1.imag - c2.imag;
	return c3;
}
Complex complex_multiply(Complex c1, Complex c2) {
	Complex c3;
	c3.real = c1.real * c2.real - (c1.imag * c2.imag);
	c3.imag = c1.real * c2.imag + c1.imag * c2.real;
	return c3;
}
bool complex_equals(Complex c1, Complex c2) {
	if (c1.real == c2.real && c1.imag == c2.imag)
		return true;
	return false;
}
void complex_scalar_mult(Complex* c, float s) {
	c->real *= s;
	c->imag *= s;

}
float complex_mag(Complex c) {
	return sqrt(c.real * c.real + c.imag * c.imag);
}
float complex_phase(Complex c) {
	return atan2(c.imag, c.real);
}
void complex_to_polar(Complex c, float* r, float* theta) {
	*r = complex_mag(c);
	*theta = complex_phase(c);
}
void complex_display(Complex c) {
	if (c.imag == 0) {
		printf("%.f", c.real);
		return;
	}
	if(c.imag < 0)
		printf("%.f + (%.f)i\n", c.real, c.imag);
	else
		printf("%.f + %.fi\n", c.real, c.imag);
}
