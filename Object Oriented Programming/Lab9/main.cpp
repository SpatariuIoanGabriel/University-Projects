#include "mainwindow.h"
#include "song.h"
#include "songexception.h"
#include "repository.h"
#include <QApplication>
#include <iostream>
#include <ostream>
#include "filerepository.h"
#include "songcontroller.h"
#include "repositorytest.h"
#include "filerepositorytest.h"
#include "songcontrollertest.h"
#include <vector>
#include "filerepository.h"

/*int main()
{

    RepositoryTest::runAllTests();
    FileRepositoryTest::runAllTests();
    SongControllerTest::runAllTests();

    QApplication a();
    //Repository repo;
    //SongController ctrl{repo};*/
//MainWindow w;
// w.show();

//return a.exec();


/*Repository repository;

    Song song1("z", "xxx", 1, "Lyrics1", "URL1");
    repository.store(song1);

    Song song2("f", "aaa", 2, "Lyrics2", "URL2");
    repository.store(song2);

    Song song3("a", "bbb", 3, "Lyrics3", "URL3");
    repository.store(song3);

    SongController sc = SongController(repository);

    std::vector<Song> songs = sc.sortByTitles(true);

    for(Song& song: songs)
    {
        std::cout<<song.getTitle()<<std::endl;
        std::cout<<song.getArtist()<<std::endl;
        std::vector<std::string> lyrics = song.getLyrics();
        for(int i = 0; i < lyrics.size(); i++)
        {
            std::cout<<lyrics.at(i)<<endl;
        }
        std::cout<<song.getUrl()<<std::endl;
        std::cout<<std::endl;
    }*/






int main(int argc, char *argv[])
{
    try
    {
        FileRepository fr = FileRepository("songs.txt");
        fr.save();
        fr.load();
    }
    catch (const std::invalid_argument& expt)
    {
        std::cerr << "Error: " << expt.what();
    }
    QApplication a(argc, argv);
    FileRepository repo("data.txt");
    SongController* ctrl = new SongController(repo);
    Playlist* ply = new Playlist();
    MainWindow w{ctrl, ply};
    w.show();


    return a.exec();
}
