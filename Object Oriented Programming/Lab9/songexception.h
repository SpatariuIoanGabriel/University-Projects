#ifndef SONGEXCEPTION_H
#define SONGEXCEPTION_H
#include<exception>
#include<string>

class SongException: public std::exception
{
public:
    explicit SongException(const char* message);

    explicit SongException(const std::string& message);

    virtual ~SongException() noexcept;

    virtual const char* what() const noexcept;

protected:
    std::string msg_;
};

#endif // SONGEXCEPTION_H
