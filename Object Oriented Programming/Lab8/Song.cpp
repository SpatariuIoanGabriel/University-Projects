#include "Song.h"
#include <algorithm>
#include <cctype>
#include <sstream>

Song::Song(std::string artist, std::string title, std::string lyrics) {
    this->artist = artist;
    this->title = title;

    std::stringstream ss(lyrics);
    std::string word;
    while (ss >> word) {
        std::string clean_word;
        for (char c : word) {
            if (std::isalpha(c)) {
                clean_word += std::tolower(c);
            }
        }
        this->lyrics.push_back(clean_word);
    }
}

std::string Song::getArtist() const {
    return artist;
}

std::string Song::getTitle() const {
    return title;
}

std::vector<std::string> Song::getLyrics() const {
    return lyrics;
}
