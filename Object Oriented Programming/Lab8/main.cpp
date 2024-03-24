#include <iostream>
#include "SongCollection.h"

int main() {
    try {
        SongCollection collection("songs.txt");
        std::cout << "Loaded " << collection.getSongs().size() << " songs from file.\n";

        std::cout << "Unique artists: ";
        for (const auto& artist : collection.getUniqueArtists()) {
            std::cout << artist << " ";
        }
        std::cout << "\n";

        auto groupedByArtist = collection.groupByArtist();
        std::cout << "Number of songs by artist:\n";
        std::vector<std::pair<std::string, int>> artistCounts;
        for (const auto& entry : groupedByArtist) {
            artistCounts.emplace_back(entry.first, entry.second.size());
        }
        std::sort(artistCounts.begin(), artistCounts.end(),
                  [](const auto& p1, const auto& p2) {
                      return p1.second > p2.second;
                  });
        int count = 0;
        for (const auto& entry : artistCounts) {
            std::cout << entry.first << ": " << entry.second << "\n";
            if (++count >= 10) {
                break;
            }
        }

        std::cout << "Songs sorted by artist:\n";
        for (const auto& song : collection.sortByArtist()) {
            std::cout << song.getArtist() << " - " << song.getTitle() << "\n";
        }

        std::cout << "Songs sorted by title:\n";
        for (const auto& song : collection.sortByTitle()) {
            std::cout << song.getTitle() << " by " << song.getArtist() << "\n";
        }

        std::cout << "Songs sorted by lyrics:\n";
        for (const auto& song : collection.sortByLyrics()) {
            std::cout << song.getArtist() << " - " << song.getTitle() << " (" << song.getLyrics().size() << " words)\n";
        }

        std::string searchWord = "love";
        std::cout << "Songs containing \"" << searchWord << "\":\n";
        for (const auto& song : collection.search(searchWord)) {
            std::cout << song.getTitle() << " by " << song.getArtist() << "\n";
        }
    }
    catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}
