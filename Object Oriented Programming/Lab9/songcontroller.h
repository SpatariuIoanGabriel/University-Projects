#ifndef SONGCONTROLLER_H
#define SONGCONTROLLER_H
#include "repository.h"
#include <string>
#include <algorithm>
#include <stack>
#include"action.h"
#include"add.h"
#include"delete.h"
#include<memory>
using namespace std;

class SongController
{
public:
    SongController(Repository &r);
    void add(string title, string artist, int year, string lyrics = "", string url = "");
    void remove(Song& song);
    const Song& find(string title, string artist);
    std::vector<Song> sortByArtistName(bool ascending = true);
    std::vector<Song> sortByTitles(bool ascending = true);
    void addSongAction( Song& song);
    void removeSongAction( Song& song);
    void undo();
    void redo();
    Repository &getRepository();


private:
    Repository &repo;
    stack <Action*> undoStack;
    stack <Action*>redoStack;

};

#endif // SONGCONTROLLER_
