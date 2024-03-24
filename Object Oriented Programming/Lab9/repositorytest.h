#ifndef REPOSITORYTEST_H
#define REPOSITORYTEST_H
#include "repository.h"
#include <cassert>



class RepositoryTest
{
public:
    static void runAllTests();
    static void testStore();
    static void testFind();
    static void testRemove();

};

#endif // REPOSITORYTEST_H
