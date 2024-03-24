#include "playlist.h"
#include"random"
#include"songexception.h"
#include <numeric>

Playlist::Playlist()
{
}

void Playlist::add(Song &s)
{

    auto it = std::find_if(songs.begin(), songs.end(), [s](const Song &song) {
        return song.getTitle() == s.getTitle() && s.getArtist() == song.getArtist();
    });
    if(it == songs.end())
    {
        songs.push_back(s);
    }
    else
    {
        throw SongException("A song " + s.getTitle() + " by " + s.getArtist() + " already exists.");

    }
}

void Playlist::clear()
{
    songs.clear();
}

void Playlist::remove(Song &s)
{
    auto it = std::find_if(songs.begin(), songs.end(), [s](const Song &song) {
        return song.getTitle() == s.getTitle() && song.getArtist() == s.getArtist();
    });
    if(it == songs.end())
    {
        throw SongException("The song " + s.getTitle() + " by " + s.getArtist() + " does not exist.");
    }
    else
    {
        songs.erase(it);
    }
}

std::vector<Song> Playlist::generateRandom(int n, std::vector<Song> songs)
{
    std::vector<Song> playlist;

    if (n > songs.size())
    {
        return playlist;
    }
    else
    {
        std::random_device generator;
        std::mt19937 gen(generator());
        std::vector<int> indices(songs.size());
        std::iota(indices.begin(), indices.end(), 0);  // Initialize indices from 0 to songs.size() - 1

        std::shuffle(indices.begin(), indices.end(), gen);  // Randomly shuffle the indices

        for (int i = 0; i < n; i++)
        {
            int randomIndex = indices[i];
            playlist.push_back(songs[randomIndex]);
        }
    }

    return playlist;
}
