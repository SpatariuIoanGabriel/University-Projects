#include "complex_number.h"
#include <sstream>
#include <iomanip>
#include <cmath>
#include <string>
using namespace std;

Complex::Complex(){
	this->real = 0;
	this->imag = 0;
}

Complex::Complex(float real, float imag) {
	this->real = real;
	this->imag = imag;
}
float Complex::getReal() const{
	return this->real;
}

float Complex::getImag() const {
	return this->imag;
}

void Complex::setReal(float real) {
	this->real = real;
}

void Complex::setImag(float imag) {
	this->imag = imag;
}

Complex Complex::conjugate() const{
	return Complex(this->real, -this->imag);
}

Complex Complex::add(Complex c) const {
	return Complex(this->real + c.real, this->imag + c.imag);
}

Complex Complex::subtract(Complex c) const {
	return Complex(this->real - c.real, this->imag - c.imag);
}

Complex Complex::multiply(Complex c) const {
	Complex c3;
	c3.real = this->real * c.real - (this->imag * c.imag);
	c3.imag = this->real * c.imag + this->imag * c.real;
	return c3;
}

void Complex::multiply(float s) {
	this->real *= s;
	this->imag *= s;
}

bool Complex::equals(Complex c) const{
	return this->real == c.real && this->imag == c.imag;
}

float Complex::magnitude() {
	return sqrt(this->real * this->real + this->imag * this->imag);
}

float Complex::phase() {
	return atan2(this->imag, this->real);
}

void Complex::toPolar(float *r, float *theta) {
	*r = this->magnitude();
	*theta = this->phase();
}

string Complex::toString() const {
	ostringstream sstr;
	float eps = 0.0001;
	if (fabs(this->real) < eps && fabs(this->imag) < eps) {
		sstr << 0;
		return sstr.str();
	}
	sstr << std::setprecision(2) << std::fixed;
	if (this->imag < 0) {
		sstr << this->real << this->imag << "i";
		return sstr.str();
	}
	sstr << this->real << "+" << this->imag << "i";
	return sstr.str();
}

Complex Complex::operator-(const Complex& c) const {
	return Complex(this->real - c.getReal(), this->imag - c.getImag());
}

Complex Complex::operator*(const Complex& c) const {
	Complex c3;
	c3.real = this->real * c.real - (this->imag * c.imag);
	c3.imag = this->real * c.imag + this->imag * c.real;
	return c3;
}

Complex operator+(const Complex& c1, const Complex& c2) {
	return Complex(c1.real + c2.real, c1.imag + c2.imag);
}

std::istream& operator>> (std::istream& in, Complex& c) {
	/*int it = 1;
	float x, y = 0, z = 0;
	while (in >> x) {
		if (it == 1)
			y = x;
		else
			z = x;
	}
	c.real= y;
	c.real = z;*/
	in >> c.real >> c.imag;
	return in;
}

std::ostream& operator<< (std::ostream& out, const Complex& c) {
	out << c.toString();
	return out;
}