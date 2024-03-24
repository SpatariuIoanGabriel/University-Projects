#include "repositorytest.h"
#include<iostream>

void RepositoryTest::runAllTests()
{
    testStore();
    testFind();
    testRemove();
    std::cout<<"All repository tests passed"<<endl;
}

void RepositoryTest::testStore()
{
    Repository repository;

    Song song1("Title1", "Artist1", 1, "Lyrircs1", "url1");
    repository.store(song1);

    Song song2("Title2", "Artist2", 2, "Lyrircs2", "url2");
    repository.store(song2);
    assert(repository.getAll().size() == 2);
}

void RepositoryTest::testFind()
{
    Repository repository;

    Song song1("Title1", "Artist1", 1, "Lyrircs1", "url1");
    repository.store(song1);

    Song song2("Title2", "Artist2", 2, "Lyrircs2", "url2");
    repository.store(song2);

    const Song& foundSong = repository.find("Title2", "Artist2");
    assert(foundSong.getTitle() == "Title2");
    assert(foundSong.getArtist() == "Artist2");
}

void RepositoryTest::testRemove()
{
    Repository repository;

    Song song1("Title1", "Artist1", 1, "Lyrircs1", "url1");
    repository.store(song1);

    Song song2("Title2", "Artist2", 2, "Lyrircs2", "url2");
    repository.store(song2);

    repository.remove(song1);
    assert(repository.getAll().size() == 1);

    repository.remove(song2);
    assert(repository.getAll().size() == 0);
}
