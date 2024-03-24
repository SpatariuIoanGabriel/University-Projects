#ifndef FILEREPOSITORYTEST_H
#define FILEREPOSITORYTEST_H
#include "filerepository.h"
#include<cassert>

class FileRepositoryTest
{
public:
    FileRepositoryTest();

public:
    static void runAllTests();
    static void testStore();
    static void testRemove();

};

#endif // FILEREPOSITORYTEST_H
