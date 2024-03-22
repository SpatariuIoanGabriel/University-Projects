#include "BigInteger.h"

#include <cctype> // for isdigit
#include <iostream>
#include <iomanip>
#include <string>
#include <iterator>

using namespace std;


BigInteger::BigInteger() {
    this->digits = nullptr;
    this->sign = 0;
    this->size = 0;
}

BigInteger::BigInteger(const BigInteger& copy) {
    this->size = copy.size;
    this->sign = copy.sign;
    this->digits = new int[copy.size + 1];
    for (int i = 0; i < copy.size; i++)
        this->digits[i] = copy.digits[i];
}

BigInteger& BigInteger::operator=(BigInteger copy) {
    this->size = copy.size;
    this->sign = copy.sign;
    delete[] this->digits;
    this->digits = new int[copy.size + 1];
    for (int i = 0; i < copy.size; i++)
        this->digits[i] = copy.digits[i];
    return *this;
}

BigInteger::BigInteger(std::string s) {
    this->digits = new int [s.size() + 1];
    this->size = s.size();
    if (!isdigit(s[0])) {
        if (s[0] == '-')
            this->sign = -1;
        else
            this->sign = 1;
        for (int i = s.size() - 1; i >= 1; i--)
            this->digits[s.size() - i - 1] = s[i] - '0';
        this->size--;
    }
    else {
        this->sign = 1;
        for (int i = s.size() - 1; i >= 0; i--)
            this->digits[s.size() - (i + 1)] = s[i] - '0';
    }
    bool zero = true;
    for (int i = 0; i < this->size; i++)
        if (this->digits[i] != 0)
            zero = false;
    if (zero)
        this->sign = 0;
}

BigInteger::~BigInteger() {
    delete[] this->digits;
}

void BigInteger::resize(int size) {
    int *new_digits = new int[size + 1];
    for (int i = 0; i < this->size; i++)
        new_digits[i] = this->digits[i];
    delete[] this->digits;
    this->digits = new_digits;
}

int BigInteger::compare(const BigInteger& N) const {
    if (this->sign == 1 && N.sign == -1)
        return 1;
    if (this->sign == -1 && N.sign == 1)
        return -1;
    if (this->sign == 1) {
        if (this->size < N.size)
            return -1;
        if (this->size > N.size)
            return 1;
        //for (int i = this->size - 1; i >= 0; i--) //print number
        //	cout << this->digits[i];
        //cout << endl;
        //for (int i = N.size - 1; i >= 0; i--) //print number
        //	cout << N.digits[i];
        for (int i = N.size - 1; i >= 0; i--)
            if (N.digits[i] < this->digits[i])
                return 1;
            else if (N.digits[i] > this->digits[i])
                return -1;

    }
    if (this->sign == -1) {
        if (this->size < N.size)
            return 1;
        if (this->size > N.size)
            return -1;
        for (int i = N.size - 1; i >= 0; i--)
            if (N.digits[i] < this->digits[i])
                return -1;
            else if (N.digits[i] > this->digits[i])
                return 1;
    }
    return 0;
}

int BigInteger::abs_compare(const BigInteger& N) const {
    //for (int i = this->size - 1; i >= 0; i--) //print number
    //	cout << this->digits[i];

    //cout << endl;
    //for (int i = N.size - 1; i >= 0; i--) //print number
    //	cout << N.digits[i];
    if (this->size < N.size)
        return -1;
    if (this->size > N.size)
        return 1;
    for (int i = N.size - 1; i >= 0; i--)
        if (N.digits[i] < this->digits[i])
            return 1;
        else if (N.digits[i] > this->digits[i])
            return -1;
    return 0;
}

