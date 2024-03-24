#ifndef SONG_H
#define SONG_H
#include <string>
#include <vector>
using namespace std;

class Song
{
public:
    Song();
    Song(string title, string artist, int year, string lyrics, string url);

    string getTitle() const;
    void setTitle(const string &newTitle);

    string getArtist() const;
    void setArtist(const string &newArtist);

    int getYear() const;
    void setYear(int newYear);

    std::vector<std::string> getLyrics() const;
    void setLyrics(const std::vector<std::string> &newLyrics);

    string getUrl() const;
    void setUrl(const string &newUrl);

    string toString();
    bool operator<(const Song& other) const;

private:
    string title;
    string artist;
    int year;
    std::vector<std::string> lyrics;
    string url;
};

#endif // SONG_H
