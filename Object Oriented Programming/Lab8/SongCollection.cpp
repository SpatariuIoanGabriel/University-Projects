#include "SongCollection.h"
#include <fstream>
#include <sstream>
#include <algorithm>

SongCollection::SongCollection(std::string file_path) {
    std::ifstream file(file_path);
    if (!file.is_open()) {
        throw std::invalid_argument("Could not open file.");
    }

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::string artist, title, lyrics;
        std::getline(iss, artist, ',');
        std::getline(iss, title, ',');
        std::getline(iss, lyrics, ',');
        songs.push_back(Song(artist, title, lyrics));
    }

    file.close();
}

std::vector<Song> SongCollection::getSongs() const {
    return songs;
}

std::set<std::string> SongCollection::getUniqueArtists() const {
    std::set<std::string> uniqueArtists;
    for (const auto& song : songs) {
        uniqueArtists.insert(song.getArtist());
    }
    return uniqueArtists;
}

std::unordered_map<std::string, std::vector<Song>> SongCollection::groupByArtist() const {
    std::unordered_map<std::string, std::vector<Song>> groupedByArtist;
    for (const auto& song : songs) {
        groupedByArtist[song.getArtist()].push_back(song);
    }
    return groupedByArtist;
}

std::vector<Song> SongCollection::sortByArtist() const {
    std::vector<Song> sortedByArtist = songs;
    std::sort(sortedByArtist.begin(), sortedByArtist.end(),
              [](const Song& s1, const Song& s2) {
                  return s1.getArtist() < s2.getArtist();
              });
    return sortedByArtist;
}

std::vector<Song> SongCollection::sortByTitle() const {
    std::vector<Song> sortedByTitle = songs;
    std::sort(sortedByTitle.begin(), sortedByTitle.end(),
              [](const Song& s1, const Song& s2) {
                  return s1.getTitle() < s2.getTitle();
              });
    return sortedByTitle;
}

std::vector<Song> SongCollection::sortByLyrics() const {
    std::vector<Song> sortedByLyrics = songs;
    std::sort(sortedByLyrics.begin(), sortedByLyrics.end(),
              [](const Song& s1, const Song& s2) {
                  return s1.getLyrics() < s2.getLyrics();
              });
    return sortedByLyrics;
}

std::vector<Song> SongCollection::search(std::string word) const {
    std::vector<Song> searchResults;
    for (const auto &song: songs) {
        if (song.getArtist().find(word) != std::string::npos ||
            song.getTitle().find(word) != std::string::npos) {
            searchResults.push_back(song);
        }
        return searchResults;
    }
}
