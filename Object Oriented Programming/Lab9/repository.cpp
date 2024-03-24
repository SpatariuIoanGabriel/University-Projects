#include "repository.h"
#include<algorithm>
#include<stdexcept>
#include "songexception.h"

Repository::Repository()
{}

void Repository::store(const Song &s)
{
    auto it = std::find_if(songs.begin(), songs.end(), [s](const Song &song) {
        return song.getTitle() == s.getTitle() && song.getArtist() == s.getArtist();
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

const Song &Repository::find(string title, string artist)
{
    auto it = std::find_if(songs.begin(), songs.end(), [title, artist](const Song &song) {return song.getTitle() == title && song.getArtist() == artist;});
    if(it == songs.end())
    {
        throw SongException("The song " + title + " by " + artist + " does not exist.");
    }
    return *it;
}

void Repository::remove(const Song &s)
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

vector<Song> Repository::getAll()
{
    return songs;
}
