#ifndef FILEREPOSITORY_H
#define FILEREPOSITORY_H
#include "repository.h"
#include <string>

class FileRepository : public Repository
{
public:
    FileRepository(const std::string& filepath);
    void load();
    void save();
    void store(const Song& s) override;
    void remove(const Song& s) override;

private:
    std::string filepath;
    friend class FileRepositoryTest;
};

#endif // FILEREPOSITORY_H
