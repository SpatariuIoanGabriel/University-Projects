#pragma once
#include<string>
#include<iostream>


class BigInteger{

public:
    BigInteger();
    BigInteger(std::string s);

    BigInteger(const BigInteger& other);
    BigInteger& operator=(BigInteger copy);
    ~BigInteger();

    int sgn() const;
    void negate();

    BigInteger& operator++();
    BigInteger operator++(int t);

    friend std::ostream& operator<<(std::ostream& stream, BigInteger N);
    friend bool operator==(const BigInteger& A, const BigInteger& B);
    friend bool operator<(const BigInteger& A, const BigInteger& B);
    friend bool operator<=(const BigInteger& A, const BigInteger& B);
    friend bool operator>(const BigInteger& A, const BigInteger& B);
    friend bool operator>=(const BigInteger& A, const BigInteger& B);

    friend BigInteger operator+(const BigInteger& A, const BigInteger& B);
    friend BigInteger& operator+=(BigInteger& A, const BigInteger& B);

    friend BigInteger operator-(const BigInteger& A, const BigInteger& B);
    friend BigInteger& operator-=(BigInteger& A, const BigInteger& B);

private:
    int sign;
    int* digits;
    int size;

    BigInteger add(const BigInteger& N) const;
    BigInteger sub(const BigInteger& N) const;
    int compare(const BigInteger& N) const;
    void resize(int size);
    int abs_compare(const BigInteger& N) const;

    std::string to_string();
};
