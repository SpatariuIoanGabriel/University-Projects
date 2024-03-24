#ifndef SONGCOLLECTION_H
#define SONGCOLLECTION_H

#include "Song.h"
#include <string>
#include <vector>
#include <set>
#include <unordered_map>

class SongCollection {
private:
    std::vector<Song> songs;

public:
    SongCollection(std::string file_path);
    std::vector<Song> getSongs() const;
    std::set<std::string> getUniqueArtists() const;
    std::unordered_map<std::string, std::vector<Song>> groupByArtist() const;
    std::vector<Song> sortByArtist() const;
    std::vector<Song> sortByTitle() const;
    std::vector<Song> sortByLyrics() const;
    std::vector<Song> search(std::string word) const;
};

#endif
