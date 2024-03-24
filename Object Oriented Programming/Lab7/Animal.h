#pragma once
#include "Entity.h"

class Animal : public Entity {

public:

	int getAge() const;
	void setAge(int a);
	virtual std::string toString() const;
	friend std::ostream& operator<<(std::ostream& out, const Animal& a);
	virtual EntityType what() = 0;
protected:
	int age;

};