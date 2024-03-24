#ifndef PLAYLIST_H
#define PLAYLIST_H
#include"song.h"

class Playlist
{
public:
    Playlist();
    void add(Song& song);
    void clear();
    void remove(Song& song);
    std::vector<Song> generateRandom(int n, std::vector<Song> songs);
private:
    std::vector<Song> songs;
};

#endif // PLAYLIST_H
