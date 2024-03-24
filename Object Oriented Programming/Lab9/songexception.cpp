#include "songexception.h"

SongException::SongException(const char *message)
    : msg_(message) {}

SongException::SongException(const std::string &message)
    : msg_(message) {}

SongException::~SongException() noexcept {}

const char *SongException::what() const noexcept
{
    return msg_.c_str();
}




