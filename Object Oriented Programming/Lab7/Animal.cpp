#include "Animal.h"

int Animal::getAge() const
{
	return this->age;
}

void Animal::setAge(int a)
{
	this->age = a;
}

std::string Animal::toString() const
{
	return "Animal";
}

std::ostream& operator<<(std::ostream& out, const Animal& a)
{
	out << a.toString();
	return out;
}

