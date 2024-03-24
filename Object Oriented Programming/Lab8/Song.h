#ifndef SONG_H
#define SONG_H

#include <string>
#include <vector>

class Song {
private:
    std::string artist;
    std::string title;
    std::vector<std::string> lyrics;

public:
    Song(std::string artist, std::string title, std::string lyrics);
    std::string getArtist() const;
    std::string getTitle() const;
    std::vector<std::string> getLyrics() const;
};

#endif //SONG_H
