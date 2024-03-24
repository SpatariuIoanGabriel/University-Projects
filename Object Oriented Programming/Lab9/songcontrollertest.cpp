#include "songcontrollertest.h"
#include <iostream>

void SongControllerTest::runAllTests()
{
    testAdd();
    testFind();
    testSortByArtistName();
    testSortByTitles();
    std::cout<<"All controller tests passed"<<endl;
}

void SongControllerTest::testAdd()
{
    Repository repository;
    SongController songController(repository);

    songController.add("Title", "Artist", 1, "Lyrics1", "url1");

    assert(repository.getAll().size() == 1);

}

void SongControllerTest::testFind()
{
    Repository repository;
    SongController songController(repository);

    songController.add("Title1", "Artist1", 1, "Lyrics1", "url1");
    songController.add("Title2", "Artist2", 2, "Lyrics2", "url2");

    const Song& song = songController.find("Title1", "Artist1");

    assert(song.getTitle() == "Title1");
    assert(song.getArtist() == "Artist1");
}

void SongControllerTest::testSortByArtistName()
{

    Repository repository;
    Song song1("z", "yy3", 1, "Lyrics1", "URL1");
    repository.store(song1);

    Song song2("a", "aa1", 2, "Lyrics2", "URL2");
    repository.store(song2);

    Song song3("c", "ff2", 3, "Lyrics3", "URL3");
    repository.store(song3);

    SongController sc = SongController(repository);
    std::vector<Song> songs = sc.sortByArtistName(true);
    assert(songs[0].getArtist() == "aa1");
    assert(songs[1].getArtist() == "ff2");
    assert(songs[2].getArtist() == "yy3");
    std::vector<Song> songs1 = sc.sortByArtistName(false);
    assert(songs1[2].getArtist() == "aa1");
    assert(songs1[1].getArtist() == "ff2");
    assert(songs1[0].getArtist() == "yy3");



}

void SongControllerTest::testSortByTitles()
{
    Repository repository;
    Song song1("z", "yy3", 1, "Lyrics1", "URL1");
    repository.store(song1);

    Song song2("a", "aa1", 2, "Lyrics2", "URL2");
    repository.store(song2);

    Song song3("c", "ff2", 3, "Lyrics3", "URL3");
    repository.store(song3);

    SongController sc = SongController(repository);
    std::vector<Song> songs = sc.sortByTitles(true);
    assert(songs[0].getTitle() == "a");
    assert(songs[1].getTitle() == "c");
    assert(songs[2].getTitle() == "z");
    std::vector<Song> songs1 = sc.sortByTitles(false);
    assert(songs1[0].getTitle() == "z");
    assert(songs1[1].getTitle() == "c");
    assert(songs1[2].getTitle() == "a");
}
