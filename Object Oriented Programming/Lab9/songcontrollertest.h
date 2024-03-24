#ifndef SONGCONTROLLERTEST_H
#define SONGCONTROLLERTEST_H
#include "songcontroller.h"
#include<cassert>

class SongControllerTest
{
public:
    static void runAllTests();
    static void testAdd();
    static void testFind();
    static void testSortByArtistName();
    static void testSortByTitles();

};

#endif // SONGCONTROLLERTEST_H