BigInteger BigInteger::add(const BigInteger& N) const {

    if (this->sign == 0)
        return N;
    if (N.sign == 0) {
        return *this;
    }
    if (this->sign == N.sign) {
        //for (int i = this->size - 1; i >= 0; i--) //print number
        //	cout << this->digits[i];
        BigInteger result;
        int SIZE = max(this->size, N.size);
        result.digits = new int[SIZE + 1];
        int carry = 0;
        int i = 0;
        while(i < min(this->size, N.size)) {
            result.digits[i] = this->digits[i] + N.digits[i] + carry;
            carry = result.digits[i] / 10;
            result.digits[i] %= 10;
            i++;
        }
        while (i < this->size) {
            result.digits[i] = this->digits[i] + carry;
            carry = result.digits[i] / 10;
            result.digits[i] %= 10;
            i++;
        }
        while (i < N.size) {
            result.digits[i] = N.digits[i] + carry;
            carry = result.digits[i] / 10;
            result.digits[i] %= 10;
            i++;
        }
        result.sign = this->sign;
        result.size = max(this->size, N.size);
        if (carry) {
            result.resize(max(this->size, N.size) + 2);
            result.digits[size] = carry;
            result.size++;
        }
        //for (int i = result.size - 1; i >= 0; i--) //print number
        //	cout << result.digits[i];
        return result;
    }
    else {
        if (this->abs_compare(N) == 1) {
            BigInteger result;
            result.digits = new int[this->size + 1];
            int borrow = 0;
            int i = 0;
            //for (int i = this->size - 1; i >= 0; i--) //print number
            //	cout << this->digits[i];
            //cout << "\n";
            //for (int i = N.size - 1; i >= 0; i--) //print number
            //	cout << N.digits[i];
            //cout << "\n";
            while (i < N.size) {
                result.digits[i] = this->digits[i] - N.digits[i] - borrow;
                borrow = 0;
                if (result.digits[i] < 0)
                    borrow = 1;
                result.digits[i] = (result.digits[i] + 10) % 10;
                i++;
            }
            while (i < this->size) {
                result.digits[i] = this->digits[i] - borrow;
                borrow = 0;
                if (result.digits[i] < 0)
                    borrow = 1;
                result.digits[i] = (result.digits[i] + 10) % 10;
                i++;
            }
            int size = this->size;
            /*cout << result.sign << " " << this->size << " " << size << " ";*/
            //for (int i = size - 1; i >= 0; i--) //print number
            //	cout << result.digits[i];
            while (result.digits[size - 1] == 0 && size > 1)
                size--;
            result.size = size;
            result.sign = this->sign;
            if (size != this->size)
                result.resize(size + 2);
            return result;
        }
        else if (this->abs_compare(N) == -1) {
            BigInteger result;
            result.digits = new int[N.size + 1];
            int borrow = 0;
            int i = 0;
            while (i < this->size) {
                result.digits[i] = N.digits[i] - this->digits[i] - borrow;
                borrow = 0;
                if (result.digits[i] < 0)
                    borrow = 1;
                result.digits[i] = (result.digits[i] + 10) % 10;
                i++;
            }
            while (i < N.size) {
                result.digits[i] = N.digits[i] - borrow;
                borrow = 0;
                if (result.digits[i] < 0)
                    borrow = 1;
                result.digits[i] = (result.digits[i] + 10) % 10;
                i++;
            }
            int size = N.size;
            while (result.digits[size - 1] == 0 && size > 1)
                size--;
            result.size = size;
            result.sign = N.sign;
            if (size != this->size)
                result.resize(size + 2);
            return result;
        }
        else {
            return BigInteger("0");
        }
    }
}
BigInteger BigInteger::sub(const BigInteger& N) const {
    BigInteger C(N);
    C.sign *= -1;
    return this->add(C);
}

bool operator==(const BigInteger& A, const BigInteger& B) {
    if (A.compare(B) == 0)
        return true;
    return false;
}

bool operator<=(const BigInteger& A, const BigInteger& B) {
    if (A.compare(B) <= 0)
        return true;
    return false;
}

bool operator>=(const BigInteger& A, const BigInteger& B) {
    if (A.compare(B) >= 0)
        return true;
    return false;
}

bool operator>(const BigInteger& A, const BigInteger& B) {
    if (A.compare(B) == 1)
        return true;
    return false;
}

bool operator<(const BigInteger& A, const BigInteger& B) {
    if (A.compare(B) == -1)
        return true;
    return false;
}

BigInteger& BigInteger::operator++() {
    *this = this->add(BigInteger("1"));
    return *this;
}



BigInteger BigInteger::operator++(int t) {
    BigInteger temp = *this;
    ++*this;
    return temp;
}

std::ostream& operator<<(std::ostream& stream, BigInteger N) {
    stream << N.to_string();
    return stream;
}

std::string BigInteger::to_string() {
    string str = "";
    if (this->sign == -1)
        str += "-";
    for (int i = this->size - 1; i >= 0; i--)
        str += this->digits[i] + '0';
    return str;
}

BigInteger operator+(const BigInteger& A, const BigInteger& B){
    return A.add(B);
}

BigInteger& operator+=(BigInteger& A, const BigInteger& B) {
    A = A.add(B);
    return A;
}

BigInteger operator-(const BigInteger& A, const BigInteger& B) {
    return A.sub(B);
}

BigInteger& operator-=(BigInteger& A, const BigInteger& B) {
    A = A.sub(B);
    return A;
}

int BigInteger::sgn() const{
    return this->sign;
}

void BigInteger::negate() {
    this->sign *= -1;
}
