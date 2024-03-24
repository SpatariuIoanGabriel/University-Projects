#include "songcontroller.h"


SongController::SongController(Repository& r): repo{r}
{}

void SongController::add(string title, string artist, int year, string lyrics, string url)
{
    Song s(title, artist, year, lyrics, url);
    repo.store(s);
}

void SongController::remove(Song &song)
{
    repo.remove(song);
}

const Song &SongController::find(string title, string artist)
{
    return repo.find(title, artist);
}

std::vector<Song> SongController::sortByArtistName(bool ascending)
{
    std::vector <Song> sortSongs = repo.getAll();
    if(ascending)
    {
        std::sort(sortSongs.begin(), sortSongs.end(), [](const Song& song1, const Song song2)
                  {
                      return song1.getArtist() < song2.getArtist();
                  });
        return sortSongs;
    }
    else
    {
        std::sort(sortSongs.begin(), sortSongs.end(), [](const Song& song1, const Song song2)
                  {
                      return song1.getArtist() > song2.getArtist();
                  });
        return sortSongs;
    }
}

std::vector<Song> SongController::sortByTitles(bool ascending)
{
    std::vector<Song> sortSongs = repo.getAll();
    if(ascending)
    {
        std::sort(sortSongs.begin(), sortSongs.end(), [](const Song& song1, const Song song2)
                  {
                      return song1.getTitle() < song2.getTitle();
                  });
        return sortSongs;
    }
    else
    {
        std::sort(sortSongs.begin(), sortSongs.end(), [](const Song& song1, const Song song2)
                  {
                      return song1.getTitle() > song2.getTitle();
                  });
        return sortSongs;
    }
}

void SongController::addSongAction( Song &song)
{
    Action* action = new ActionAdd(repo, song);
    action->apply();
    undoStack.push(action);

}

void SongController::removeSongAction( Song &song)
{
    Action* action = new ActionDelete(repo, song);
    action->apply();
    undoStack.push(action);
}

void SongController::undo()
{
    if(! undoStack.empty())
    {
        Action* lastAction = undoStack.top();
        undoStack.pop();
        lastAction->apply();
        redoStack.push(lastAction);
    }
}

void SongController::redo()
{
    if(! redoStack.empty())
    {
        Action* lastAction = redoStack.top();
        redoStack.pop();
        lastAction->apply();
        undoStack.push(lastAction);
    }
}

Repository &SongController::getRepository()
{
    return repo;
}
